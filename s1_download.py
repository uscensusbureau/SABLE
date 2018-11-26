#Name:        s1_download.py
#Purpose:     Download PDFs discovered during web crawling
#Invocation:  python3 s1_download.py <project name>

import codecs
import csv
import os
import re
import sys

#Name:       are_valid_arguments
#Arguments:  sys.argv (globally defined list of command-line arguments)
#Purpose:    Checks whether the command-line arguments are valid

def are_valid_arguments():
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
    urlmatch = re.search(r"^(\S+)\.([pP][dD][fF])$", url)
    metadatamatch = re.search(r"Content-Type:application/pdf", metadata)
    return urlmatch or metadatamatch

#Name:       download_pdf
#Arguments:  url
#            projname
#Purpose:    Download the PDF

def download_pdf(url, projname):
    #Use the Linux/Unix utility wget to download the PDF
    os.system("wget --no-check-certificate -nv -P /" + projname + "/download/ " + url)
    return

#Name:       download_pdfs
#Arguments:  projname (project name)
#Purpose:    Download PDFs

def download_pdfs(projname):
    #Read in the list of URLs crawled by Apache Nutch and download the PDFs
    f = codecs.open("/" + projname + "/dump/dump.csv", "rU")
    rdr = csv.DictReader(f)
    for row in rdr:
        if is_pdf(row["Url"], row["Metadata"]):
            download_pdf(row["Url"], projname)
    f.close()
    
    return

def main():
    if are_valid_arguments():
        download_pdfs(sys.argv[1])
    else:
        print("\nInvalid arguments\n")
    return

if __name__ == "__main__":
    main()
