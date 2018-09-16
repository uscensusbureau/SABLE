#Name:            s3_model.py
#Purpose:         Classify PDFs as positive or negative based on the extracted text stored in the /project/pos_txt/
#                 and /project/neg_txt/ folders
#Data Layout:     See README.md
#Python Version:  3

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

#Name:       get_feats_inds
#Arguments:  text (string of text)
#Purpose:    Return binary indicators of 1-grams and 2-grams in text

def get_feats_inds(text):
    t = Text(word_tokenize(text))
    g1s = [(g, True) for g in ngrams(t, 1)]
    g2s = [(g, True) for g in ngrams(t, 2)]
    #3-grams, 4-grams, and so on can also be used
    #g3s = [(g, True) for g in ngrams(t, 3)]
    return dict(g1s + g2s)

#Name:       get_feats_counts
#Arguments:  text (string of text)
#Purpose:    Return counts of 1-grams and 2-grams in text

def get_feats_counts(text):
    t = Text(word_tokenize(text))
    g1s = [(g, count) for g, count in FreqDist(ngrams(t, 1)).items()]
    g2s = [(g, count) for g, count in FreqDist(ngrams(t, 2)).items()]
    #3-grams, 4-grams, and so on can also be used
    #g3s = [(g, count) for g, count in FreqDist(ngrams(t, 3)).items()]
    return dict(g1s + g2s)

#Name:       evaluate
#Arguments:  classifier (fitted classification model)
#            pos_test (list of indices of positive test observations)
#            neg_test (list of indices of negative test observations)
#            pos_texts_dict (dictionary of positive texts)
#            neg_texts_dict (dictionary of negative texts)
#            pos_docs_dict (dictionary of positive document names)
#            neg_docs_dict (dictionary of negative document names)
#Purpose:    Evaluate classifier by applying it to the test set and calculating various performance statistics

def evaluate(classifier, pos_test, neg_test, pos_texts_dict, neg_texts_dict, pos_docs_dict, neg_docs_dict):
    #Number of true positives
    tp = 0
    #Number of false negatives
    fn = 0
    #Number of true negatives
    tn = 0
    #Number of false positives
    fp = 0
    #List of true classes
    true_all = []
    #List of predicted classes
    pred_all = []
    
    #Print document names of false negatives
    print("False Negatives")
    print("---------------")
    for i in pos_test:
        true_all.append("pos")
        pred = classifier.classify(get_feats_inds(pos_texts_dict[i]))
        pred_all.append(pred)
        if pred == "pos":
            tp += 1
        else:
            fn += 1
            print(pos_docs_dict[i])
    print("")
    
    #Print document names of false positives
    print("False Positives")
    print("---------------")
    for i in neg_test:
        true_all.append("neg")
        pred = classifier.classify(get_feats_inds(neg_texts_dict[i]))
        pred_all.append(pred)
        if pred == "neg":
            tn += 1
        else:
            fp += 1
            print(neg_docs_dict[i])
    print("")
    
    #Accuracy
    acc = round((tp + tn)/(tp + tn + fn + fp), 3)
    
    #F1 score
    if (2*tp + fn + fp) > 0:
        f1 = round((2*tp)/(2*tp + fn + fp), 3)
    else:
        f1 = "NaN"
    
    #True positive rate (also known as sensitivity and recall)
    if (tp + fn) > 0:
        tpr = round(tp/(tp + fn), 3)
    else:
        tpr = "NaN"
    
    #True negative rate (also known as specificity)
    if (tn + fp) > 0:
        tnr = round(tn/(tn + fp), 3)
    else:
        tnr = "NaN"
    
    #Positive predictive rate (also known as precision)
    if (tp + fp) > 0:
        ppr = round(tp/(tp + fp), 3)
    else:
        ppr = "NaN"
    
    #Negative predictive rate
    if (tn + fn) > 0:
        npr = round(tn/(tn + fn), 3)
    else:
        npr = "NaN"
    
    #Kappa statistic
    p0 = (tp + tn)/(tp + tn + fn + fp)
    pe = ((tp + fn)*(tp + fp) + (tn + fp)*(tn + fn))/pow(tp + tn + fn + fp, 2)
    if pe < 1:
        kappa = round((p0 - pe)/(1 - pe), 3)
    else:
        kappa = 1
    
    #Print classifier performance statistics
    print("Summary")
    print("-------")
    print("tp    = " + str(tp))
    print("fn    = " + str(fn))
    print("tn    = " + str(tn))
    print("fp    = " + str(fp))
    print("acc   = " + str(acc))
    print("f1    = " + str(f1))
    print("tpr   = " + str(tpr))
    print("tnr   = " + str(tnr))
    print("ppr   = " + str(ppr))
    print("npr   = " + str(npr))
    print("kappa = " + str(kappa))
    print("")
    
    #Print confusion matrix
    print("Confusion Matrix")
    print("----------------")
    print(confusion_matrix(true_all, pred_all, ["pos", "neg"]))
    print("")
    return

def main():
    pos_texts = []
    pos_docs  = []
    neg_texts = []
    neg_docs  = []
    
    #Read in text from documents classified as positive
    pos_directory = sorted(os.listdir("/project/pos_txt/"))
    for f in pos_directory:
        namematch = re.search(r"^(\S+)\.txt$", f)
        if namematch:
            pos_docs.append(namematch.group(1))
            txtfile = "/project/pos_txt/" + namematch.group(1) + ".txt"
            tmpfile = codecs.open(txtfile, "rU")
            pos_texts.append(tmpfile.readlines()[0])
            tmpfile.close()
    
    #Read in text from documents classified as negative
    neg_directory = sorted(os.listdir("/project/neg_txt/"))
    for f in neg_directory:
        namematch = re.search(r"^(\S+)\.txt$", f)
        if namematch:
            neg_docs.append(namematch.group(1))
            txtfile = "/project/neg_txt/" + namematch.group(1) + ".txt"
            tmpfile = codecs.open(txtfile, "rU")
            neg_texts.append(tmpfile.readlines()[0])
            tmpfile.close()
    
    #Create dictionaries to facilitate referencing observations and their corresponding text 
    pos_index      = [i for i in range(len(pos_texts))]
    pos_texts_dict = dict([(i, pos_texts[i]) for i in pos_index])
    pos_docs_dict  = dict([(i, pos_docs[i]) for i in pos_index])
    neg_index      = [i for i in range(len(neg_texts))]
    neg_texts_dict = dict([(i, neg_texts[i]) for i in neg_index])
    neg_docs_dict  = dict([(i, neg_docs[i]) for i in neg_index])
    
    #Set random number seed if desired
    random.seed(1234567890)
    random.shuffle(pos_index)
    random.shuffle(neg_index)
    
    #Two-thirds of the observations are used for training, and the remaining one-third is used for testing/validation
    train_frac = 2.0/3.0
    pos_cut = int(round(train_frac * len(pos_index)))
    neg_cut = int(round(train_frac * len(neg_index)))
    pos_train = sorted(pos_index[:pos_cut])
    pos_test  = sorted(pos_index[pos_cut:])
    neg_train = sorted(neg_index[:neg_cut])
    neg_test  = sorted(neg_index[neg_cut:])
    
    #Create features based on n-gram indicators
    pos_feats_train = [(get_feats_inds(pos_texts_dict[i]), "pos") for i in pos_train]
    neg_feats_train = [(get_feats_inds(neg_texts_dict[i]), "neg") for i in neg_train]
    feats_train = pos_feats_train + neg_feats_train
    
    #Print number of positive and negative observations used for training and testing
    print("")
    print("Positive Training: " + str(len(pos_train)))
    print("Positive Testing:  " + str(len(pos_test)))
    print("Negative Training: " + str(len(neg_train)))
    print("Negative Testing:  " + str(len(neg_test)) + "\n")
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   Naive Bayes Classifier (NLTK Implementation)   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    classifier_nb = NaiveBayesClassifier.train(feats_train)
    classifier_nb.show_most_informative_features(n=50)
    print("")
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   Naive Bayes Classifier (Bernoulli Model)   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    classifier_nbber = nltk.classify.SklearnClassifier(BernoulliNB(alpha=1.0))
    classifier_nbber.train(feats_train)
    evaluate(classifier_nbber, pos_test, neg_test, pos_texts_dict, neg_texts_dict, pos_docs_dict, neg_docs_dict)
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   Naive Bayes Classifier (Bernoulli Model)   @@@")
    print("@@@   with Cross-Validated Smoothing Parameter   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    n_folds = 10
    alpha_list = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.5, 5.0]
    classifier_nbbercv = nltk.classify.SklearnClassifier(GridSearchCV(BernoulliNB(), cv=n_folds, param_grid={"alpha": alpha_list}))
    classifier_nbbercv.train(feats_train)
    evaluate(classifier_nbbercv, pos_test, neg_test, pos_texts_dict, neg_texts_dict, pos_docs_dict, neg_docs_dict)
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   K-Nearest Neighbors Classifier   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    classifier_knn = nltk.classify.SklearnClassifier(KNeighborsClassifier(n_neighbors=5))
    classifier_knn.train(feats_train)
    evaluate(classifier_knn, pos_test, neg_test, pos_texts_dict, neg_texts_dict, pos_docs_dict, neg_docs_dict)
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   K-Nearest Neighbors Classifier                       @@@")
    print("@@@   with Cross-Validated Number of Neighbors Parameter   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    n_folds = 10
    n_neighbors_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    classifier_knncv = nltk.classify.SklearnClassifier(GridSearchCV(KNeighborsClassifier(), cv=n_folds, param_grid={"n_neighbors": n_neighbors_list}))
    classifier_knncv.train(feats_train)
    evaluate(classifier_knncv, pos_test, neg_test, pos_texts_dict, neg_texts_dict, pos_docs_dict, neg_docs_dict)
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   Linear Support Vector Classifier   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    classifier_svc = nltk.classify.SklearnClassifier(LinearSVC(class_weight="balanced"))
    classifier_svc.train(feats_train)
    evaluate(classifier_svc, pos_test, neg_test, pos_texts_dict, neg_texts_dict, pos_docs_dict, neg_docs_dict)
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   Logistic Regression   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    classifier_logit = nltk.classify.SklearnClassifier(LogisticRegression(class_weight="balanced"))
    classifier_logit.train(feats_train)
    evaluate(classifier_logit, pos_test, neg_test, pos_texts_dict, neg_texts_dict, pos_docs_dict, neg_docs_dict)
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   Decision Tree Classifier   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    classifier_tree = nltk.classify.SklearnClassifier(DecisionTreeClassifier(class_weight="balanced"))
    classifier_tree.train(feats_train)
    evaluate(classifier_tree, pos_test, neg_test, pos_texts_dict, neg_texts_dict, pos_docs_dict, neg_docs_dict)
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   Random Forest Classifier   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    classifier_forest = nltk.classify.SklearnClassifier(RandomForestClassifier(n_estimators=50, class_weight="balanced"))
    classifier_forest.train(feats_train)
    evaluate(classifier_forest, pos_test, neg_test, pos_texts_dict, neg_texts_dict, pos_docs_dict, neg_docs_dict)
    
    return

if __name__ == "__main__":
    main()
