#Name:        s0_setup.py
#Purpose:     Set up project folders
#Invocation:  python3 s0_setup.py <projName>

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

#Name:        create_folders
#Purpose:     Create project folders
#Parameters:  projName (project name)
#Returns:     

def create_folders(projName):
    projDir = "/{}/".format(projName)
    if os.path.isdir(projDir):
        print("\nProject folder {} already exists\n".format(projDir))
    else:
        os.system("mkdir {}".format(projDir))
        os.system("mkdir {}crawl/".format(projDir))
        os.system("mkdir {}download/".format(projDir))
        #The folder /projName/dump/ is created by Apache Nutch when its database contents are output to CSV format
        os.system("mkdir {}neg_pdf/".format(projDir))
        os.system("mkdir {}neg_prob/".format(projDir))
        os.system("mkdir {}neg_txt/".format(projDir))
        os.system("mkdir {}neg_xml/".format(projDir))
        os.system("mkdir {}pos_pdf/".format(projDir))
        os.system("mkdir {}pos_prob/".format(projDir))
        os.system("mkdir {}pos_txt/".format(projDir))
        os.system("mkdir {}pos_xml/".format(projDir))
        os.system("mkdir {}pred_pdf/".format(projDir))
        os.system("mkdir {}pred_prob/".format(projDir))
        os.system("mkdir {}pred_txt/".format(projDir))
        os.system("mkdir {}pred_xml/".format(projDir))
        os.system("mkdir {}urls/".format(projDir))
        print("\nProject folder {} and subfolders created\n".format(projDir))
    return

def main():
    if valid_arguments():
        create_folders(sys.argv[1])
    else:
        print("\nInvalid arguments\n")
    return

if __name__ == "__main__":
    main()
