#Name:        s0_setup.py
#Purpose:     Set-up project folders
#Invocation:  python3 s0_setup.py <project name>

import os
import re
import sys

#Name:       valid_arguments
#Arguments:  sys.argv (globally defined list of command-line arguments)
#Purpose:    Checks whether the command-line arguments are valid

def valid_arguments():
    valid = False
    if len(sys.argv) == 2:
        if re.search(r"^[a-zA-Z][a-zA-Z_-]*$", sys.argv[1]) != None:
            valid = True
    return valid

#Name:       create_folders
#Arguments:  projname (project name)
#Purpose:    Creates project folders

def create_folders(projname):
    projdir = "/" + projname + "/"
    if os.path.isdir(projdir):
        print("\nProject folder " + projdir + " already exists\n")
    else:
        os.system("mkdir " + projdir)
        os.system("mkdir " + projdir + "crawl/")
        os.system("mkdir " + projdir + "download/")
        #The /projname/dump/ folder is created by Apache Nutch when its database contents are output to CSV format
        os.system("mkdir " + projdir + "neg_pdf/")
        os.system("mkdir " + projdir + "neg_prob/")
        os.system("mkdir " + projdir + "neg_txt/")
        os.system("mkdir " + projdir + "neg_xml/")
        os.system("mkdir " + projdir + "pos_pdf/")
        os.system("mkdir " + projdir + "pos_prob/")
        os.system("mkdir " + projdir + "pos_txt/")
        os.system("mkdir " + projdir + "pos_xml/")
        os.system("mkdir " + projdir + "urls/")
        print("\nProject folder " + projdir + " and subfolders created\n")
    return

def main():
    if valid_arguments():
        create_folders(sys.argv[1])
    else:
        print("\nInvalid arguments\n")
    return

if __name__ == "__main__":
    main()
