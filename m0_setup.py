# Name:        m0_setup.py
# Purpose:     Set up project folders
# Invocation:  python3 m0_setup.py <projName>

import os
import re
import sys

# Name:        valid_arguments
# Purpose:     Check whether the command-line arguments are valid
# Parameters:  sys.argv (globally defined list of command-line arguments)
# Returns:     True (all arguments are valid) or False (at least one argument is invalid)

def valid_arguments():
    if len(sys.argv) == 2 and re.search(r"^[a-zA-Z][a-zA-Z_-]*$", sys.argv[1]):
        return True
    return False

# Name:        create_folders
# Purpose:     Create project folders
# Parameters:  projName (project name)
# Returns:     

def create_folders(projName):
    projDir = "./{}".format(projName)
    if os.path.isdir(projDir):
        print("\nProject folder {} already exists\n".format(projDir))
    else:
        os.system("mkdir {}".format(projDir))
        os.system("mkdir {}/dat".format(projDir))
        os.system("mkdir {}/pdf".format(projDir))
        os.system("mkdir {}/prod".format(projDir))
        os.system("mkdir {}/txt".format(projDir))
        print("\nProject folder {} and subfolders created\n".format(projDir))
    return

def main():
    # Check valid arguments
    if valid_arguments():
        create_folders(sys.argv[1])
    else:
        print("\nInvalid arguments\n")
    return

if __name__ == "__main__":
    main()
