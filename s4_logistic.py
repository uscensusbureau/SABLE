# Name:        s4_logistic.py
# Purpose:     Classify new PDFs as positive or negative using a logistic regression model and output predicted classes and probabilities
# Invocation:  python3 s4_logistic.py <projName>

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
from sklearn.linear_model import *
from sklearn.metrics import *
from sklearn.model_selection import *
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

# Name:        format_prob
# Purpose:     Round probability to four decimal places and convert it into a string
# Parameters:  prob (probability)
# Returns:     String representing probability rounded to four decimal places

def format_prob(prob):
    return str(round(prob, 4))

# Name:        fit_and_predict
# Purpose:     Fit a logistic regression model and output predicted classes and probabilities
# Parameters:  projName (project name)
# Returns:     

def fit_and_predict(projName):
    posTexts  = []
    posDocs   = []
    negTexts  = []
    negDocs   = []
    predTexts = []
    predDocs  = []
    
    # Read in text from documents classified as positive
    posDir = sorted(os.listdir("./{}/pos_txt".format(projName)))
    for f in posDir:
        nameMatch = re.search(r"^(\S+)\.txt$", f)
        if nameMatch:
            posDocs.append(nameMatch.group(1))
            txtFile = "./{}/pos_txt/{}.txt".format(projName, nameMatch.group(1))
            tmpFile = codecs.open(txtFile, "r")
            posTexts.append(tmpFile.readlines()[0])
            tmpFile.close()
    
    # Read in text from documents classified as negative
    negDir = sorted(os.listdir("./{}/neg_txt".format(projName)))
    for f in negDir:
        nameMatch = re.search(r"^(\S+)\.txt$", f)
        if nameMatch:
            negDocs.append(nameMatch.group(1))
            txtFile = "./{}/neg_txt/{}.txt".format(projName, nameMatch.group(1))
            tmpFile = codecs.open(txtFile, "r")
            negTexts.append(tmpFile.readlines()[0])
            tmpFile.close()
    
    # Create features based on n-gram indicators
    posFeatsTrain = [(get_feats_inds(posText), "pos") for posText in posTexts]
    negFeatsTrain = [(get_feats_inds(negText), "neg") for negText in negTexts]
    featsTrain = posFeatsTrain + negFeatsTrain
    
    # Read in text from documents for prediction
    predDir = sorted(os.listdir("./{}/pred_txt".format(projName)))
    for f in predDir:
        nameMatch = re.search(r"^(\S+)\.txt$", f)
        if nameMatch:
            predDocs.append(nameMatch.group(1))
            txtFile = "./{}/pred_txt/{}.txt".format(projName, nameMatch.group(1))
            tmpFile = codecs.open(txtFile, "r")
            predTexts.append(tmpFile.readlines()[0])
            tmpFile.close()
    
    # Print number of positive and negative observations used for training and number of observations for prediction
    print("")
    print("Positive Training: {}".format(len(posTexts)))
    print("Negative Training: {}".format(len(negTexts)))
    print("Prediction:        {}\n".format(len(predTexts)))
    
    if len(posFeatsTrain) >= 10 and len(negFeatsTrain) >= 10:
    
        # Fit a logistic regression model and apply it to new observations
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("@@@   Logistic Regression   @@@")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        classifierLR = nltk.classify.SklearnClassifier(LogisticRegression(penalty="l2", C=1, class_weight="balanced"))
        classifierLR.train(featsTrain)
        predClasses = [classifierLR.classify(get_feats_inds(predText)) for predText in predTexts]
        predProbs = [classifierLR.prob_classify(get_feats_inds(predText)) for predText in predTexts]
        
        # Print predicted positives
        print("Predicted Positives")
        print("-------------------")
        for i in range(len(predTexts)):
            if predClasses[i] == "pos":
                print(predDocs[i])
        print("")
        
        # Create output
        outputFile = {}/pred_output.txt".format(projName)
        varNames = ["docName", "predClass", "probPos", "probNeg"]
        f = open(outputFile, "w")
        f.write("|".join(varNames) + "\n")
        for i in range(len(predTexts)):
            line = [predDocs[i], predClasses[i], format_prob(predProbs[i].prob("pos")), format_prob(predProbs[i].prob("neg"))]
            f.write("|".join(line) + "\n")
        f.close()
    
    return

def main():
    # Check valid arguments
    if valid_arguments():
        fit_and_predict(sys.argv[1])
    else:
        print("\nInvalid arguments\n")
    return

if __name__ == "__main__":
    main()
