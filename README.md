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

This repository contains Python programs, lists of stop words, and example input and output.

### Python Programs

The following table describes the purpose of each of the four Python programs in this repository.  Additional information can be found in the programs themsevles.  A fifth Python program named ```pdf2txt.py``` comes with the PDFMiner3K module and is called by ```s2_convert.py```.

| Program              | Purpose                                      |
| -------------------- | -------------------------------------------- |
| ```s0_setup.py```    | Set up project folders                       |
| ```s1_download.py``` | Download PDFs discovered during web crawling |
| ```s2_convert.py```  | Convert PDFs to TXT format                   |
| ```s3_model.py ```   | Fit and evaluate text classification models  |

### Lists of Stop Words

Lists of NLTK stop words for multiple languages are provided.  Foreign accent marks have been removed from characters, and some lists have been modified slightly in other ways.

### Examples

Three examples of the PDF-to-TXT conversion program, ```s2_convert.py```, are provided.  Also, an example training set for predicting whether a PDF contains data on tax revenue collections is contained in the ```/neg_txt/``` and ```/pos_txt/``` folders.  These TXT files were created by applying the ```s2_convert.py``` program to PDFs discovered on various websites.  The associated ```example_model_output.txt``` file was created by applying the model fitting and evaluation program, ```s3_model.py```, to this training set.

| Example                        | Description                                                                       |
| ------------------------------ | --------------------------------------------------------------------------------- |
| ```example_g12-cg-org.pdf```   | 2012 Census of Governments report                                                 |
| ```example_g12-cg-org.txt```   | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Output after applying ```s2_convert.py```           |
| ```example_g16_aspp-sl.pdf```  | 2016 Annual Survey of Public Pensions report                                      |
| ```example_g16-aspp-sl.txt```  | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Output after applying ```s2_convert.py```           |
| ```example_g17-qtax4.pdf```    | 2017 Quarter 4 Quarterly Summary of State and Local Government Tax Revenue report |
| ```example_g17-qtax4.txt```    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Output after applying ```s2_convert.py```           |
| ```/neg_txt/```                | Folder containing TXT files belonging to the "negative" class in the training set |
| ```/pos_txt/```                | Folder containing TXT files belonging to the "positive" class in the training set |
| ```example_model_output.txt``` | Model output after applying ```s3_model.py``` to the training set                 |

## Organization of Files

The following organization of files and folders on a Linux/Unix system is assumed.

### Python Programs

```
/pdf2txt.py
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

Set up project folders.

```
python3 s0_setup.py
```

Create ```seed.txt```, which contains the seed URLs, or starting points, of the web crawl.  Run Apache Nutch and crawl to a specified depth (depth equals three in this example).  Output contents of the Apache Nutch database to CSV format.

```
vi /project/urls/seed.txt
#Enter seed URLs
crawl /project/urls/ /project/crawl/ 3
readdb /project/crawl/crawldb/ -dump /project/dump/ -format csv
cat /project/dump/part-00000 > /project/dump/dump.csv
```

Download PDFs discovered during the web crawl to the ```/project/download/``` folder.  Manually classify the downloaded PDFs as "positive" (contains useful data) or "negative" and place them accordingly in the ```/project/pos_pdf/``` and ```/project/neg_pdf/``` folders.

```
python3 s1_download.py
```

Convert the PDFs in the positive class to TXT format.  Convert the PDFs in the negative class to TXT format.

```
vi s2_convert.py
#Change the value of the variable clss
python3 s2_convert.py
vi s2_convert.py
#Change the value of the variable clss
python3 s2_convert.py
```

Fit and evaluate text classification models.

```
python3 s3_model.py
```
