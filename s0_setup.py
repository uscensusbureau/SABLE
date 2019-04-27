#Name:        s0_setup.py
#Purpose:     Set-up project folders
#Invocation:  python3 s0_setup.py <projectName>

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

#Name:       create_folders
#Arguments:  projectName
#Purpose:    Create project folders

def create_folders(projectName):
    projectDir = "/" + projectName + "/"
    if os.path.isdir(projectDir):
        print("\nProject folder " + projectDir + " already exists\n")
    else:
        os.system("mkdir " + projectDir)
        os.system("mkdir " + projectDir + "crawl/")
        os.system("mkdir " + projectDir + "download/")
        #The /projectName/dump/ folder is created by Apache Nutch when its database contents are output to CSV format
        os.system("mkdir " + projectDir + "neg_pdf/")
        os.system("mkdir " + projectDir + "neg_prob/")
        os.system("mkdir " + projectDir + "neg_txt/")
        os.system("mkdir " + projectDir + "neg_xml/")
        os.system("mkdir " + projectDir + "pos_pdf/")
        os.system("mkdir " + projectDir + "pos_prob/")
        os.system("mkdir " + projectDir + "pos_txt/")
        os.system("mkdir " + projectDir + "pos_xml/")
        os.system("mkdir " + projectDir + "pred_pdf/")
        os.system("mkdir " + projectDir + "pred_prob/")
        os.system("mkdir " + projectDir + "pred_txt/")
        os.system("mkdir " + projectDir + "pred_xml/")
        os.system("mkdir " + projectDir + "urls/")
        print("\nProject folder " + projectDir + " and subfolders created\n")
    return

def main():
    if valid_arguments():
        create_folders(sys.argv[1])
    else:
        print("\nInvalid arguments\n")
    return

if __name__ == "__main__":
    main()
