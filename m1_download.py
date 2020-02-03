#Name:        m1_download.py
#Purpose:     Download specific tax revenue documents
#Invocation:  python3 m1_download.py <projName> <yyyy> <mm>

import os
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

#Name:        print_state
#Purpose:     Print name of state
#Parameters:  state
#Returns:     

def print_state(state):
    n = len(state)
    print("")
    print("=" * (n + 12))
    print("===   " + state + "   ===")
    print("=" * (n + 12))
    print("")
    return

#Name:        get_targets_XX
#Purpose:     Get PDF names and URLs for state XX
#Parameters:  yyyy (4-digit year)
#             yy (2-digit year)
#             mm (2-digit month)
#             month
#             month3 (3-letter month)
#             month4 (4-letter month)
#Returns:     List of PDF names and list of URLs

#Alabama
def get_targets_AL(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Alaska
def get_targets_AK(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Arizona
def get_targets_AZ(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Arkansas
def get_targets_AR(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#California
def get_targets_CA(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Colorado
def get_targets_CO(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Connecticut
def get_targets_CT(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Delaware
def get_targets_DE(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Florida
def get_targets_FL(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Georgia
def get_targets_GA(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Hawaii
def get_targets_HI(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Idaho
def get_targets_ID(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Illinois
def get_targets_IL(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Indiana
def get_targets_IN(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Iowa
def get_targets_IA(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Kansas
def get_targets_KS(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Kentucky
def get_targets_KY(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Louisiana
def get_targets_LA(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Maine
def get_targets_ME(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Maryland
def get_targets_MD(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Massachusetts
def get_targets_MA(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Michigan
def get_targets_MI(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Minnesota
def get_targets_MN(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Mississippi
def get_targets_MS(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Missouri
def get_targets_MO(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Montana
def get_targets_MT(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Nebraska
def get_targets_NE(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Nevada
def get_targets_NV(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#New Hampshire
def get_targets_NH(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#New Jersey
def get_targets_NJ(yyyy, yy, mm, month, month3, month4):
    fyyy = yyyy
    if mm in ["08", "09", "10", "11", "12"]:
        fyyy = str(int(fyyy) + 1)
    fy = fyyy[2:]

    targetPDFNames = []
    targetURLs = []
    targetPDFName_a = "FY" + fy + "_" + month
    targetPDFNames.append(targetPDFName_a)
    targetURLs.append("https://www.njleg.state.nj.us/legislativepub/budget/" + targetPDFName_a + ".pdf")
    return targetPDFNames, targetURLs

#New Mexico
def get_targets_NM(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#New York
def get_targets_NY(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#North Carolina
def get_targets_NC(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#North Dakota
def get_targets_ND(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Ohio
def get_targets_OH(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Oklahoma
def get_targets_OK(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Oregon
def get_targets_OR(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Pennsylvania
def get_targets_PA(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Rhode Island
def get_targets_RI(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#South Carolina
def get_targets_SC(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#South Dakota
def get_targets_SD(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Tennessee
def get_targets_TN(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Texas
def get_targets_TX(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Utah
def get_targets_UT(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Vermont
def get_targets_VT(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Virginia
def get_targets_VA(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Washington
def get_targets_WA(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#West Virginia
def get_targets_WV(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Wisconsin
def get_targets_WI(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Wyoming
def get_targets_WY(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

#Name:        get_pdf_name_unix
#Purpose:     Account for special character codes in PDF name after the PDF is downloaded to a Linux/Unix environment
#Parameters:  name (name of PDF)
#Returns:     Name of PDF with special character codes replaced with special characters

def get_pdf_name_unix(name):
    nameUnix = re.sub(r"%20", " ", name)
    nameUnix = re.sub(r"%28", "(", nameUnix)
    nameUnix = re.sub(r"%29", ")", nameUnix)
    nameUnix = re.sub(r"%2C", ",", nameUnix)
    return nameUnix

#Name:        download_pdf
#Purpose:     Download the PDF
#Parameters:  projName (project name)
#             state
#             yyyy (4-digit year)
#             mm (2-digit month)
#             targetPDFNames (list of PDF names)
#             targetURLs (list of URLs)
#Returns:     

def download_pdf(projName, state, yyyy, mm, targetPDFNames, targetURLs):
    PDFName = state + "_" + yyyy + "_" + mm
    pdfLoc = "/" + projName + "/pdf/" + PDFName + ".pdf"

    if os.path.isfile(pdfLoc):
        print("PDF already exists.")
    else:
        pdfDownload = False
        for i in range(len(targetURLs)):
            targetPDFName = targetPDFNames[i]
            targetPDFNameUnix = get_pdf_name_unix(targetPDFName)
            targetURL = targetURLs[i]
            if not pdfDownload:
                os.system("wget --no-check-certificate -nv --user-agent=\"SABLE (U.S. Census Bureau research to find alternative data sources and reduce respondent burden) https://github.com/uscensusbureau/sable/\" -P /" + projName + "/pdf/ \"" + targetURL + "\"")
                if os.path.isfile("/" + projName + "/pdf/" + targetPDFNameUnix + ".pdf"):
                    os.system("pdftotext -q -layout \"/" + projName + "/pdf/" + targetPDFNameUnix + ".pdf\" /" + projName + "/pdf/test.txt")
                    if not os.path.isfile("/" + projName + "/pdf/test.txt"):
                        os.system("rm \"/" + projName + "/pdf/" + targetPDFNameUnix + ".pdf\"")
                    elif os.stat("/" + projName + "/pdf/test.txt").st_size == 0:
                        os.system("rm \"/" + projName + "/pdf/" + targetPDFNameUnix + ".pdf\"")
                        os.system("rm /" + projName + "/pdf/test.txt")
                    else:
                        os.system("rm /" + projName + "/pdf/test.txt")
                        os.system("mv \"/" + projName + "/pdf/" + targetPDFNameUnix + ".pdf\" " + pdfLoc)
                        pdfDownload = True
                        print("PDF downloaded.")
        if not pdfDownload:
            print("No PDF downloaded.")
    return

#Name:        download_pdfs
#Purpose:     Download PDFs
#Parameters:  projName (project name)
#             yyyy (4-digit year)
#             mm (2-digit month)
#Returns:     

def download_pdfs(projName, yyyy, mm):
    #Create year and month values
    yy = yyyy[2:]
    month = ""
    month3 = ""
    month4 = ""
    if mm == "01":
        month = "January"
        month3 = "Jan"
        month4 = "Jan"
    elif mm == "02":
        month = "February"
        month3 = "Feb"
        month4 = "Feb"
    elif mm == "03":
        month = "March"
        month3 = "Mar"
        month4 = "Mar"
    elif mm == "04":
        month = "April"
        month3 = "Apr"
        month4 = "Apr"
    elif mm == "05":
        month = "May"
        month3 = "May"
        month4 = "May"
    elif mm == "06":
        month = "June"
        month3 = "Jun"
        month4 = "June"
    elif mm == "07":
        month = "July"
        month3 = "Jul"
        month4 = "July"
    elif mm == "08":
        month = "August"
        month3 = "Aug"
        month4 = "Aug"
    elif mm == "09":
        month = "September"
        month3 = "Sep"
        month4 = "Sept"
    elif mm == "10":
        month = "October"
        month3 = "Oct"
        month4 = "Oct"
    elif mm == "11":
        month = "November"
        month3 = "Nov"
        month4 = "Nov"
    elif mm == "12":
        month = "December"
        month3 = "Dec"
        month4 = "Dec"

    #List of states to loop through
    states = ["NJ"]
    statesDict = {"AL":"Alabama", "AK":"Alaska", "AZ":"Arizona", "AR":"Arkansas", "CA":"California",
        "CO":"Colorado", "CT":"Connecticut", "DE":"Delaware", "FL":"Florida", "GA":"Georgia",
        "HI":"Hawaii", "ID":"Idaho", "IL":"Illinois", "IN":"Indiana", "IA":"Iowa",
        "KS":"Kansas", "KY":"Kentucky", "LA":"Louisiana", "ME":"Maine", "MD":"Maryland",
        "MA":"Massachusetts", "MI":"Michigan", "MN":"Minnesota", "MS":"Mississippi", "MO":"Missouri",
        "MT":"Montana", "NE":"Nebraska", "NV":"Nevada", "NH":"New Hampshire", "NJ":"New Jersey",
        "NM":"New Mexico", "NY":"New York", "NC":"North Carolina", "ND":"North Dakota", "OH":"Ohio",
        "OK":"Oklahoma", "OR":"Oregon", "PA":"Pennsylvania", "RI":"Rhode Island", "SC":"South Carolina",
        "SD":"South Dakota", "TN":"Tennessee", "TX":"Texas", "UT":"Utah", "VT":"Vermont",
        "VA":"Virginia", "WA":"Washington", "WV":"West Virginia", "WI":"Wisconsin", "WY":"Wyoming"}

    for state in states:
        print_state(statesDict[state])
        targetPDFNames = []
        targetURLs = []
        if state == "AL":
            targetPDFNames, targetURLs = get_targets_AL(yyyy, yy, mm, month, month3, month4)
        elif state == "AK":
            targetPDFNames, targetURLs = get_targets_AK(yyyy, yy, mm, month, month3, month4)
        elif state == "AZ":
            targetPDFNames, targetURLs = get_targets_AZ(yyyy, yy, mm, month, month3, month4)
        elif state == "AR":
            targetPDFNames, targetURLs = get_targets_AR(yyyy, yy, mm, month, month3, month4)
        elif state == "CA":
            targetPDFNames, targetURLs = get_targets_CA(yyyy, yy, mm, month, month3, month4)
        elif state == "CO":
            targetPDFNames, targetURLs = get_targets_CO(yyyy, yy, mm, month, month3, month4)
        elif state == "CT":
            targetPDFNames, targetURLs = get_targets_CT(yyyy, yy, mm, month, month3, month4)
        elif state == "DE":
            targetPDFNames, targetURLs = get_targets_DE(yyyy, yy, mm, month, month3, month4)
        elif state == "FL":
            targetPDFNames, targetURLs = get_targets_FL(yyyy, yy, mm, month, month3, month4)
        elif state == "GA":
            targetPDFNames, targetURLs = get_targets_GA(yyyy, yy, mm, month, month3, month4)
        elif state == "HI":
            targetPDFNames, targetURLs = get_targets_HI(yyyy, yy, mm, month, month3, month4)
        elif state == "ID":
            targetPDFNames, targetURLs = get_targets_ID(yyyy, yy, mm, month, month3, month4)
        elif state == "IL":
            targetPDFNames, targetURLs = get_targets_IL(yyyy, yy, mm, month, month3, month4)
        elif state == "IN":
            targetPDFNames, targetURLs = get_targets_IN(yyyy, yy, mm, month, month3, month4)
        elif state == "IA":
            targetPDFNames, targetURLs = get_targets_IA(yyyy, yy, mm, month, month3, month4)
        elif state == "KS":
            targetPDFNames, targetURLs = get_targets_KS(yyyy, yy, mm, month, month3, month4)
        elif state == "KY":
            targetPDFNames, targetURLs = get_targets_KY(yyyy, yy, mm, month, month3, month4)
        elif state == "LA":
            targetPDFNames, targetURLs = get_targets_LA(yyyy, yy, mm, month, month3, month4)
        elif state == "ME":
            targetPDFNames, targetURLs = get_targets_ME(yyyy, yy, mm, month, month3, month4)
        elif state == "MD":
            targetPDFNames, targetURLs = get_targets_MD(yyyy, yy, mm, month, month3, month4)
        elif state == "MA":
            targetPDFNames, targetURLs = get_targets_MA(yyyy, yy, mm, month, month3, month4)
        elif state == "MI":
            targetPDFNames, targetURLs = get_targets_MI(yyyy, yy, mm, month, month3, month4)
        elif state == "MN":
            targetPDFNames, targetURLs = get_targets_MN(yyyy, yy, mm, month, month3, month4)
        elif state == "MS":
            targetPDFNames, targetURLs = get_targets_MS(yyyy, yy, mm, month, month3, month4)
        elif state == "MO":
            targetPDFNames, targetURLs = get_targets_MO(yyyy, yy, mm, month, month3, month4)
        elif state == "MT":
            targetPDFNames, targetURLs = get_targets_MT(yyyy, yy, mm, month, month3, month4)
        elif state == "NE":
            targetPDFNames, targetURLs = get_targets_NE(yyyy, yy, mm, month, month3, month4)
        elif state == "NV":
            targetPDFNames, targetURLs = get_targets_NV(yyyy, yy, mm, month, month3, month4)
        elif state == "NH":
            targetPDFNames, targetURLs = get_targets_NH(yyyy, yy, mm, month, month3, month4)
        elif state == "NJ":
            targetPDFNames, targetURLs = get_targets_NJ(yyyy, yy, mm, month, month3, month4)
        elif state == "NM":
            targetPDFNames, targetURLs = get_targets_NM(yyyy, yy, mm, month, month3, month4)
        elif state == "NY":
            targetPDFNames, targetURLs = get_targets_NY(yyyy, yy, mm, month, month3, month4)
        elif state == "NC":
            targetPDFNames, targetURLs = get_targets_NC(yyyy, yy, mm, month, month3, month4)
        elif state == "ND":
            targetPDFNames, targetURLs = get_targets_ND(yyyy, yy, mm, month, month3, month4)
        elif state == "OH":
            targetPDFNames, targetURLs = get_targets_OH(yyyy, yy, mm, month, month3, month4)
        elif state == "OK":
            targetPDFNames, targetURLs = get_targets_OK(yyyy, yy, mm, month, month3, month4)
        elif state == "OR":
            targetPDFNames, targetURLs = get_targets_OR(yyyy, yy, mm, month, month3, month4)
        elif state == "PA":
            targetPDFNames, targetURLs = get_targets_PA(yyyy, yy, mm, month, month3, month4)
        elif state == "RI":
            targetPDFNames, targetURLs = get_targets_RI(yyyy, yy, mm, month, month3, month4)
        elif state == "SC":
            targetPDFNames, targetURLs = get_targets_SC(yyyy, yy, mm, month, month3, month4)
        elif state == "SD":
            targetPDFNames, targetURLs = get_targets_SD(yyyy, yy, mm, month, month3, month4)
        elif state == "TN":
            targetPDFNames, targetURLs = get_targets_TN(yyyy, yy, mm, month, month3, month4)
        elif state == "TX":
            targetPDFNames, targetURLs = get_targets_TX(yyyy, yy, mm, month, month3, month4)
        elif state == "UT":
            targetPDFNames, targetURLs = get_targets_UT(yyyy, yy, mm, month, month3, month4)
        elif state == "VT":
            targetPDFNames, targetURLs = get_targets_VT(yyyy, yy, mm, month, month3, month4)
        elif state == "VA":
            targetPDFNames, targetURLs = get_targets_VA(yyyy, yy, mm, month, month3, month4)
        elif state == "WA":
            targetPDFNames, targetURLs = get_targets_WA(yyyy, yy, mm, month, month3, month4)
        elif state == "WV":
            targetPDFNames, targetURLs = get_targets_WV(yyyy, yy, mm, month, month3, month4)
        elif state == "WI":
            targetPDFNames, targetURLs = get_targets_WI(yyyy, yy, mm, month, month3, month4)
        elif state == "WY":
            targetPDFNames, targetURLs = get_targets_WY(yyyy, yy, mm, month, month3, month4)
        download_pdf(projName, state, yyyy, mm, targetPDFNames, targetURLs)

    print("")
    return

def main():
    #Check valid arguments
    if valid_arguments():
        download_pdfs(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("\nInvalid arguments\n")
    return

if __name__ == "__main__":
    main()
