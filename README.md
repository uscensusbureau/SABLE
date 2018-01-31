# SABLE

This readme is a work in progress.

## Introduction

SABLE, which stands for Scraping Assisted by Learning, is a collection of tools for web crawling, web scraping, and text classification with the help of machine learning.  The idea is to discover potential new sources of data on the web in PDF format, apply a classification model to predict whether the PDF contains useful data, and then scrape the data.  SABLE was initially developed to scrape data on tax revenue collections from state and local government websites but has been applied to other settings such as finding population and housing statistics on the websites of foreign national statistical agencies.

## Software

SABLE is based on two main pieces of open-source software: Apache Nutch, a Java-based web crawler, and Python.  Nutch is used to crawl websites, discover PDFs, and compile a training set of documents for model building.  Python is used to extract text from PDFs and to fit and evaluate classification models.  For PDFs containing useful data, templates in the form of additional Python programs can be developed to scrape the data.  SABLE uses the following Python modules: scikit-learn, Natural Language Toolkit (NLTK), PDFMiner (Python 2.X version), and PDFMiner3K (a Python 3.X port of PDFMiner).

## Description of Contents

This repository contains Python programs for converting PDFs to TXT format and for fitting and evaluating classification models that predict whether a PDF contains useful data based on the extracted text.  Lists of NLTK stop words for multiple languages are provided.  Foreign accent marks have been removed from characters, and some lists have been modified slightly.

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
```
