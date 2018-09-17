# SABLE

This readme is a work in progress.

## Introduction

SABLE, which stands for Scraping Assisted by Learning, is a collection of tools for web crawling and web scraping.  Some elements involve supervised machine learning to perform text classification.  The idea is to discover potential new sources of data on the web in PDF format, apply a text classification model to predict whether the PDF contains useful data, and then scrape data using templates, text analysis, and other models.  SABLE was initially developed to scrape data on tax revenue collections from state and local government websites but has been applied to other settings such as finding population and housing statistics on the websites of foreign national statistical agencies.

## Software

SABLE is based on the following pieces of open-source software:

* [Apache Nutch](http://nutch.apache.org/)
* [Python](http://www.python.org/)
  * [scikit-learn](http://www.scikit-learn.org/stable/)
  * [Natural Language Toolkit (NLTK)](https://www.nltk.org/)
  * [PDFMiner3K](https://github.com/jaepil/pdfminer3k/)

Apache Nutch is a Java-based web crawler and is used to crawl websites, discover PDFs, and compile a training set of documents for model building.  Python is used to extract text from PDFs and to fit and evaluate text classification models based on various supervised machine learning algorithms.  These algorithms consist of:

* Naive Bayes
* K-Nearest Neighbors
* Linear Support Vector Classifier
* Logistic Regression
* Decision Tree
* Random Forest

## Description of Contents

This repository contains Python programs, lists of stop words, and example input and output.  PDFs that are to be converted to TXT format and used as input into building classification models should be manually classified as "positive" (contains useful data) or "negative" and placed accordingly in the ```/project/pos_pdf/``` and ```/project/neg_pdf/``` folders.  The extracted text is output to the ```/project/pos_txt/``` and ```/project/neg_txt/``` folders.

### Python Programs

| Program              | Description                                                     |
| -------------------- | --------------------------------------------------------------- |
| ```s0_setup.py```    | Sets up project directories                                     |
| ```s1_download.py``` | Downloads PDFs from an Apache Nutch database dump in CSV format |
| ```s2_convert.py```  | Converts PDFs to TXT format                                     |
| ```s3_model.py ```   | Fits and evaluates text classification models                   |

Additional information can be found in the comments in the Python programs.

### Lists of Stop Words

Lists of NLTK stop words for multiple languages are provided.  Foreign accent marks have been removed from characters, and some lists have been modified slightly in other ways.

### Examples

| Program                        | Description                                          |
| ------------------------------ | ---------------------------------------------------- |
| ```example_g12-cg-org.pdf```   | placeholder text                                     |
| ```example_g12-cg-org.txt```   | placeholder text                                     |
| ```example_g16_aspp-sl.pdf```  | placeholder text                                     |
| ```example_g16-aspp-sl.txt```  | placeholder text                                     |
| ```example_g17-qtax4.pdf```    | placeholder text                                     |
| ```example_g17-qtax4.txt```    | placeholder text                                     |
| ```/neg_txt/```                | placeholder text                                     |
| ```/pos_txt/```                | placeholder text                                     |
| ```example_model_output.txt``` | placeholder text                                     |

## Organization of Files

The following organization of files and folders on a Linux/Unix system is assumed. <br />

### Python Programs

```
/s0_setup.py
/s1_download.py
/s2_convert.py
/s3_model.py
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

### Folders

```
/project/crawl/
/project/download/
/project/dump/
/project/neg_pdf/
/project/neg_prob/
/project/neg_txt/
/project/neg_xml/
/project/pos_pdf/
/project/pos_prob/
/project/pos_txt/
/project/pos_xml/
/project/urls/
```

## Example Run

This section is a work in progress.

```
python3 s0_setup.py
nutch/bin/crawl ./urls ./crawl 3
nutch/bin/readdb ./crawl/crawldb -output dump -format csv
python3 s1_download.py
python3 s2_convert.py
python3 s3_model.py
```
