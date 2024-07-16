#Name:        s1_download.py
#Purpose:     Download PDFs discovered during web crawling
#Invocation:  python3 s1_download.py <projName>

import codecs
import csv
import os
import re
import sys

#Name:        valid_arguments
#Purpose:     Check whether the command-line arguments are valid
#Parameters:  sys.argv (globally defined list of command-line arguments)
#Returns:     True (all arguments are valid) or False (at least one argument is invalid)

def valid_arguments():
    if len(sys.argv) == 2 and re.search(r"^[a-zA-Z][a-zA-Z_-]*$", sys.argv[1]):
        return True
    return False

#Name:        is_pdf
#Purpose:     Determine whether the URL points to a PDF
#Parameters:  url
#             metadata
#Returns:     Regular expression match object

def is_pdf(url, metadata):
    urlMatch = re.search(r"^(\S+)\.([pP][dD][fF])$", url)
    metadataMatch = re.search(r"Content-Type:application/pdf", metadata)
    return urlMatch or metadataMatch

#Name:        download_pdf
#Purpose:     Download the PDF
#Parameters:  url
#             projName (project name)
#Returns:     

def download_pdf(url, projName):
    #Use the Linux/Unix utility wget to download the PDF
    os.system("wget --no-check-certificate -nv --user-agent=\"SABLE (U.S. Census Bureau research to find alternative data sources and reduce respondent burden) https://github.com/uscensusbureau/sable/; census-aidcrb-support-team@census.gov; For more information, go to www.census.gov/scraping/\" -P /{}/download/ {}".format(projName, url))
    return

#Name:        download_pdfs
#Purpose:     Download PDFs
#Parameters:  projName (project name)
#Returns:     

def download_pdfs(projName):
    #Read in the list of URLs crawled by Apache Nutch and download the PDFs
    f = codecs.open("/{}/dump/dump.csv".format(projName), "r")
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
