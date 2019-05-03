#Name:        s4_logistic.py
#Purpose:     Classify new PDFs as positive or negative using a logistic regression model and output predicted classes and probabilities
#Invocation:  python3 s4_logistic.py <projectName>

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

#Name:       valid_arguments
#Arguments:  sys.argv (globally defined list of command-line arguments)
#Purpose:    Check whether the command-line arguments are valid

def valid_arguments():
    valid = False
    if len(sys.argv) == 2:
        if re.search(r"^[a-zA-Z][a-zA-Z_-]*$", sys.argv[1]) != None:
            valid = True
    return valid

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

#Name:       format_prob
#Arguments:  prob (probability)
#Purpose:    Round probability to four decimal places and convert it into a string

def format_prob(prob):
    return str(round(prob, 4))

#Name:       fit_and_predict
#Arguments:  projectName
#Purpose:    Fit a logistic regression model and output predicted classes and probabilities

def fit_and_predict(projectName):
    posTexts  = []
    posDocs   = []
    negTexts  = []
    negDocs   = []
    predTexts = []
    predDocs  = []
    
    #Read in text from documents classified as positive
    posDir = sorted(os.listdir("/" + projectName + "/pos_txt/"))
    for f in posDir:
        nameMatch = re.search(r"^(\S+)\.txt$", f)
        if nameMatch:
            posDocs.append(nameMatch.group(1))
            txtFile = "/" + projectName + "/pos_txt/" + nameMatch.group(1) + ".txt"
            tmpFile = codecs.open(txtFile, "rU")
            posTexts.append(tmpFile.readlines()[0])
            tmpFile.close()
    
    #Read in text from documents classified as negative
    negDir = sorted(os.listdir("/" + projectName + "/neg_txt/"))
    for f in negDir:
        nameMatch = re.search(r"^(\S+)\.txt$", f)
        if nameMatch:
            negDocs.append(nameMatch.group(1))
            txtFile = "/" + projectName + "/neg_txt/" + nameMatch.group(1) + ".txt"
            tmpFile = codecs.open(txtFile, "rU")
            negTexts.append(tmpFile.readlines()[0])
            tmpFile.close()
    
    #Create features based on n-gram indicators
    posFeatsTrain = [(get_feats_inds(posText), "pos") for posText in posTexts]
    negFeatsTrain = [(get_feats_inds(negText), "neg") for negText in negTexts]
    featsTrain = posFeatsTrain + negFeatsTrain
    
    #Read in text from documents for prediction
    predDir = sorted(os.listdir("/" + projectName + "/pred_txt/"))
    for f in predDir:
        nameMatch = re.search(r"^(\S+)\.txt$", f)
        if nameMatch:
            predDocs.append(nameMatch.group(1))
            txtFile = "/" + projectName + "/pred_txt/" + nameMatch.group(1) + ".txt"
            tmpFile = codecs.open(txtFile, "rU")
            predTexts.append(tmpFile.readlines()[0])
            tmpFile.close()
    
    #Print number of positive and negative observations used for training and number of observations for prediction
    print("")
    print("Positive Training: " + str(len(posTexts)))
    print("Negative Training: " + str(len(negTexts)))
    print("Prediction:        " + str(len(predTexts)) + "\n")
    
    #Fit a logistic regression model and apply it to new observations
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   Logistic Regression   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    classifierLR = nltk.classify.SklearnClassifier(LogisticRegression(penalty="l2", C=1, class_weight="balanced"))
    classifierLR.train(featsTrain)
    predClasses = [classifierLR.classify(get_feats_inds(predText)) for predText in predTexts]
    predProbs = [classifierLR.prob_classify(get_feats_inds(predText)) for predText in predTexts]
    
    #Create output
    outputFile = "/" + projectName + "/pred_output.txt"
    varNames = ["docName", "predClass", "probPos", "probNeg"]
    f = open(outputFile, "w")
    f.write("|".join(varNames) + "\n")
    for i in range(len(predTexts)):
        line = [predDocs[i], predClasses[i], format_prob(predProbs[i].prob("pos")), format_prob(predProbs[i].prob("neg"))]
        f.write("|".join(line) + "\n")
    f.close()
    os.system("chmod 777 " + outputFile)
    
    return

def main():
    if valid_arguments():
        fit_and_predict(sys.argv[1])
    else:
        print("\nInvalid arguments\n")
    return

if __name__ == "__main__":
    main()
