#Name:        s1_download.py
#Purpose:     Download PDFs discovered during web crawling
#Invocation:  python3 s1_download.py <projName>

import codecs
import csv
import os
import re
import sys

#Name:       valid_arguments
#Arguments:  sys.argv (globally defined list of command-line arguments)
#Purpose:    Check whether the command-line arguments are valid

def valid_arguments():
    valid = False
    if len(sys.argv) == 2:
        if re.search(r"^[a-zA-Z][a-zA-Z_-]*$", sys.argv[1]):
            valid = True
    return valid

#Name:       is_pdf
#Arguments:  url
#            metadata
#Purpose:    Determine whether the URL points to a PDF

def is_pdf(url, metadata):
    urlMatch = re.search(r"^(\S+)\.([pP][dD][fF])$", url)
    metadataMatch = re.search(r"Content-Type:application/pdf", metadata)
    return urlMatch or metadataMatch

#Name:       download_pdf
#Arguments:  url
#            projName (project name)
#Purpose:    Download the PDF

def download_pdf(url, projName):
    #Use the Linux/Unix utility wget to download the PDF
    os.system("wget --no-check-certificate -nv -P /" + projName + "/download/ " + url)
    return

#Name:       download_pdfs
#Arguments:  projName (project name)
#Purpose:    Download PDFs

def download_pdfs(projName):
    #Read in the list of URLs crawled by Apache Nutch and download the PDFs
    f = codecs.open("/" + projName + "/dump/dump.csv", "rU")
    rdr = csv.DictReader(f)
    for row in rdr:
        if is_pdf(row["Url"], row["Metadata"]):
            download_pdf(row["Url"], projName)
    f.close()
    return

def main():
    if valid_arguments():
        download_pdfs(sys.argv[1])
    else:
        print("\nInvalid arguments\n")
    return

if __name__ == "__main__":
    main()
