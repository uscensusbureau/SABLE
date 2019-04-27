#Name:        s1_download.py
#Purpose:     Download PDFs discovered during web crawling
#Invocation:  python3 s1_download.py <projectName>

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
        if re.search(r"^[a-zA-Z][a-zA-Z_-]*$", sys.argv[1]) != None:
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
#            projectName
#Purpose:    Download the PDF

def download_pdf(url, projectName):
    #Use the Linux/Unix utility wget to download the PDF
    os.system("wget --no-check-certificate -nv -P /" + projectName + "/download/ " + url)
    return

#Name:       download_pdfs
#Arguments:  projectName
#Purpose:    Download PDFs

def download_pdfs(projectName):
    #Read in the list of URLs crawled by Apache Nutch and download the PDFs
    f = codecs.open("/" + projectName + "/dump/dump.csv", "rU")
    rdr = csv.DictReader(f)
    for row in rdr:
        if is_pdf(row["Url"], row["Metadata"]):
            download_pdf(row["Url"], projectName)
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
