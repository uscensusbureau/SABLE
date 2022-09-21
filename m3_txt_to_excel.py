#Name:        m3_txt_to_excel.py
#Purpose:     Convert scraped data product in TXT format to Microsoft EXCEL
#Invocation:  python3 m3_txt_to_excel.py <projName> <yyyy> <mm>

import os
import pandas as pd
import re
import sys

#Name:        valid_arguments
#Purpose:     Check whether the command-line arguments are valid
#Parameters:  sys.argv (globally defined list of command-line arguments)
#Returns:     True (arguments are valid) or False (arguments are invalid)

def valid_arguments():
    yearValid = [str(yyyy) for yyyy in range(2000, 2051)]
    monthValid = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    if len(sys.argv) == 4 and re.search(r"^[a-zA-Z][a-zA-Z_-]*$", sys.argv[1]) and sys.argv[2] in yearValid and sys.argv[3] in monthValid:
        return True
    return False

#Name:        convert_txt_to_excel
#Purpose:     Convert data product in TXT format to Microsoft EXCEL format
#Parameters:  projName (project name)
#             yyyy (4-digit year)
#             mm (2-digit month)
#Returns:     

def convert_txt_to_excel(projName, yyyy, mm):
    prodLoc = "/" + projName + "/prod/" + yyyy + "_" + mm + ".txt"
    excelLoc = "/" + projName + "/excel/" + yyyy + "_" + mm + ".xlsx"
    if os.path.isfile(prodLoc):
        prod = pd.read_csv(prodLoc, sep='|')
        prod.to_csv(excelLoc.replace(".xlsx", ".csv"), index=False)
    else:
        print("\n!!! PROBLEM: " + prodLoc + " does not exist\n")
    return

def main():
    #Check valid arguments
    if valid_arguments():
        convert_txt_to_excel(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("\nInvalid arguments\n")
    return

if __name__ == "__main__":
    main()
