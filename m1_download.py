# Name:        m1_download.py
# Purpose:     Download specific tax revenue documents
# Invocation:  python3 m1_download.py <projName> <yyyy> <mm>

import os
import re
import sys
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import Request, urlopen

SABLE_USER_AGENT = "SABLE (U.S. Census Bureau research to find alternative data sources and reduce respondent burden) https://github.com/uscensusbureau/sable/; census-aidcrb-support-team@census.gov; For more information, go to www.census.gov/scraping/"

# Name:        valid_arguments
# Purpose:     Check whether the command-line arguments are valid
# Parameters:  sys.argv (globally defined list of command-line arguments)
# Returns:     True (all arguments are valid) or False (at least one argument is invalid)

def valid_arguments():
    yearsValid = [str(yyyy) for yyyy in range(2000, 2051)]
    monthsValid = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    if len(sys.argv) == 4 and re.search(r"^[a-zA-Z][a-zA-Z_-]*$", sys.argv[1]) and sys.argv[2] in yearsValid and sys.argv[3] in monthsValid:
        return True
    return False

# Name:        print_section_name
# Purpose:     Print name of section
# Parameters:  sectionName (section name)
# Returns:     

def print_section_name(sectionName):
    n = len(sectionName)
    print("")
    print("=" * (n + 12))
    print("===   {}   ===".format(sectionName))
    print("=" * (n + 12))
    print("")
    return

# Name:        get_targets_XX
# Purpose:     Get PDF names and URLs for state XX
# Parameters:  yyyy (4-digit year)
#              yy (2-digit year)
#              mm (2-digit month)
#              month
#              month3 (3-letter month)
#              month4 (4-letter month)
# Returns:     List of PDF names and list of URLs

# Alabama (AL)
def get_targets_AL(yyyy, yy, mm, month, month3, month4): 
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Alaska (AK)
def get_targets_AK(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Arizona (AZ)
def get_targets_AZ(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Arkansas (AR)
def get_targets_AR(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# California (CA)
def get_targets_CA(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []

    if mm in ["07", "08", "09", "10", "11", "12"]:
        fy1 = str(yyyy)
        fy2 = str(int(yyyy) + 1)
    else:
        fy1 = str(int(yyyy) - 1)
        fy2 = str(yyyy)

    print("Using default URL.")

    url = "https://www.sco.ca.gov/ard_state_cash.html"
    req = Request(url, headers={"User-Agent": SABLE_USER_AGENT})
    page = urlopen(req).read()
    html = page.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")
    for l in links:
        if re.search("{}.??{}".format(fy1, fy2), str(l)):
            print("Updating URL.")
            url = "https://www.sco.ca.gov{}".format(l.get("href"))
            break

    req = Request(url, headers={"User-Agent": SABLE_USER_AGENT})
    page = urlopen(req).read()
    html = page.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")
    for l in links:
        if re.search("{}.??{}".format(month, yyyy), str(l)):
            print("Link found.")
            target_link = "https://www.sco.ca.gov{}".format(l.get("href"))
            target_name = target_link[target_link.rfind("/")+1:]
            targetURLs.append(target_link)
            targetPDFNames.append(target_name)
            break
    else:
        print("Link NOT found.")
    
    return targetPDFNames, targetURLs

# Colorado (CO)
def get_targets_CO(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Connecticut (CT)
def get_targets_CT(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []

    url = "http://portal.ct.gov/DRS/DRS-Reports/Comparative-Statement-Reports/{}---{}-Monthly-Comparative-Statements".format(yyyy, int(yyyy)-1) 
    req = Request(url, headers={"User-Agent": SABLE_USER_AGENT})
    page = urlopen(req).read()
    html = page.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find("div", {"class": "content"})
    links = div.find_all("a")
    for l in links:
        if re.search(month3, str(l), re.I) and re.search(yyyy, str(l), re.I):
            print("Link found.")
            target_link = l.get("href")
            if not re.search("ct\.gov", target_link, re.I):
                target_link = "https://portal.ct.gov{}".format(target_link)
            # There could be text after ".pdf" in target_link (e.g., "?rev=865...")
            target_link = target_link[:target_link.rfind(".pdf")+4]
            target_name = target_link[target_link.rfind("/")+1:-4]
            targetPDFNames.append(target_name)
            targetURLs.append(target_link)
            break
    else:
        print("Link NOT found.")
     
    return targetPDFNames, targetURLs

# Delaware (DE)
def get_targets_DE(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# District of Columbia (DC)
def get_targets_DE(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Florida (FL)
def get_targets_FL(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Georgia (GA)
def get_targets_GA(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Hawaii (HI)
def get_targets_HI(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Idaho (ID)
def get_targets_ID(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Illinois (IL)
def get_targets_IL(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Indiana (IN)
def get_targets_IN(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Iowa (IA)
def get_targets_IA(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Kansas (KS)
def get_targets_KS(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Kentucky (KY)
def get_targets_KY(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Louisiana (LA)
def get_targets_LA(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Maine (ME)
def get_targets_ME(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Maryland (MD)
def get_targets_MD(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Massachusetts (MA)
def get_targets_MA(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Michigan (MI)
def get_targets_MI(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Minnesota (MN)
def get_targets_MN(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Mississippi (MS)
def get_targets_MS(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Missouri (MO)
def get_targets_MO(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Montana (MT)
def get_targets_MT(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Nebraska (NE)
def get_targets_NE(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Nevada (NV)
def get_targets_NV(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# New Hampshire (NH)
def get_targets_NH(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# New Jersey (NJ)
def get_targets_NJ(yyyy, yy, mm, month, month3, month4):
    fyyy = yyyy
    if mm in ["07", "08", "09", "10", "11", "12"]:
        fyyy = str(int(fyyy) + 1)
    fy = fyyy[2:]

    nyyy = yyyy
    if mm == "12":
        nyyy = str(int(yyyy) + 1)

    # Nested/inner function
    def NJ_repeat(url):
        targetPDFNames = []
        targetURLs = []

        req = Request(url, headers={"User-Agent": SABLE_USER_AGENT})
        page = urlopen(req).read()
        html = page.decode("utf-8")
        soup = BeautifulSoup(html, "html.parser", parse_only=SoupStrainer("td"))
        cells = soup.find_all("td")
        link = ""
        for cell in cells:
            if re.search(month, str(cell), re.I) and re.search("treasury", str(cell), re.I) and re.search("major\s*(taxes|revenue)", str(cell), re.I) and re.search("{}|{}".format(nyyy, yyyy), str(cell), re.I):
                print("Press release found.")
                link = cell.find("a").get("href")
                if not re.search("https", link, re.I):
                    link = "https://www.nj.gov/treasury/{}".format(link)
                break

        if link == "":
            print("Press release NOT found.")
            return targetPDFNames, targetURLs

        req = Request(link, headers={"User-Agent": SABLE_USER_AGENT})
        page = urlopen(req).read()
        html = page.decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        links = soup.find_all("a")
        for l in links:
            if re.search("FY{}.??{}".format(fy, month), str(l), re.I) or re.search("{}.??{}".format(month, yyyy), str(l), re.I):
                if (re.search("monthly", str(l), re.I) and re.search("report", str(l), re.I) and re.search("snapshot", str(l), re.I)) or (re.search("revenue.??report", str(l), re.I)):
                    link = l.get("href")
                    link = link[link.rfind("pdf/"):]
                    target_name = link[link.rfind("/")+1:]
                    target_link_a = "https://www.nj.gov/treasury/news/{}/{}".format(nyyy, link)
                    target_link_b = "https://www.nj.gov/treasury/{}".format(link)
                    r = requests.get(target_link_a)
                    if r.status_code != 404:
                        print("Link found.")
                        targetPDFNames.append(target_name)
                        targetURLs.append(target_link_a)
                    r = requests.get(target_link_b)
                    if r.status_code != 404:
                        print("Link found.")
                        targetPDFNames.append(target_name)
                        targetURLs.append(target_link_b)
                    break

        if len(targetPDFNames) == 0 and len(targetURLs) == 0:
            ps = soup.find_all("p")
            for p in ps:
                if re.search("treasury", str(p), re.I) and re.search("{}".format(month), str(p), re.I) and re.search("revenue", str(p), re.I):
                    # Iterate through the same links as above
                    for l in links:
                        if re.search("attached chart", str(l), re.I):
                            link = l.get("href")
                            link = link[link.rfind("pdf/"):]
                            target_name = link[link.rfind("/")+1:]
                            target_link_a = "https://www.nj.gov/treasury/news/{}/{}".format(nyyy, link)
                            target_link_b = "https://www.nj.gov/treasury/{}".format(link)
                            r = requests.get(target_link_a)
                            if r.status_code != 404:
                                print("Link found.")
                                targetPDFNames.append(target_name)
                                targetURLs.append(target_link_a)
                            r = requests.get(target_link_b)
                            if r.status_code != 404:
                                print("Link found.")
                                targetPDFNames.append(target_name)
                                targetURLs.append(target_link_b)
                            break
                    else:
                        continue
                    break
            else:
                print("Link NOT found.")

        return targetPDFNames, targetURLs
    # End of nested/inner function

    # First attempt: recent press releases page
    print("Trying recent press releases page.")
    url = "https://www.nj.gov/treasury/news.shtml"
    targetPDFNames, targetURLs = NJ_repeat(url)

    # Second attempt: archived press releases page
    if len(targetPDFNames) == 0 and len(targetURLs) == 0:
        print("Trying archived press releases page.")
        url = "https://www.nj.gov/treasury/newsarchive.shtml"
        targetPDFNames, targetURLs = NJ_repeat(url)
    
    return targetPDFNames, targetURLs

# New Mexico (NM)
def get_targets_NM(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# New York (NY)
def get_targets_NY(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# North Carolina (NC)
def get_targets_NC(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# North Dakota (ND)
def get_targets_ND(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Ohio (OH)
def get_targets_OH(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Oklahoma (OK)
def get_targets_OK(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Oregon (OR)
def get_targets_OR(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Pennsylvania (PA)
def get_targets_PA(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []

    url = "https://www.pa.gov/en/agencies/revenue/resources/reports-and-statistics/monthly-revenue-reports.html"
    req = Request(url, headers={"User-Agent": SABLE_USER_AGENT})
    page = urlopen(req).read()
    html = page.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")

    # Enter remaining code here

    return targetPDFNames, targetURLs

# Puerto Rico (PR)
def get_targets_PA(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Rhode Island (RI)
def get_targets_RI(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# South Carolina (SC)
def get_targets_SC(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# South Dakota (SD)
def get_targets_SD(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Tennessee (TN)
def get_targets_TN(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Texas (TX)
def get_targets_TX(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Utah (UT)
def get_targets_UT(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Vermont (VT)
def get_targets_VT(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Virginia (VA)
def get_targets_VA(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Washington (WA)
def get_targets_WA(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# West Virginia (WV)
def get_targets_WV(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Wisconsin (WI)
def get_targets_WI(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Wyoming (WY)
def get_targets_WY(yyyy, yy, mm, month, month3, month4):
    targetPDFNames = []
    targetURLs = []
    return targetPDFNames, targetURLs

# Name:        get_filename_unix
# Purpose:     Account for special character codes in filename after the file is downloaded to a Linux/Unix environment
# Parameters:  name (name of file)
# Returns:     Name of file with special character codes replaced with special characters

def get_filename_unix(name):
    nameUnix = re.sub(r"%20", " ", name)
    nameUnix = re.sub(r"%28", "(", nameUnix)
    nameUnix = re.sub(r"%29", ")", nameUnix)
    nameUnix = re.sub(r"%2C", ",", nameUnix)
    return nameUnix

# Name:        download_pdf
# Purpose:     Download the PDF
# Parameters:  projName (project name)
#              state (2-letter state abbreviation)
#              yyyy (4-digit year)
#              mm (2-digit month)
#              targetPDFNames (list of PDF names)
#              targetURLs (list of URLs)
# Returns:     status (string indicating PDF download status)

def download_pdf(projName, state, yyyy, mm, targetPDFNames, targetURLs):
    PDFName = "{}_{}_{}".format(state, yyyy, mm)
    pdfLoc = "./{}/pdf/{}.pdf".format(projName, PDFName)
    pdfDownloaded = False

    # If the PDF already exists
    if os.path.isfile(pdfLoc):
        print("PDF already exists.")
    else:
        # Iterate through the target URLs
        for i in range(len(targetURLs)):
            targetPDFName = targetPDFNames[i]
            targetPDFNameUnix = get_filename_unix(targetPDFName)
            targetURL = targetURLs[i]
            # If the PDF is not downloaded
            if not pdfDownloaded:
                # Try using wget to download PDF
                os.system("wget --no-check-certificate -nv --user-agent=\"{}\" -P ./{}/pdf \"{}\"".format(SABLE_USER_AGENT, projName, targetURL))
                # If the PDF exists
                if os.path.isfile("./{}/pdf/{}.pdf".format(projName, targetPDFNameUnix)):
                    # Try converting the PDF to TXT format
                    os.system("pdftotext -q -layout \"./{}/pdf/{}.pdf\" ./{}/pdf/test.txt".format(projName, targetPDFNameUnix, projName))
                    # If the converted TXT file does not exist
                    if not os.path.isfile("./{}/pdf/test.txt".format(projName)):
                        os.system("rm \"./{}/pdf/{}.pdf\"".format(projName, targetPDFNameUnix))
                    # If the converted TXT file has size 0
                    elif os.stat("./{}/pdf/test.txt".format(projName)).st_size == 0:
                        os.system("rm \"./{}/pdf/{}.pdf\"".format(projName, targetPDFNameUnix))
                        os.system("rm ./{}/pdf/test.txt".format(projName))
                    # PDF is downloaded and can be converted to TXT format
                    else:
                        os.system("rm ./{}/pdf/test.txt".format(projName))
                        os.system("mv \"./{}/pdf/{}.pdf\" {}".format(projName, targetPDFNameUnix, pdfLoc))
                        # Set pdfDownloaded to True
                        pdfDownloaded = True
                        print("PDF downloaded.")
                        return "dlyes"
        if not pdfDownloaded:
            print("No PDF downloaded.")
            return "dlno"
    return "exist"

# Name:        download_pdfs
# Purpose:     Download PDFs
# Parameters:  projName (project name)
#              yyyy (4-digit year)
#              mm (2-digit month)
# Returns:     

def download_pdfs(projName, yyyy, mm):
    # Create year and month values
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

    # Dictionary of state abbreviations (includes District of Columbia and Puerto Rico)
    statesDict = {"AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California",
        "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "DC": "District of Columbia", "FL": "Florida",
        "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa",
        "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts",
        "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri", "MT": "Montana", "NE": "Nebraska",
        "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
        "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon",
        "PA": "Pennsylvania", "PR": "Puerto Rico", "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota",
        "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia", "WA": "Washington",
        "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming"}

    # List of states to loop through
    states = ["CA", "CT", "NJ"]

    # Empty list of statuses
    statuses = []
    
    for state in states:
        print_section_name(statesDict[state])
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
        elif state == "DC":
            targetPDFNames, targetURLs = get_targets_DC(yyyy, yy, mm, month, month3, month4)
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
        elif state == "PR":
            targetPDFNames, targetURLs = get_targets_PR(yyyy, yy, mm, month, month3, month4)
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
        statuses.append(download_pdf(projName, state, yyyy, mm, targetPDFNames, targetURLs))

    print_section_name("Summary")
    print("Number of PDFs that already exist:     {}".format(len([status for status in statuses if status == "exist"])))
    print("Number of successful PDF downloads:    {}".format(len([status for status in statuses if status == "dlyes"])))
    print("Number of unsuccessful PDF downloads:  {}".format(len([status for status in statuses if status == "dlno"])))
    print("")
    return

def main():
    # Check valid arguments
    if valid_arguments():
        download_pdfs(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("\nInvalid arguments\n")
    return

if __name__ == "__main__":
    main()
