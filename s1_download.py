#Name:            s1_download.py
#Purpose:         Download PDFs that were discovered during web crawling and whose URLs are found in /project/dump/dump.csv
#Data Layout:     See README.md
#Python Version:  3

import codecs
import csv
import os
import re

#Name:       is_pdf
#Arguments:  url
#            metadata
#Purpose:    Determine whether the URL points to a PDF

def is_pdf(url, metadata):
    urlmatch = re.search(r"^(\S+)\.([pP][dD][fF])$", url)
    metadatamatch = re.search(r"Content-Type:application/pdf", metadata)
    return urlmatch or metadatamatch

#Name:       download_pdf
#Arguments:  url
#Purpose:    Download the PDF

def download_pdf(url):
    os.system("wget --no-check-certificate -nv -P /project/download/ " + url)
    return

def main():
    #Project name
    projname = "project"
    
    #Read in list of URLs and download PDFs
    f = codecs.open("/project/dump/dump.csv", "rU")
    rdr = csv.DictReader(f)
    for row in rdr:
        if is_pdf(row["Url"], row["Metadata"]):
            download_pdf(row["Url"], project)
    f.close()
    
    return

if __name__ == "__main__":
    main()
