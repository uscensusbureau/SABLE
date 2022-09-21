#Name:        m3_txt_to_excel.py
#Purpose:     Convert scraped data in TXT format to Microsoft EXCEL
#Invocation:  python3 m3_txt_to_excel.py <txtFileName> <excelFileName>

import pandas as pd
import sys

def main():
    #Check valid arguments
    if valid_arguments():
        convert_txt_to_excel(sys.argv[1], sys.argv[2])
    else:
        print("\nInvalid arguments\n")
    return

if __name__ == "__main__":
    main()
