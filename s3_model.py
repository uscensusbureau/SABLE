# Name:        s3_model.py
# Purpose:     Fit and evaluate classification models based on the text extracted from manually classified PDFs
# Invocation:  python3 s3_model.py <projName>

import codecs
from nltk.classify import *
from nltk.classify.util import *
from nltk.metrics import *
from nltk import FreqDist
from nltk import ngrams
from nltk import Text
from nltk import word_tokenize
import os
import random
import re
from sklearn.ensemble import *
from sklearn.linear_model import *
from sklearn.metrics import *
from sklearn.model_selection import *
from sklearn.naive_bayes import *
from sklearn.neighbors import *
from sklearn.svm import *
from sklearn.tree import *
import sys

# Name:        valid_arguments
# Purpose:     Check whether the command-line arguments are valid
# Parameters:  sys.argv (globally defined list of command-line arguments)
# Returns:     True (all arguments are valid) or False (at least one argument is invalid)

def valid_arguments():
    if len(sys.argv) == 2 and re.search(r"^[a-zA-Z][a-zA-Z_-]*$", sys.argv[1]):
        return True
    return False

# Name:        get_feats_inds
# Purpose:     Create model features, which are binary indicators of 1-grams and 2-grams
# Parameters:  text (string of text)
# Returns:     Dictionary of binary indicators of 1-grams and 2-grams in text

def get_feats_inds(text):
    t = Text(word_tokenize(text))
    g1s = [(g, True) for g in ngrams(t, 1)]
    g2s = [(g, True) for g in ngrams(t, 2)]
    # 3-grams, 4-grams, and so on can also be used
    # g3s = [(g, True) for g in ngrams(t, 3)]
    return dict(g1s + g2s)

# Name:        get_feats_counts
# Purpose:     Create model features, which are counts of 1-grams and 2-grams
# Parameters:  text (string of text)
# Returns:     Dictionary of counts of 1-grams and 2-grams in text

def get_feats_counts(text):
    t = Text(word_tokenize(text))
    g1s = [(g, count) for g, count in FreqDist(ngrams(t, 1)).items()]
    g2s = [(g, count) for g, count in FreqDist(ngrams(t, 2)).items()]
    # 3-grams, 4-grams, and so on can also be used
    # g3s = [(g, count) for g, count in FreqDist(ngrams(t, 3)).items()]
    return dict(g1s + g2s)

# Name:        evaluate
# Purpose :    Evaluate classifier by applying it to the test set and calculating various performance statistics
# Parameters:  classifier (fitted classification model)
#              posTest (list of indices of positive test observations)
#              negTest (list of indices of negative test observations)
#              posTextsDict (dictionary of positive texts)
#              negTextsDict (dictionary of negative texts)
#              posDocsDict (dictionary of positive document names)
#              negDocsDict (dictionary of negative document names)
# Returns:     

def evaluate(classifier, posTest, negTest, posTextsDict, negTextsDict, posDocsDict, negDocsDict):
    # Number of true positives
    tp = 0
    # Number of false negatives
    fn = 0
    # Number of true negatives
    tn = 0
    # Number of false positives
    fp = 0
    # List of true classes
    trueAll = []
    # List of predicted classes
    predAll = []
    
    # Print document names of false negatives
    print("False Negatives")
    print("---------------")
    for i in posTest:
        trueAll.append("pos")
        pred = classifier.classify(get_feats_inds(posTextsDict[i]))
        predAll.append(pred)
        if pred == "pos":
            tp += 1
        else:
            fn += 1
            print(posDocsDict[i])
    print("")
    
    # Print document names of false positives
    print("False Positives")
    print("---------------")
    for i in negTest:
        trueAll.append("neg")
        pred = classifier.classify(get_feats_inds(negTextsDict[i]))
        predAll.append(pred)
        if pred == "neg":
            tn += 1
        else:
            fp += 1
            print(negDocsDict[i])
    print("")
    
    # Accuracy
    acc = round((tp + tn)/(tp + tn + fn + fp), 3)
    
    # F1 score
    f1 = round((2*tp)/(2*tp + fn + fp), 3) if (2*tp + fn + fp) > 0 else "NaN"
    
    # True positive rate (also known as sensitivity and recall)
    tpr = round(tp/(tp + fn), 3) if (tp + fn) > 0 else "NaN"
    
    # True negative rate (also known as specificity)
    tnr = round(tn/(tn + fp), 3) if (tn + fp) > 0 else "NaN"
    
    # Positive predictive rate (also known as precision)
    ppr = round(tp/(tp + fp), 3) if (tp + fp) > 0 else "NaN"
    
    # Negative predictive rate
    npr = round(tn/(tn + fn), 3) if (tn + fn) > 0 else "NaN"
    
    # Kappa statistic
    p0 = (tp + tn)/(tp + tn + fn + fp)
    pe = ((tp + fn)*(tp + fp) + (tn + fp)*(tn + fn))/pow(tp + tn + fn + fp, 2)
    kappa = round((p0 - pe)/(1 - pe), 3) if pe < 1 else 1
    
    # Print classifier performance statistics
    print("Summary")
    print("-------")
    print("tp    = {}".format(tp))
    print("fn    = {}".format(fn))
    print("tn    = {}".format(tn))
    print("fp    = {}".format(fp))
    print("acc   = {}".format(acc))
    print("f1    = {}".format(f1))
    print("tpr   = {}".format(tpr))
    print("tnr   = {}".format(tnr))
    print("ppr   = {}".format(ppr))
    print("npr   = {}".format(npr))
    print("kappa = {}".format(kappa))
    print("")
    
    # Print confusion matrix
    print("Confusion Matrix")
    print("----------------")
    print(confusion_matrix(trueAll, predAll, labels=["pos", "neg"]))
    print("")
    return

# Name:        fit_models
# Purpose:     Fit text classification models
# Parameters:  projName (project name)
# Returns:     

def fit_models(projName):
    posTexts = []
    posDocs  = []
    negTexts = []
    negDocs  = []
    
    # Read in text from documents classified as positive
    posDir = sorted(os.listdir("/{}/pos_txt/".format(projName)))
    for f in posDir:
        nameMatch = re.search(r"^(\S+)\.txt$", f)
        if nameMatch:
            posDocs.append(nameMatch.group(1))
            txtFile = "/{}/pos_txt/{}.txt".format(projName, nameMatch.group(1))
            tmpFile = codecs.open(txtFile, "r")
            posTexts.append(tmpFile.readlines()[0])
            tmpFile.close()
    
    # Read in text from documents classified as negative
    negDir = sorted(os.listdir("/{}/neg_txt/".format(projName)))
    for f in negDir:
        nameMatch = re.search(r"^(\S+)\.txt$", f)
        if nameMatch:
            negDocs.append(nameMatch.group(1))
            txtFile = "/{}/neg_txt/{}.txt".format(projName, nameMatch.group(1))
            tmpFile = codecs.open(txtFile, "r")
            negTexts.append(tmpFile.readlines()[0])
            tmpFile.close()
    
    # Create dictionaries to facilitate referencing observations and their corresponding text 
    posIndex     = [i for i in range(len(posTexts))]
    posTextsDict = dict([(i, posTexts[i]) for i in posIndex])
    posDocsDict  = dict([(i, posDocs[i]) for i in posIndex])
    negIndex     = [i for i in range(len(negTexts))]
    negTextsDict = dict([(i, negTexts[i]) for i in negIndex])
    negDocsDict  = dict([(i, negDocs[i]) for i in negIndex])
    
    # Set random number seed if desired
    random.seed(1234567890)
    random.shuffle(posIndex)
    random.shuffle(negIndex)
    
    # Divide the data into training and test sets
    trainFrac = 2.0/3.0
    posCut = int(round(trainFrac * len(posIndex)))
    negCut = int(round(trainFrac * len(negIndex)))
    posTrain = sorted(posIndex[:posCut])
    posTest  = sorted(posIndex[posCut:])
    negTrain = sorted(negIndex[:negCut])
    negTest  = sorted(negIndex[negCut:])
    
    # Create features based on n-gram indicators
    posFeatsTrain = [(get_feats_inds(posTextsDict[i]), "pos") for i in posTrain]
    negFeatsTrain = [(get_feats_inds(negTextsDict[i]), "neg") for i in negTrain]
    featsTrain = posFeatsTrain + negFeatsTrain
    
    # Print number of positive and negative observations used for training and testing
    print("")
    print("Positive Training: {}".format(len(posTrain)))
    print("Positive Testing:  {}".format(len(posTest)))
    print("Negative Training: {}".format(len(negTrain)))
    print("Negative Testing:  {}\n".format(len(negTest)))
    print("")
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   Naive Bayes Classifier (NLTK Implementation)   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    classifierNB = NaiveBayesClassifier.train(featsTrain)
    classifierNB.show_most_informative_features(n=50)
    print("")
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   Naive Bayes Classifier (Bernoulli Model)   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    classifierNBBer = nltk.classify.SklearnClassifier(BernoulliNB(alpha=1.0))
    classifierNBBer.train(featsTrain)
    evaluate(classifierNBBer, posTest, negTest, posTextsDict, negTextsDict, posDocsDict, negDocsDict)
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   Naive Bayes Classifier (Bernoulli Model)   @@@")
    print("@@@   with Cross-Validated Smoothing Parameter   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    nFolds = 10
    alphaList = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.5, 5.0]
    classifierNBBerCV = nltk.classify.SklearnClassifier(GridSearchCV(BernoulliNB(), cv=nFolds, param_grid={"alpha": alphaList}))
    classifierNBBerCV.train(featsTrain)
    evaluate(classifierNBBerCV, posTest, negTest, posTextsDict, negTextsDict, posDocsDict, negDocsDict)
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   K-Nearest Neighbors Classifier   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    classifierKNN = nltk.classify.SklearnClassifier(KNeighborsClassifier(n_neighbors=5))
    classifierKNN.train(featsTrain)
    evaluate(classifierKNN, posTest, negTest, posTextsDict, negTextsDict, posDocsDict, negDocsDict)
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   K-Nearest Neighbors Classifier                       @@@")
    print("@@@   with Cross-Validated Number of Neighbors Parameter   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    nFolds = 10
    nNeighborsList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    classifierKNNCV = nltk.classify.SklearnClassifier(GridSearchCV(KNeighborsClassifier(), cv=nFolds, param_grid={"n_neighbors": nNeighborsList}))
    classifierKNNCV.train(featsTrain)
    evaluate(classifierKNNCV, posTest, negTest, posTextsDict, negTextsDict, posDocsDict, negDocsDict)
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   Linear Support Vector Classifier   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    classifierSVC = nltk.classify.SklearnClassifier(LinearSVC(class_weight="balanced", dual="auto"))
    classifierSVC.train(featsTrain)
    evaluate(classifierSVC, posTest, negTest, posTextsDict, negTextsDict, posDocsDict, negDocsDict)
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   Logistic Regression   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    classifierLR = nltk.classify.SklearnClassifier(LogisticRegression(class_weight="balanced"))
    classifierLR.train(featsTrain)
    evaluate(classifierLR, posTest, negTest, posTextsDict, negTextsDict, posDocsDict, negDocsDict)
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   Decision Tree Classifier   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    classifierTree = nltk.classify.SklearnClassifier(DecisionTreeClassifier(class_weight="balanced"))
    classifierTree.train(featsTrain)
    evaluate(classifierTree, posTest, negTest, posTextsDict, negTextsDict, posDocsDict, negDocsDict)
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   Random Forest Classifier   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    classifierForest = nltk.classify.SklearnClassifier(RandomForestClassifier(n_estimators=50, class_weight="balanced"))
    classifierForest.train(featsTrain)
    evaluate(classifierForest, posTest, negTest, posTextsDict, negTextsDict, posDocsDict, negDocsDict)
    
    return

def main():
    if valid_arguments():
        fit_models(sys.argv[1])
    else:
        print("\nInvalid arguments\n")
    return

if __name__ == "__main__":
    main()
