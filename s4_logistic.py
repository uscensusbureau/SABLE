#Name:        s4_logistic.py
#Purpose:     Classify new PDFs as positive or negative using a logistic regression model and output predicted classes and probabilities
#Invocation:  python3 s4_logistic.py <project name>

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
#Arguments:  projname (project name)
#Purpose:    Fit a logistic regression model and output predicted classes and probabilities

def fit_and_predict(projname):
    pos_texts  = []
    pos_docs   = []
    neg_texts  = []
    neg_docs   = []
    pred_texts = []
    pred_docs  = []
    
    #Read in text from documents classified as positive
    pos_directory = sorted(os.listdir("/" + projname + "/pos_txt/"))
    for f in pos_directory:
        namematch = re.search(r"^(\S+)\.txt$", f)
        if namematch:
            pos_docs.append(namematch.group(1))
            txtfile = "/" + projname + "/pos_txt/" + namematch.group(1) + ".txt"
            tmpfile = codecs.open(txtfile, "rU")
            pos_texts.append(tmpfile.readlines()[0])
            tmpfile.close()
    
    #Read in text from documents classified as negative
    neg_directory = sorted(os.listdir("/" + projname + "/neg_txt/"))
    for f in neg_directory:
        namematch = re.search(r"^(\S+)\.txt$", f)
        if namematch:
            neg_docs.append(namematch.group(1))
            txtfile = "/" + projname + "/neg_txt/" + namematch.group(1) + ".txt"
            tmpfile = codecs.open(txtfile, "rU")
            neg_texts.append(tmpfile.readlines()[0])
            tmpfile.close()
    
    #Create features based on n-gram indicators
    pos_feats_train = [(get_feats_inds(pos_text), "pos") for pos_text in pos_texts]
    neg_feats_train = [(get_feats_inds(neg_text), "neg") for neg_text in neg_texts]
    feats_train = pos_feats_train + neg_feats_train
    
    #Read in text from documents for prediction
    pred_directory = sorted(os.listdir("/" + projname + "/pred_txt/"))
    for f in pred_directory:
        namematch = re.search(r"^(\S+)\.txt$", f)
        if namematch:
            pred_docs.append(namematch.group(1))
            txtfile = "/" + projname + "/pred_txt/" + namematch.group(1) + ".txt"
            tmpfile = codecs.open(txtfile, "rU")
            pred_texts.append(tmpfile.readlines()[0])
            tmpfile.close()
    
    #Print number of positive and negative observations used for training and number of observations for prediction
    print("")
    print("Positive Training: " + str(len(pos_texts)))
    print("Negative Training: " + str(len(neg_texts)))
    print("Prediction:        " + str(len(pred_texts)) + "\n")
    
    #Fit a logistic regression model and apply it to new observations
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   Logistic Regression   @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    classifier_logit = nltk.classify.SklearnClassifier(LogisticRegression(penalty="l2", C=1, class_weight="balanced"))
    classifier_logit.train(feats_train)
    pred_classes = [classifier_logit.classify(get_feats_inds(pred_text)) for pred_text in pred_texts]
    pred_probs = [classifier_logit.prob_classify(get_feats_inds(pred_text)) for pred_text in pred_texts]
    
    #Create output
    outputfile = "/" + projname + "/pred_output.txt"
    var_names = ["document_name", "predicted_class", "probability_positive", "probability_negative"]
    f = open(outputfile, "w")
    f.write("|".join(var_names) + "\n")
    for i in range(len(pred_texts)):
        line = [pred_docs[i], pred_classes[i], format_prob(pred_probs[i].prob("pos")), format_prob(pred_probs[i].prob("neg"))]
        f.write("|".join(line) + "\n")
    f.close()
    os.system("chmod 777 " + outputfile)
    
    return

def main():
    if valid_arguments():
        fit_and_predict(sys.argv[1])
    else:
        print("\nInvalid arguments\n")
    return

if __name__ == "__main__":
    main()
