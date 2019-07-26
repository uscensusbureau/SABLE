# SABLE

This readme is a work in progress.

## Introduction

SABLE, which stands for Scraping Assisted by Learning, is a collection of tools for web crawling and web scraping.  Some elements involve supervised machine learning to perform text classification.  The idea is to discover potential new sources of data on the web in PDF format, apply a text classification model to predict whether the PDF contains useful data, and then scrape data using templates, text analysis, and other models.  SABLE was initially developed to scrape data on tax revenue collections from state and local government websites but has been applied to other settings such as finding population and housing statistics on the websites of foreign national statistical agencies.

## Software

SABLE is based on the following open-source software:

* [Linux](https://www.linux.org/)
  * wget command-line utility
  * pdftotext command-line utility
* [Apache Nutch](http://nutch.apache.org/) (version 1.15)
* [Python](http://www.python.org/) (version 3.6)
  * [scikit-learn](http://www.scikit-learn.org/stable/)
  * [NLTK (Natural Language Toolkit)](https://www.nltk.org/)
  * [PDFMiner3K](https://github.com/jaepil/pdfminer3k/)

Apache Nutch is a Java-based web crawler and is used to crawl websites, discover PDFs, and compile a training set of documents for model building.  Python is used to scrape data and text from PDFs and to fit and evaluate text classification models based on various supervised machine learning algorithms such as naive Bayes, logistic regression, and random forests.

## Python Programs

The following tables describe the Python programs in this repository.  More information can be found in the programs themsevles.    There are multiple series of Python programs depending on the task SABLE is to perform.

### S-Series

There is an additional Python program used in SABLE named ```pdf2txt.py```.  It comes with the PDFMiner3K module and is invoked by ```s2_convert.py```.

| Program               | Purpose                                                  |
| --------------------- | -------------------------------------------------------- |
| ```s0_setup.py```     | Set up project folders                                   |
| ```s1_download.py```  | Download PDFs discovered during web crawling             |
| ```s2_convert.py```   | Convert PDFs to TXT format                               |
| ```s3_model.py ```    | Fit and evaluate text classification models              |
| ```s4_logistic.py ``` | Fit a logisitc regression model and apply it to new PDFs |

### M-Series

| Program               | Purpose                                             |
| --------------------- | --------------------------------------------------- |
| ```m0_setup.py```     | Set up project folders                              |
| ```m1_download.py```  | Download documents known to contain useful data     |
| ```m2_scrape.py```    | Apply templates to scrape data from these documents |

## Lists of Stop Words

This repository also contains lists of common "stop" words for multiple languages such as French, German, and Spanish.  These lists come from the NLTK module.  Foreign accent marks have been removed from characters, and some lists have been modified slightly in other ways.

## Examples

An example training set for predicting whether a PDF contains data on tax revenue collections is contained in the folders ```/neg_txt/``` and ```/pos_txt/```.  These TXT files were created by applying the PDF-to-TXT conversion program ```s2_convert.py``` to PDFs discovered on various websites.  The folder ```/pred_txt/``` contains TXT files that represent previously unseen documents that are to be classified by a model.

| Example Folder   | Description                                                                   |
| ---------------- | ----------------------------------------------------------------------------- |
| ```/neg_txt/```  | Collection of TXT files belonging to the "negative" class in the training set |
| ```/pos_txt/```  | Collection of TXT files belonging to the "positive" class in the training set |
| ```/pred_txt/``` | Collection of TXT files that are to be classified by a model                  |

The following files are found in the ```/examples/``` folder.  The PDFs and corresponding TXT files are three examples of the PDF-to-TXT conversion program applied to publications from the U.S. Census Bureau website: [https://www.census.gov](https://www.census.gov).  The file ```example_model_output.txt``` was created by applying the model fitting and evaluation program ```s3_model.py``` to the training set.  The file ```example_pred_output.txt``` was created by applying the logistic regression program ```s4_logistic.py``` to the TXT files in ```/pred_txt/```.  Finally, the file ```example_seed.txt``` contains seed URLs for crawling state government websites in search of PDFs containing tax revenue data.

| Example File                   | Description                                                                       |
| ------------------------------ | --------------------------------------------------------------------------------- |
| ```example_g12-cg-org.pdf```   | 2012 Census of Governments report                                                 |
| ```example_g12-cg-org.txt```   | Output from ```s2_convert.py``` applied to above PDF                              |
| ```example_g16-aspp-sl.pdf```  | 2016 Annual Survey of Public Pensions report                                      |
| ```example_g16-aspp-sl.txt```  | Output from ```s2_convert.py``` applied to above PDF                              |
| ```example_g17-qtax4.pdf```    | 2017q4 Quarterly Summary of State and Local Government Tax Revenue report         |
| ```example_g17-qtax4.txt```    | Output from ```s2_convert.py``` applied to above PDF                              |
| ```example_model_output.txt``` | Output from ```s3_model.py``` applied to training set                             |
| ```example_pred_output.txt```  | Output from ```s4_logistic.py``` applied to training set and TXT files in ```/pred_txt/```  |
| ```example_seed.txt```         | Example seed URLs for crawling state government websites                          |

## Organization of Files

The following organization of files and folders on a Linux/Unix system is assumed.

```
#Python programs
/m0_setup.py
/m1_download.py
/m2_scrape.py
/pdf2txt.py
/s0_setup.py
/s1_download.py
/s2_convert.py
/s3_model.py
/s4_logistic.py

#Lists of stop words
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

#M-series folders
/m_series_project/dat/
/m_series_project/pdf/
/m_series_project/prod/
/m_series_project/txt/

#S-series folders
/s_series_project/crawl/
/s_series_project/download/
/s_series_project/dump/
/s_series_project/neg_pdf/
/s_series_project/neg_prob/
/s_series_project/neg_txt/
/s_series_project/neg_xml/
/s_series_project/pos_pdf/
/s_series_project/pos_prob/
/s_series_project/pos_txt/
/s_series_project/pos_xml/
/s_series_project/pred_pdf/
/s_series_project/pred_prob/
/s_series_project/pred_txt/
/s_series_project/pred_xml/
/s_series_project/urls/
```

## Example S-Series Run

Set up folders for a project called ```my_project```.

```
>> python3 s0_setup.py my_project
```

Create ```seed.txt```, which contains the seed URLs, or starting points, of the web crawl.  Run Apache Nutch and crawl to a specified depth (depth equals three in this example).  Output contents of the Apache Nutch database to CSV format.

```
>> vi /my_project/urls/seed.txt
#Enter seed URLs
>> crawl -s /my_project/urls/ /my_project/crawl/ 3
>> readdb /my_project/crawl/crawldb/ -dump /my_project/dump/ -format csv
>> cat /my_project/dump/part-r-00000 > /my_project/dump/dump.csv
```

Download PDFs discovered during the web crawl to the folder ```/my_project/download/```.  Manually classify the downloaded PDFs as "positive" (contains useful data) or "negative" and place them accordingly in the folders ```/my_project/pos_pdf/``` and ```/my_project/neg_pdf/```.

```
>> python3 s1_download.py my_project
```

Convert the PDFs in the positive class to TXT format.  Convert the PDFs in the negative class to TXT format.

```
>> python3 s2_convert.py my_project english pos
>> python3 s2_convert.py my_project english neg
```

Fit and evaluate various text classification models.

```
>> python3 s3_model.py my_project
```

Obtain new PDFs (for example, through continued web crawling) and place them in the folder ```/my_project/pred_pdf/```.  Convert these PDFs to TXT format.

```
>> python3 s2_convert.py my_project english pred
```

Fit a logistic regression model using the manually classified positive and negative PDFs and use it to predict classes and probabilities for the new PDFs.

```
>> python3 s4_logistic.py my_project
```
