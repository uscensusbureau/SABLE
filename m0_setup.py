#Name:        m0_setup.py
#Purpose:     Set up project folders
#Invocation:  python3 m0_setup.py <projName>

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

#Name:       create_folders
#Arguments:  projName (project name)
#Purpose:    Create project folders

def create_folders(projName):
    projDir = "/" + projName + "/"
    if os.path.isdir(projDir):
        print("\nProject folder " + projDir + " already exists\n")
    else:
        os.system("mkdir " + projDir)
        os.system("mkdir " + projDir + "dat/")
        os.system("mkdir " + projDir + "pdf/")
        os.system("mkdir " + projDir + "prod/")
        os.system("mkdir " + projDir + "txt/")
        print("\nProject folder " + projDir + " and subfolders created\n")
    return

def main():
    if valid_arguments():
        create_folders(sys.argv[1])
    else:
        print("\nInvalid arguments\n")
    return

if __name__ == "__main__":
    main()
