# SABLE

This readme is a work in progress.

## Introduction

SABLE, which stands for Scraping Assisted by Learning, is a collection of tools for web crawling and web scraping.  Some elements involve supervised machine learning to perform text classification.  The idea is to discover potential new sources of data on the web in PDF format, apply a classification model to predict whether the PDF contains useful data, and then scrape data using templates, text analysis, and other models.  SABLE was initially developed to scrape data on tax revenue collections from state and local government websites but has been applied to other settings such as finding population and housing statistics on the websites of foreign national statistical agencies.

## Software

SABLE is based on the following pieces of open-source software:

* [Apache Nutch](http://nutch.apache.org/)
* [Python](http://www.python.org/)
  * [scikit-learn](http://www.scikit-learn.org/stable/)
  * [Natural Language Toolkit (NLTK)](https://www.nltk.org/)
  * [PDFMiner3K](https://github.com/jaepil/pdfminer3k/)

Apache Nutch is a Java-based web crawler and is used to crawl websites, discover PDFs, and compile a training set of documents for model building.  Python is used to extract text from PDFs and to fit and evaluate text classification models based on various supervised machine learning algorithms.  These algorithms consist of the following:

* Naive Bayes
* K-Nearest Neighbors
* Linear Support Vector Classifier
* Logistic Regression
* Decision Tree
* Random Forest

## Description of Contents

This repository contains Python programs for converting PDFs to TXT format and for fitting and evaluating classification models that predict whether a PDF contains useful data based on the extracted text.  Also provided are PDF-to-TXT conversion examples, an example training set, and corresponding model output.  This repository also contains lists of NLTK stop words for multiple languages.  Foreign accent marks have been removed from characters, and some lists have been modified slightly in other ways.

## Organization of Files

The following organization of data, programs, and supplementary files on a Linux/Unix system is assumed.  PDFs that are to be converted to TXT format and used as input into building classification models should be manually classified as "positive" (contains useful data) or "negative" and placed accordingly in the ```/data/pos_pdf/``` and ```/data/neg_pdf/``` folders.  The extracted text is output to the ```/data/pos_txt/``` and ```/data/neg_txt/``` folders.  Additional information can be found in the comments in the Python programs. <br />

### Data Folders

```
/data/neg_pdf/
/data/neg_prob/
/data/neg_txt/
/data/neg_xml/
/data/pos_pdf/
/data/pos_prob/
/data/pos_txt/
/data/pos_xml/
```

### Python Programs

```
/classify_convert.py
/classify_model.py
```

### Lists of Stop Words

```
/stop_danish.txt
/stop_dutch.txt
/stop_english.txt
/stop_finnish.txt
/stop_french.txt
/stop_german.txt
/stop_hungarian.txt
/stop_italian.txt
/stop_norwegian.txt
/stop_portuguese.txt
/stop_spanish.txt
/stop_swedish.txt
/stop_turkish.txt
```
