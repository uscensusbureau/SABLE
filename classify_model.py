#Name:            classify_model.py
#Purpose:         Classify PDFs as positive or negative based on the extracted text stored in the /data/pos_txt/
#                 and /data/neg_txt/ folders
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
from sklearn.naive_bayes import *
from sklearn.svm import *
from sklearn.tree import *

#Name:       get_feats_inds
#Arguments:  text (string of text)
#Purpose:    Return binary indicators of 1-grams and 2-grams in text

def get_feats_inds(text):
    t = Text(word_tokenize(text))
    g1s = [(g, True) for g in ngrams(t, 1)]
    g2s = [(g, True) for g in ngrams(t, 2)]
    return dict(g1s + g2s)

#Name:       get_feats_counts
#Arguments:  text (string of text)
#Purpose:    Return counts of 1-grams and 2-grams in text

def get_feats_counts(text):
    t = Text(word_tokenize(text))
    g1s = [(g, count) for g, count in FreqDist(ngrams(t, 1)).items()]
    g2s = [(g, count) for g, count in FreqDist(ngrams(t, 2)).items()]
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
    
    #Print document names of false negatives
    print("False Negatives")
    print("---------------")
    for i in pos_test:
        pred = classifier.classify(get_feats_inds(pos_texts_dict[i]))
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
        pred = classifier.classify(get_feats_inds(neg_texts_dict[i]))
        if pred == "neg":
            tn += 1
        else:
            fp += 1
            print(neg_docs_dict[i])
    print("")
    
    #Accuracy
    acc = round((tp + tn)/(tp + tn + fn + fp), 3)
    #F1 score
    f1 = round((2*tp)/(2*tp + fn + fp), 3)
    #True positive rate (also known as sensitivity and recall)
    tpr = round(tp/(tp + fn), 3)
    #True negative rate (also known as specificity)
    tnr = round(tn/(tn + fp), 3)
    #Positive predictive rate (also known as precision)
    ppr = round(tp/(tp + fp), 3)
    #Negative predictive rate
    npr = round(tn/(tn + fn), 3)
    #Kappa statistic
    p0 = (tp + tn)/(tp + tn + fn + fp)
    pe = ((tp + fn)*(tp + fp) + (tn + fp)*(tn + fn))/pow(tp + tn + fn + fp, 2)
    kappa = round((p0 - pe)/(1 - pe), 3)
    
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
    print("kappa = " + str(kappa) + "\n")
    return

def main():
    pos_texts = []
    pos_docs  = []
    neg_texts = []
    neg_docs  = []
    
    #Read in text from documents classified as positive
    pos_directory = os.listdir("/data/pos_txt/")
    for f in pos_directory:
        namematch = re.search(r"^(\S+)\.txt$", f)
        if namematch:
            pos_docs.append(namematch.group(1))
            txtfile = "/data/pos_txt/" + namematch.group(1) + ".txt"
            tmpfile = codecs.open(txtfile, "rU")
            pos_texts.append(tmpfile.readlines()[0])
            tmpfile.close()
    
    #Read in text from documents classified as negative
    neg_directory = os.listdir("/data/neg_txt/")
    for f in neg_directory:
        namematch = re.search(r"^(\S+)\.txt$", f)
        if namematch:
            neg_docs.append(namematch.group(1))
            txtfile = "/data/neg_txt/" + namematch.group(1) + ".txt"
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
    pos_train = pos_index[:pos_cut]
    pos_test  = pos_index[pos_cut:]
    neg_train = neg_index[:neg_cut]
    neg_test  = neg_index[neg_cut:]
    
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
    
    print("==================================================")
    print("Naive Bayes Classifier (NLTK Implementation)\n")
    classifier_nb = NaiveBayesClassifier.train(feats_train)
    classifier_nb.show_most_informative_features(n=50)
    print("")
    
    print("==================================================")
    print("Naive Bayes Classifier for Bernoulli Models\n")
    classifier_nbber = nltk.classify.SklearnClassifier(BernoulliNB())
    classifier_nbber.train(feats_train)
    evaluate(classifier_nbber, pos_test, neg_test, pos_texts_dict, neg_texts_dict, pos_docs_dict, neg_docs_dict)
    
    print("==================================================")
    print("Linear Support Vector Classifier\n")
    classifier_svc = nltk.classify.SklearnClassifier(LinearSVC())
    classifier_svc.train(feats_train)
    evaluate(classifier_svc, pos_test, neg_test, pos_texts_dict, neg_texts_dict, pos_docs_dict, neg_docs_dict)
    
    print("==================================================")
    print("Logistic Regression\n")
    classifier_logit = nltk.classify.SklearnClassifier(LogisticRegression())
    classifier_logit.train(feats_train)
    evaluate(classifier_logit, pos_test, neg_test, pos_texts_dict, neg_texts_dict, pos_docs_dict, neg_docs_dict)
    
    print("==================================================")
    print("Decision Tree\n")
    classifier_tree = nltk.classify.SklearnClassifier(DecisionTreeClassifier())
    classifier_tree.train(feats_train)
    evaluate(classifier_tree, pos_test, neg_test, pos_texts_dict, neg_texts_dict, pos_docs_dict, neg_docs_dict)
    
    print("==================================================")
    print("Random Forest\n")
    classifier_forest = nltk.classify.SklearnClassifier(RandomForestClassifier(n_estimators=50))
    classifier_forest.train(feats_train)
    evaluate(classifier_forest, pos_test, neg_test, pos_texts_dict, neg_texts_dict, pos_docs_dict, neg_docs_dict)
    return

if __name__ == "__main__":
    main()
