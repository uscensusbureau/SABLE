#Name:            s0_setup.py
#Purpose:         Set up project folders
#Data Layout:     See README.md
#Python Version:  3

import os

def main():
    #Project name
    projname = "project"
    
    projdir = "/" + projname + "/"
    if os.path.isdir(projdir):
        print("\nProject folder " + projdir + " already exists\n")
    else:
        os.system("mkdir " + projdir)
        os.system("mkdir " + projdir + "crawl/")
        os.system("mkdir " + projdir + "download/")
        #The /project/dump/ folder is created by Apache Nutch when its database contents are output to CSV format
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

if __name__ == "__main__":
    main()
