# Name:        m2_scrape.py
# Purpose:     Scrape specific tax revenue values from downloaded PDFs
# Invocation:  python3 m2_scrape.py <projName> <yyyy> <mm>

import codecs
import os
import re
import sys

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

# Name:        convert_pdf_to_txt
# Purpose:     Convert PDF to TXT format using the pdftotext utility
# Parameters:  pdfLoc (path of PDF)
#              txtLoc (path of TXT file)
# Returns:     

def convert_pdf_to_txt(pdfLoc, txtLoc):
    os.system("pdftotext -layout {} {}".format(pdfLoc, txtLoc))
    if os.path.isfile(txtLoc) and os.stat(txtLoc).st_size == 0:
        os.system("rm {}".format(txtLoc))
    return

# Name:        clean_text
# Purpose:     Remove whitespace and convert some characters to spaces
# Parameters:  line (line of text)
# Returns:     Cleaned line of text

def clean_text(line):
    l = line.lower()
    l = re.sub(r"[\f\n\r\t\v]+", "", l)
    l = re.sub(r"\xa0", " ", l)
    l = re.sub(u"\u2014", "-", l)
    l = re.sub(r"[^ a-z0-9,.!?:;$%&<>()[]{}/_=+-]+", " ", l)
    return l

# Name:        get_text
# Purpose:     Read in TXT file
# Parameters:  txtLoc (path of TXT file)
# Returns:     List of cleaned lines of text

def get_text(txtLoc):
    f = codecs.open(txtLoc, "r", encoding="utf8")
    lines_clean = [clean_text(line) for line in f.readlines()]
    f.close()
    return lines_clean

# Name:        clean_value
# Purpose:     Standardize negative tax value
# Parameters:  value (tax value)
# Returns:     Cleaned tax value

def clean_value(value):
    value_temp = re.sub(r"\$", "", value)
    value_temp = re.sub(r"\*", "-", value_temp)
    n = len(value_temp)
    if value_temp[0] == "(" and value_temp[n-1] == ")":
        value_new = "-{}".format(value_temp[1:n-1])
    elif value_temp == "-" or value_temp == "--" or value_temp == "---":
        value_new = "0"
    else:
        value_new = value_temp
    return value_new

# Name:        scrape_data_XX
# Purpose:     Apply a template and scrape data from the PDF for state XX
# Parameters:  lines_clean (clean lines of text)
#              state (2-letter state abbreviation)
#              yyyy (4-digit year)
#              mm (2-digit month)
# Returns:     List of lists (one for each line item) containing scraped data

# Alabama (AL)
def scrape_data_AL(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Alaska (AK)
def scrape_data_AK(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Arizona (AZ)
def scrape_data_AZ(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Arkansas (AR)
def scrape_data_AR(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# California (CA)
def scrape_data_CA(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    table_zone = False
    gf_sf = True
    col_gf = 1
    col_sf = 3
    unit = "thousands"
    time = "ytd thru month"

    stringpart = "\s+\$?\s*([\d,.()-]+)"
    string = stringpart*4

    tax_types_list = []
    tax_types_list.append({"tax_type": "alcoholic beverage excise taxes general fund",   "tax_regex": "alcoholic\s*beverage\s*excise\s*taxes"})
    tax_types_list.append({"tax_type": "alcoholic beverage excise taxes special funds",  "tax_regex": "alcoholic\s*beverage\s*excise\s*taxes"})
    tax_types_list.append({"tax_type": "corporation tax general fund",                   "tax_regex": "corporation\s*tax"})
    tax_types_list.append({"tax_type": "corporation tax special funds",                  "tax_regex": "corporation\s*tax"})
    tax_types_list.append({"tax_type": "cigarette tax general fund",                     "tax_regex": "cigarette\s*tax"})
    tax_types_list.append({"tax_type": "cigarette tax special funds",                    "tax_regex": "cigarette\s*tax"})
    tax_types_list.append({"tax_type": "cannabis excise taxes general fund",             "tax_regex": "cannabis\s*excise\s*taxes"})
    tax_types_list.append({"tax_type": "cannabis excise taxes special funds",            "tax_regex": "cannabis\s*excise\s*taxes"})
    tax_types_list.append({"tax_type": "estate inheritance and gift tax general fund",   "tax_regex": "estate,?\s*inheritance,?\s*.{0,3}\s*gift\s*tax"})
    tax_types_list.append({"tax_type": "estate inheritance and gift tax special funds",  "tax_regex": "estate,?\s*inheritance,?\s*.{0,3}\s*gift\s*tax"})
    tax_types_list.append({"tax_type": "insurance companies tax general fund",           "tax_regex": "insurance\s*companies\s*tax"})
    tax_types_list.append({"tax_type": "insurance companies tax special funds",          "tax_regex": "insurance\s*companies\s*tax"})
    tax_types_list.append({"tax_type": "gasoline tax general fund",                      "tax_regex": "gasoline\s*tax"})
    tax_types_list.append({"tax_type": "gasoline tax special funds",                     "tax_regex": "gasoline\s*tax"})
    tax_types_list.append({"tax_type": "diesel and liquid petroleum gas general fund",   "tax_regex": "diesel\s*.{0,3}\s*liquid\s*petroleum\s*gas"})
    tax_types_list.append({"tax_type": "diesel and liquid petroleum gas special funds",  "tax_regex": "diesel\s*.{0,3}\s*liquid\s*petroleum\s*gas"})
    tax_types_list.append({"tax_type": "jet fuel tax general fund",                      "tax_regex": "jet\s*fuel\s*tax"})
    tax_types_list.append({"tax_type": "jet fuel tax special funds",                     "tax_regex": "jet\s*fuel\s*tax"})
    tax_types_list.append({"tax_type": "vehicle license fees general fund",              "tax_regex": "vehicle\s*license\s*fees"})
    tax_types_list.append({"tax_type": "vehicle license fees special funds",             "tax_regex": "vehicle\s*license\s*fees"})
    tax_types_list.append({"tax_type": "personal income tax general fund",               "tax_regex": "personal\s*income\s*tax"})
    tax_types_list.append({"tax_type": "personal income tax special funds",              "tax_regex": "personal\s*income\s*tax"})
    tax_types_list.append({"tax_type": "retail sales and use taxes general fund",        "tax_regex": "retail\s*sales\s*.{0,3}\s*use\s*taxes"})
    tax_types_list.append({"tax_type": "retail sales and use taxes special funds",       "tax_regex": "retail\s*sales\s*.{0,3}\s*use\s*taxes"})
    tax_types_list.append({"tax_type": "pooled money investment interest general fund",  "tax_regex": "pooled\s*money\s*investment\s*interest"})
    tax_types_list.append({"tax_type": "pooled money investment interest special funds", "tax_regex": "pooled\s*money\s*investment\s*interest"})
    tax_types_list.append({"tax_type": "investment income general fund",                 "tax_regex": "investment\s*income"})
    tax_types_list.append({"tax_type": "investment income special funds",                "tax_regex": "investment\s*income"})
    tax_types_list.append({"tax_type": "alcoholic beverage license fees general fund",   "tax_regex": "alcoholic\s*beverage\s*license\s*fees"})
    tax_types_list.append({"tax_type": "alcoholic beverage license fees special funds",  "tax_regex": "alcoholic\s*beverage\s*license\s*fees"})
    tax_types_list.append({"tax_type": "other fees general fund",                        "tax_regex": "other\s*fees"})
    tax_types_list.append({"tax_type": "other fees special funds",                       "tax_regex": "other\s*fees"})
    tax_types_list.append({"tax_type": "cannabis licensing fees general fund",           "tax_regex": "cannabis\s*licensing\s*fees"})
    tax_types_list.append({"tax_type": "cannabis licensing fees special funds",          "tax_regex": "cannabis\s*licensing\s*fees"})
    tax_types_list.append({"tax_type": "electrical energy tax general fund",             "tax_regex": "electrical\s*energy\s*tax"})
    tax_types_list.append({"tax_type": "electrical energy tax special funds",            "tax_regex": "electrical\s*energy\s*tax"})
    tax_types_list.append({"tax_type": "private rail car tax general fund",              "tax_regex": "private\s*rail\s*car\s*tax"})
    tax_types_list.append({"tax_type": "private rail car tax special funds",             "tax_regex": "private\s*rail\s*car\s*tax"})
    tax_types_list.append({"tax_type": "penalties on traffic violations general fund",   "tax_regex": "penalties\s*on\s*traffic\s*violations"})
    tax_types_list.append({"tax_type": "penalties on traffic violations special funds",  "tax_regex": "penalties\s*on\s*traffic\s*violations"})
    tax_types_list.append({"tax_type": "health care receipts general fund",              "tax_regex": "health\s*care\s*receipts"})
    tax_types_list.append({"tax_type": "health care receipts special funds",             "tax_regex": "health\s*care\s*receipts"})
    tax_types_list.append({"tax_type": "revenues from state lands general fund",         "tax_regex": "revenues\s*from\s*state\s*lands"})
    tax_types_list.append({"tax_type": "revenues from state lands special funds",        "tax_regex": "revenues\s*from\s*state\s*lands"})
    tax_types_list.append({"tax_type": "abandoned property general fund",                "tax_regex": "abandoned\s*property"})
    tax_types_list.append({"tax_type": "abandoned property special funds",               "tax_regex": "abandoned\s*property"})
    tax_types_list.append({"tax_type": "trial court revenues general fund",              "tax_regex": "trial\s*court\s*revenues"})
    tax_types_list.append({"tax_type": "trial court revenues special funds",             "tax_regex": "trial\s*court\s*revenues"})
    tax_types_list.append({"tax_type": "horse racing fees general fund",                 "tax_regex": "horse\s*racing\s*fees"})
    tax_types_list.append({"tax_type": "horse racing fees special funds",                "tax_regex": "horse\s*racing\s*fees"})
    tax_types_list.append({"tax_type": "cap and trade general fund",                     "tax_regex": "cap\s*.{0,3}\s*trade"})
    tax_types_list.append({"tax_type": "cap and trade special funds",                    "tax_regex": "cap\s*.{0,3}\s*trade"})
    tax_types_list.append({"tax_type": "penalty assessments general fund",               "tax_regex": "penalty\s*assessments"})
    tax_types_list.append({"tax_type": "penalty assessments special funds",              "tax_regex": "penalty\s*assessments"})
    tax_types_list.append({"tax_type": "miscellaneous tax revenue general fund",         "tax_regex": "miscellaneous\s*tax\s*revenue"})
    tax_types_list.append({"tax_type": "miscellaneous tax revenue special funds",        "tax_regex": "miscellaneous\s*tax\s*revenue"})
    tax_types_list.append({"tax_type": "miscellaneous general fund",                     "tax_regex": "miscellaneous"})
    tax_types_list.append({"tax_type": "miscellaneous special funds",                    "tax_regex": "miscellaneous"})
    tax_types_list.append({"tax_type": "not otherwise classified general fund",          "tax_regex": "not\s*otherwise\s*classified"})
    tax_types_list.append({"tax_type": "not otherwise classified special funds",         "tax_regex": "not\s*otherwise\s*classified"})

    for line in lines_clean:
        line_found = False

        if len(line) != 0:

            m_gf_sf = re.search(r"(general fund|special funds)\s+(special funds|general fund)", line)
            if m_gf_sf:
                if m_gf_sf.group(1) == "general fund" and m_gf_sf.group(2) == "special funds":
                    gf_sf = True
                elif m_gf_sf.group(1) == "special funds" and m_gf_sf.group(2) == "general fund":
                    gf_sf = False
            
            m_col = re.search(r"(\d{4})\s+(\d{4})\s+(\d{4})\s+(\d{4})", line)
            if m_col:
                if gf_sf:
                    if int(m_col.group(2)) > int(m_col.group(1)):
                        col_gf = 2
                    else:
                        col_gf = 1
                    if int(m_col.group(4)) > int(m_col.group(3)):
                        col_sf = 4
                    else:
                        col_sf = 3
                else:
                    if int(m_col.group(4)) > int(m_col.group(3)):
                        col_gf = 4
                    else:
                        col_gf = 3
                    if int(m_col.group(2)) > int(m_col.group(1)):
                        col_sf = 2
                    else:
                        col_sf = 1

            m_unit = re.search(r"in\s+(dollars|thousands|millions|billions)", line)
            if m_unit:
                if m_unit.group(1) == "dollars":
                    unit = "dollars"
                elif m_unit.group(1) == "thousands":
                    unit = "thousands"
                elif m_unit.group(1) == "millions":
                    unit = "millions"
                elif m_unit.group(1) == "billions":
                    unit = "billions"

            m_table_title = re.search(r"comparative\s+statement\s+of\s+revenues\s+received", line)
            if m_table_title:
                table_zone = True
            m_table_totals = re.search(r"total\s+revenues", line)
            if m_table_totals:
                table_zone = False

            if table_zone:
                for l in range(len(tax_types_list)):
                    tax_type = tax_types_list[l]["tax_type"]
                    tax_regex = tax_types_list[l]["tax_regex"]

                    tax = "(" + tax_regex + ")" + string

                    m = re.search(tax, line)
                    if m:
                        tax_types.append(tax_type)
                        if re.search(r"general\s*fund", tax_type):
                            tax_values.append(clean_value(m.group(col_gf + 1)))
                        elif re.search(r"special\s*funds?", tax_type):
                            tax_values.append(clean_value(m.group(col_sf + 1)))
                        tax_units.append(unit)
                        tax_times.append(time)
                        line_found = True
                    
                if not line_found:
                    tax = "^\s*([a-z]+[\D]*?)" + string
                    m = re.search(tax, line)
                    if m:
                        tax_name = clean_value(m.group(1)).strip()
                        tax_types.append(tax_name + " general fund")
                        tax_values.append(clean_value(m.group(col_gf + 1)))
                        tax_units.append(unit)
                        tax_times.append(time)
                        tax_types.append(tax_name + " special funds")
                        tax_values.append(clean_value(m.group(col_sf + 1)))
                        tax_units.append(unit)
                        tax_times.append(time)
    
    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Colorado (CO)
def scrape_data_CO(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Connecticut (CT)
def scrape_data_CT(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    rev_zone = False
    ref_zone = False
    indent_tct = 0
    indent_rec = 0
    line_tct = 0
    line_rec = 0
    line_num = 0
    col = 2
    unit = "dollars"
    time = "month"

    stringpart = "\s+([\d,.()$-]+)"
    string = stringpart*2

    tax_types_list = []
    tax_types_list.append({"tax_type": "withholding",                               "tax_regex": "withholding"})
    tax_types_list.append({"tax_type": "estimates and finals",                      "tax_regex": "estimates\s*.{0,3}\s*finals"})
    tax_types_list.append({"tax_type": "sales and use",                             "tax_regex": "sales\s*.{0,3}\s*use"})
    tax_types_list.append({"tax_type": "room occupancy",                            "tax_regex": "room\s*occupancy"})
    tax_types_list.append({"tax_type": "corporation business",                      "tax_regex": "corporation\s*business"})
    tax_types_list.append({"tax_type": "pass-through entity",                       "tax_regex": "pass\s*-?\s*through\s*entity"})
    tax_types_list.append({"tax_type": "unrelated business income",                 "tax_regex": "unrelated\s*business\s*income"})
    tax_types_list.append({"tax_type": "cable, satellite and video",                "tax_regex": "cable,?\s*satellite\s*.{0,3}\s*video"})
    tax_types_list.append({"tax_type": "peg account",                               "tax_regex": "peg\s*account"})
    tax_types_list.append({"tax_type": "electric and power",                        "tax_regex": "electric\s*.{0,3}\s*power"})
    tax_types_list.append({"tax_type": "gas companies",                             "tax_regex": "gas\s*companies"})
    tax_types_list.append({"tax_type": "railroads",                                 "tax_regex": "railroads"})
    tax_types_list.append({"tax_type": "estate and gift",                           "tax_regex": "estate\s*.{0,3}\s*gift"})
    tax_types_list.append({"tax_type": "domestic",                                  "tax_regex": "domestic"})
    tax_types_list.append({"tax_type": "foreign",                                   "tax_regex": "foreign"})
    tax_types_list.append({"tax_type": "health care centers",                       "tax_regex": "health\s*care\s*centers"})
    tax_types_list.append({"tax_type": "nonadmitted unauthorized captive insurers", "tax_regex": "nonadmitted\s*/\s*unauthorized\s*/\s*"})
    tax_types_list.append({"tax_type": "alcoholic beverages",                       "tax_regex": "alcoholi?c?\s*beverages"})
    tax_types_list.append({"tax_type": "cigarette",                                 "tax_regex": "cigarette"})
    tax_types_list.append({"tax_type": "electronic cigarette products",             "tax_regex": "electronic\s*cigarette\s*products"})
    tax_types_list.append({"tax_type": "tobacco products",                          "tax_regex": "tobacco\s*products"})
    tax_types_list.append({"tax_type": "controlling interest transfer",             "tax_regex": "controlling\s*interest\s*transfer"})
    tax_types_list.append({"tax_type": "real estate conveyance",                    "tax_regex": "real\s*estate\s*conveyance"})
    tax_types_list.append({"tax_type": "petroleum gross earnings",                  "tax_regex": "petroleum\s*gross\s*earnings"})
    tax_types_list.append({"tax_type": "admission and dues and tnc fee",            "tax_regex": "admission\s*.{0,3}\s*dues\s*.{0,3}\s*tnc\s*fee"})
    tax_types_list.append({"tax_type": "dry cleaners",                              "tax_regex": "dry\s*cleaners"})
    tax_types_list.append({"tax_type": "occupational",                              "tax_regex": "occupational"})
    tax_types_list.append({"tax_type": "rental surcharge",                          "tax_regex": "rental\s*surcharge"})
    tax_types_list.append({"tax_type": "solid waste",                               "tax_regex": "solid\s*waste"})
    tax_types_list.append({"tax_type": "tourism tax",                               "tax_regex": "tourism\s*tax"})
    tax_types_list.append({"tax_type": "controlled substances",                     "tax_regex": "controlled\s*substances"})
    tax_types_list.append({"tax_type": "prepaid wireless e911 fee",                 "tax_regex": "prepaid\s*wireless\s*e-?9-?1-?1\s*fee"})
    tax_types_list.append({"tax_type": "cannabis tax",                              "tax_regex": "cannabis\s*tax"})
    tax_types_list.append({"tax_type": "paid preparer fee",                         "tax_regex": "paid\s*preparer\s*fee"})
    tax_types_list.append({"tax_type": "repealed taxes",                            "tax_regex": "repealed\s*taxes"})
    tax_types_list.append({"tax_type": "nursing home user fee",                     "tax_regex": "nursing\s*home\s*user\s*fee"})
    tax_types_list.append({"tax_type": "hospitals",                                 "tax_regex": "hospitals"})
    tax_types_list.append({"tax_type": "intermediate care facility",                "tax_regex": "intermediate\s*care\s*facility"})
    tax_types_list.append({"tax_type": "ambulatory surgical center",                "tax_regex": "ambulatory\s*surgical\s*center"})
    tax_types_list.append({"tax_type": "gasoline",                                  "tax_regex": "gasoline"})
    tax_types_list.append({"tax_type": "special fuel",                              "tax_regex": "special\s*fuel"})
    tax_types_list.append({"tax_type": "motor carrier",                             "tax_regex": "motor\s*carrier"})
    tax_types_list.append({"tax_type": "highway use fee",                           "tax_regex": "highway\s*use\s*fee"})
    tax_types_list.append({"tax_type": "total motor fuel taxes",                    "tax_regex": "total\s*motor\s*fuel\s*taxes"})
    tax_types_list.append({"tax_type": "total healthcare taxes",                    "tax_regex": "total\s*healthcare\s*taxes"})
    tax_types_list.append({"tax_type": "total miscellaneous taxes",                 "tax_regex": "total\s*miscellaneous\s*taxes"})
    tax_types_list.append({"tax_type": "total cigarette taxes",                     "tax_regex": "total\s*cigarette\s*taxes"})
    tax_types_list.append({"tax_type": "total income taxes",                        "tax_regex": "total\s*income\s*taxes"})
    tax_types_list.append({"tax_type": "total sales & use tax",                     "tax_regex": "total\s*sales\s*.{0,3}?\s*use\s*tax"})
    tax_types_list.append({"tax_type": "total corporation taxes",                   "tax_regex": "total\s*corporation\s*taxes"})
    tax_types_list.append({"tax_type": "total public service corps.",               "tax_regex": "total\s*public\s*service\s*corps."})
    tax_types_list.append({"tax_type": "total insurance taxes",                     "tax_regex": "total\s*insurance\s*taxes"})
    tax_types_list.append({"tax_type": "licenses",                                  "tax_regex": "licenses"})
    tax_types_list.append({"tax_type": "beverage container deposit",                "tax_regex": "beverage\s*container\s*deposit"})
    tax_types_list.append({"tax_type": "total healthcare fees",                     "tax_regex": "total\s*healthcare\s*fees"})
    
    tax_types_list_ref = []
    tax_types_list_ref.append({"tax_type": "withholding refund",                   "tax_regex": "withholding"})
    tax_types_list_ref.append({"tax_type": "income tax refund",                    "tax_regex": "income\s*tax"})
    tax_types_list_ref.append({"tax_type": "sales and use refund",                 "tax_regex": "sales\s*.{0,3}?\s*use"})
    tax_types_list_ref.append({"tax_type": "room occupancy refund",                "tax_regex": "room\s*occupancy"})
    tax_types_list_ref.append({"tax_type": "business entity refund",               "tax_regex": "business\s*entity"})
    tax_types_list_ref.append({"tax_type": "corporation business refund",          "tax_regex": "corporation\s*business"})
    tax_types_list_ref.append({"tax_type": "r & d credit buybacks refund",         "tax_regex": "r\s*.{0,3}?\s*d\s*credit\s*buybacks"})
    tax_types_list_ref.append({"tax_type": "pass-through entity refund",           "tax_regex": "pass\s*-?\s*through\s*entity"})
    tax_types_list_ref.append({"tax_type": "unrelated business refund",            "tax_regex": "unrelated\s*business"})
    tax_types_list_ref.append({"tax_type": "cable, satellite and video refund",    "tax_regex": "cable,\s*satellite\s*.{0,3}?\s*video"})
    tax_types_list_ref.append({"tax_type": "peg account refund",                   "tax_regex": "peg\s*account"})
    tax_types_list_ref.append({"tax_type": "electric and power refund",            "tax_regex": "electric\s*.{0,3}?\s*power"})
    tax_types_list_ref.append({"tax_type": "gas companies refund",                 "tax_regex": "gas\s*companies"})
    tax_types_list_ref.append({"tax_type": "estate and gift refund",               "tax_regex": "estate\s*.{0,3}?\s*gift"})
    tax_types_list_ref.append({"tax_type": "domestic insurance refund",            "tax_regex": "domestic\s*insurance"})
    tax_types_list_ref.append({"tax_type": "foreign insurance refund",             "tax_regex": "foreign\s*insurance"})
    tax_types_list_ref.append({"tax_type": "health care centers refund",           "tax_regex": "health\s*care\s*centers"})
    tax_types_list_ref.append({"tax_type": "nonadmitted insurance refund",         "tax_regex": "nonadmitted\s*insurance"})
    tax_types_list_ref.append({"tax_type": "alcoholic beverages refund",           "tax_regex": "alcoholic\s*beverages"})
    tax_types_list_ref.append({"tax_type": "cigarette refund",                     "tax_regex": "cigarette"})
    tax_types_list_ref.append({"tax_type": "electronic cigarette products refund", "tax_regex": "electronic\s*cigarette\s*products"})
    tax_types_list_ref.append({"tax_type": "tobacco products refund",              "tax_regex": "tobacco\s*products"})
    tax_types_list_ref.append({"tax_type": "controlling interest refund",          "tax_regex": "controlling\s*interest"})
    tax_types_list_ref.append({"tax_type": "real estate conveyance refund",        "tax_regex": "real\s*estate\s*conveyance"})
    tax_types_list_ref.append({"tax_type": "petroleum gross earnings refund",      "tax_regex": "petroleum\s*gross\s*earnings"})
    tax_types_list_ref.append({"tax_type": "admissions and dues refund",           "tax_regex": "admissions\s*.{0,3}?\s*dues"})
    tax_types_list_ref.append({"tax_type": "dry cleaners refund",                  "tax_regex": "dry\s*cleaners"})
    tax_types_list_ref.append({"tax_type": "occupational refund",                  "tax_regex": "occupational"})
    tax_types_list_ref.append({"tax_type": "pre-paid wireless refund",             "tax_regex": "pre\s*-?\s*paid\s*wireless"})
    tax_types_list_ref.append({"tax_type": "nursing home user fee refund",         "tax_regex": "nursing\s*home\s*user\s*fee"})
    tax_types_list_ref.append({"tax_type": "hospitals refund",                     "tax_regex": "hospitals"})
    tax_types_list_ref.append({"tax_type": "intermediate care facility refund",    "tax_regex": "intermediate\s*care\s*facility"})
    tax_types_list_ref.append({"tax_type": "ambulatory surgical center refund",    "tax_regex": "ambulatory\s*surgical\s*center"})
    tax_types_list_ref.append({"tax_type": "gasoline refund",                      "tax_regex": "gasoline"})
    tax_types_list_ref.append({"tax_type": "special fuel refund",                  "tax_regex": "special\s*fuel"})
    tax_types_list_ref.append({"tax_type": "motor carrier refund",                 "tax_regex": "motor\s*carrier"})
    tax_types_list_ref.append({"tax_type": "highway use fee refund",               "tax_regex": "highway\s*use\s*fee"})
    tax_types_list_ref.append({"tax_type": "beverage containers refund",           "tax_regex": "beverage\s*containers"})
    tax_types_list_ref.append({"tax_type": "miscellaneous refund",                 "tax_regex": "miscellaneous"})
    tax_types_list_ref.append({"tax_type": "second hospital user fee refund",      "tax_regex": "second\s*hospital\s*user\s*fee"})
    
    m_nn = False

    for line in lines_clean:
        line_found = False
        if len(line) != 0:
            line_num += 1

            m_table_title = re.search(r"(current month revenue comparison|current month refunds comparison)", line)
            if m_table_title:
                if m_table_title.group(1) == "current month revenue comparison":
                    rev_zone = True
                    ref_zone = False
                elif m_table_title.group(1) == "current month refunds comparison":
                    rev_zone = False
                    ref_zone = True
            m_table_totals = re.search(r"(totals|(total\s+refunds))\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
            if m_table_totals:
                rev_zone = False
                ref_zone = False

            m_col1 = re.search(r"(type\s+of\s+revenue|type\s+of\s+refund)\s+(\d{4})\s+(\d{4})", line)
            m_col2 = re.search(r"tax\s+type\s+through\s+\S+\s+(\d{4})\s+through\s+\S+\s+(\d{4})", line)
 
            if m_col1:
                if int(m_col1.group(3)) > int(m_col1.group(2)):
                    col = 3
                else:
                    col = 2
            if m_col2:
                if int(m_col2.group(2)) > int(m_col2.group(1)):
                    col = 3
                else:
                    col = 2

            if rev_zone:
                for l in range(len(tax_types_list)):
                    tax_type = tax_types_list[l]["tax_type"]
                    tax_regex = tax_types_list[l]["tax_regex"]

                    tax = "(" + tax_regex + ")" + string
                    if tax_type == "nonadmitted unauthorized captive insurers":
                        m_nonadm = re.search(tax_regex, line)
                        if m_nonadm:
                            m_nn = True

                    else:
                        m = re.search(tax, line)
                        if m:
                            line_found = True
                            if tax_type in ["estate and gift", "real estate conveyance"]:
                                if tax_type in tax_types:
                                    continue
                            tax_types.append(tax_type)
                            tax_values.append(clean_value(m.group(col)))
                            tax_units.append(unit)
                            tax_times.append(time)
                    if m_nn:
                        m = re.search(string, line)
                        if m:
                            line_found = True
                            m_nn = False
                            tax_types.append("nonadmitted unauthorized captive insurers")
                            tax_values.append(clean_value(m.group(col-1)))
                            tax_units.append(unit)
                            tax_times.append(time)
                            
                if not line_found:
                    #tax = "^\s*([a-z]+[\D]*?)" + string
                    tax = "^\s*(\(.*\))?\s*([a-z]+[\D]*?)" + string
                    m = re.search(tax, line)
                    if m:
                        if clean_value(m.group(2).strip()) == "type of revenue":
                            continue
                        tax_types.append(clean_value(m.group(2)).strip())
                        tax_values.append(clean_value(m.group(col + 1)))
                        tax_units.append(unit)
                        tax_times.append(time)

            if ref_zone:
                for l in range(len(tax_types_list_ref)):
                    tax_type = tax_types_list_ref[l]["tax_type"]
                    tax_regex = tax_types_list_ref[l]["tax_regex"]

                    tax = "(" + tax_regex + ")" + string
                    m = re.search(tax, line)
                    if m:
                        line_found = True
                        if tax_type in ["estate and gift", "real estate conveyance"]:
                            if tax_type in tax_types:
                                continue
                        tax_types.append(tax_type)
                        if tax_type in ["r and d credit buybacks refund", "hospitals refund"]:
                            # tax_values.append(clean_value(m.group(col + 1)))
                            value = clean_value(m.group(col + 1))
                        else:
                            # tax_values.append
                            value = clean_value(m.group(col))
                        value = str(-1 * abs(float(value.replace(",", "").replace("--", ""))))
                        tax_values.append(value)
                        tax_units.append(unit)
                        tax_times.append(time)
                        
                if not line_found:
                    tax = "^\s*([a-z]+[\D]*?)" + string
                    m = re.search(tax, line)
                    if m:
                        if clean_value(m.group(1).strip()) == "type of refund":
                            continue
                        tax_types.append(clean_value(m.group(1)).strip() + " refund")
                        value = clean_value(m.group(col))
                        value = str(-1 * abs(float(value.replace(",", "").replace("--", ""))))
                        tax_values.append(value)
                        tax_units.append(unit)
                        tax_times.append(time)
    
    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Delaware (DE)
def scrape_data_DE(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# District of Columbia (DC)
def scrape_data_DE(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Florida (FL)
def scrape_data_FL(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Georgia (GA)
def scrape_data_GA(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Hawaii (HI)
def scrape_data_HI(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Idaho (ID)
def scrape_data_ID(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Illinois (IL)
def scrape_data_IL(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Indiana (IN)
def scrape_data_IN(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Iowa (IA)
def scrape_data_IA(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Kansas (KS)
def scrape_data_KS(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Kentucky (KY)
def scrape_data_KY(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Louisiana (LA)
def scrape_data_LA(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Maine (ME)
def scrape_data_ME(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Maryland (MD)
def scrape_data_MD(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Massachusetts (MA)
def scrape_data_MA(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Michigan (MI)
def scrape_data_MI(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Minnesota (MN)
def scrape_data_MN(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Mississippi (MS)
def scrape_data_MS(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Missouri (MO)
def scrape_data_MO(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Montana (MT)
def scrape_data_MT(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Nebraska (NE)
def scrape_data_NE(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Nevada (NV)
def scrape_data_NV(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# New Hampshire (NH)
def scrape_data_NH(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# New Jersey (NJ)
def scrape_data_NJ(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    col = 2
    unit = "thousands"
    time = "month"

    stringpart = "\s*\$?\s*([\d,.()$%-]+)"
    string1 = stringpart*3
    stringpart = "\s+\$?\s*([\d,.()$%-]+)"
    string2 = stringpart*3

    tax_types_list = []
    tax_types_list.append({"tax_type": "sales",                             "tax_regex": "sales"})
    tax_types_list.append({"tax_type": "sales tax - energy tax receipts",   "tax_regex": "sales\s*tax\s*-?\s*energy\s*tax\s*receipts"})
    tax_types_list.append({"tax_type": "sales tax dedication",              "tax_regex": "sales\s*tax\s*dedication"})
    tax_types_list.append({"tax_type": "net sales tax",                     "tax_regex": "net\s*sales\s*tax"})
    tax_types_list.append({"tax_type": "corporation business",              "tax_regex": "corporation\s*business"})
    tax_types_list.append({"tax_type": "cbt - energy tax receipts",         "tax_regex": "cbt\s*-?\s*energy\s*tax\s*receipts"})
    tax_types_list.append({"tax_type": "net corporation business tax",      "tax_regex": "net\s*corporation\s*business\s*tax"})
    tax_types_list.append({"tax_type": "business alternative income tax",   "tax_regex": "business\s*alternative\s*income\s*tax"})
    tax_types_list.append({"tax_type": "motor fuels",                       "tax_regex": "motor\s*fuels"})
    tax_types_list.append({"tax_type": "motor vehicle fees",                "tax_regex": "motor\s*vehicle\s*fees"})
    tax_types_list.append({"tax_type": "transfer inheritance tax",          "tax_regex": "transfer\s*inheritance\s*tax"})
    tax_types_list.append({"tax_type": "estate tax",                        "tax_regex": "estate\s*tax"})
    tax_types_list.append({"tax_type": "insurance premium",                 "tax_regex": "insurance\s*premium"})
    tax_types_list.append({"tax_type": "cigarette",                         "tax_regex": "cigarette"})
    tax_types_list.append({"tax_type": "petroleum products gross receipts", "tax_regex": "petroleum\s*products\s*gross\s*receipts"})
    tax_types_list.append({"tax_type": "capital reserve",                   "tax_regex": "capital\s*reserve"})
    tax_types_list.append({"tax_type": "alcoholic beverage excise",         "tax_regex": "alcoholic\s*beverage\s*excise"})
    tax_types_list.append({"tax_type": "realty transfer",                   "tax_regex": "realty\s*transfer"})
    tax_types_list.append({"tax_type": "tobacco products wholesale sales",  "tax_regex": "tobacco\s*products\s*wholesale\s*sales"})
    tax_types_list.append({"tax_type": "public utility",                    "tax_regex": "public\s*utility"})
    tax_types_list.append({"tax_type": "total general fund revenues",       "tax_regex": "total\s*general\s*fund\s*revenues"})
    tax_types_list.append({"tax_type": "gross income tax (ptrf)",           "tax_regex": "gross\s*income\s*tax\s*\(*ptrf\)*"})
    tax_types_list.append({"tax_type": "sales tax dedication",              "tax_regex": "sales\s*tax\s*dedication"})
    tax_types_list.append({"tax_type": "net gross income tax (ptrf)",       "tax_regex": "net\s*gross\s*income\s*tax\s*\(*ptrf\)*"})
    tax_types_list.append({"tax_type": "casino revenue",                    "tax_regex": "casino\s*revenue"})
    tax_types_list.append({"tax_type": "total major revenues",              "tax_regex": "total\s*major\s*revenues"})
    tax_types_list.append({"tax_type": "lottery",                           "tax_regex": "lottery"})

    rev_zone = False
    started = False
    for line in lines_clean:
        line_found = False

        if len(line) != 0:
            rev_start = re.search(r"\s*(\d{4})\s+(\d{4})\s+change\s*", line)
            if rev_start:
                rev_zone = True
                started = True
                if rev_start.group(1) == yyyy:
                    col = 1
                elif rev_start.group(2) == yyyy:
                    col = 2
            else:
                started = False
                
            if rev_zone:
                rev_end = re.search(r"^\s*(\*|(\(?[a-z]))", line)
                if rev_end:
                    rev_zone = False

            if rev_zone and not started:
                for l in range(len(tax_types_list)):
                    tax_type = tax_types_list[l]["tax_type"]
                    tax_regex = tax_types_list[l]["tax_regex"]

                    tax = "^" + string1 + "\s*(" + tax_regex + ")\s*(\(*.??\)*)?" + string2

                    m = re.search(tax, line, re.I)
                    if m:
                        tax_types.append(tax_type)
                        tax_values.append(clean_value(m.group(col)))
                        tax_units.append(unit)
                        tax_times.append(time)
                        line_found = True
                        break
                    
                if not line_found and not started:
                    tax = "^" + string1 + "\s*([a-z]+[\D]*?)\s*(\(*.??\)*)?" + string2
                    m = re.search(tax, line)
                    if m:
                        tax_types.append(clean_value(m.group(4)).strip())
                        tax_values.append(clean_value(m.group(col)))
                        tax_units.append(unit)
                        tax_times.append(time)
    
    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# New Mexico (NM)
def scrape_data_NM(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# New York (NY)
def scrape_data_NY(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# North Carolina (NC)
def scrape_data_NC(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# North Dakota (ND)
def scrape_data_ND(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Ohio (OH)
def scrape_data_OH(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Oklahoma (OK)
def scrape_data_OK(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Oregon (OR)
def scrape_data_OR(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Pennsylvania (PA)
def scrape_data_PA(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    fund_zone = False
    atoe_zone = False
    col = 2
    unit = "thousands"
    time = "month"

    stringpart = "\s+([\d,.()$-]+)"
    string = stringpart*2

    tax_types_list = []
    tax_types_list.append({"tax_type": "total - general fund",                  "tax_regex": "total\s*-?\s*general\s*fund"})
    tax_types_list.append({"tax_type": "total - tax revenue",                   "tax_regex": "total\s*-?\s*tax\s*revenue"})
    tax_types_list.append({"tax_type": "total - corporation taxes",             "tax_regex": "total\s*-?\s*corporation\s*taxes"})
    tax_types_list.append({"tax_type": "accelerated deposits",                  "tax_regex": "accelerated\s*deposits"})
    tax_types_list.append({"tax_type": "corporate net income",                  "tax_regex": "corporate\s*net\s*income"})
    tax_types_list.append({"tax_type": "gross receipts",                        "tax_regex": "gross\s*receipts"})
    tax_types_list.append({"tax_type": "utility property",                      "tax_regex": "utility\s*property"})
    tax_types_list.append({"tax_type": "insurance premiums",                    "tax_regex": "insurance\s*premiums"})
    tax_types_list.append({"tax_type": "bank shares",                           "tax_regex": "bank\s*shares"})
    tax_types_list.append({"tax_type": "mutual thrift",                         "tax_regex": "mutual\s*thrift"})
    tax_types_list.append({"tax_type": "total - consumption taxes",             "tax_regex": "total\s*-?\s*consumption\s*taxes"})
    tax_types_list.append({"tax_type": "sales and use",                         "tax_regex": "sales\s*.{0,3}?\s*use"})
    tax_types_list.append({"tax_type": "non-motor vehicle",                     "tax_regex": "non\s*-?\s*motor\s*vehicle"})
    tax_types_list.append({"tax_type": "motor vehicle",                         "tax_regex": "motor\s*vehicle"})
    tax_types_list.append({"tax_type": "cigarette",                             "tax_regex": "cigarette"})
    tax_types_list.append({"tax_type": "other tobacco products",                "tax_regex": "other\s*tobacco\s*products"})
    tax_types_list.append({"tax_type": "malt beverage",                         "tax_regex": "malt\s*beverage"})
    tax_types_list.append({"tax_type": "liquor",                                "tax_regex": "liquor"})
    tax_types_list.append({"tax_type": "total - other taxes",                   "tax_regex": "total\s*-?\s*other\s*taxes"})
    tax_types_list.append({"tax_type": "total - personal income & other taxes", "tax_regex": "total\s*-?\s*personal\s*income\s*.{0,3}?\s*other\s*taxes"})
    tax_types_list.append({"tax_type": "personal income",                       "tax_regex": "personal\s*income"})
    tax_types_list.append({"tax_type": "withholding",                           "tax_regex": "withholding"})
    tax_types_list.append({"tax_type": "quarterly",                             "tax_regex": "quarterly"})
    tax_types_list.append({"tax_type": "annual",                                "tax_regex": "annual"})
    tax_types_list.append({"tax_type": "realty transfer",                       "tax_regex": "realty\s*transfer"})
    tax_types_list.append({"tax_type": "inheritance",                           "tax_regex": "inheritance"})
    tax_types_list.append({"tax_type": "gaming",                                "tax_regex": "gaming"})
    tax_types_list.append({"tax_type": "minor and repealed",                    "tax_regex": "minor\s*.{0,3}?\s*repealed"})
    tax_types_list.append({"tax_type": "total - non-tax revenue",               "tax_regex": "total\s*-?\s*non\s*-?\s*tax\s*revenue"})
    tax_types_list.append({"tax_type": "liquor store profits",                  "tax_regex": "liquor\s*store\s*profits"})
    tax_types_list.append({"tax_type": "licenses & fees",                       "tax_regex": "licenses\s*.{0,3}?\s*fees"})
    tax_types_list.append({"tax_type": "miscellaneous",                         "tax_regex": "miscellaneous"})
    tax_types_list.append({"tax_type": "fines, penalties, & interest",          "tax_regex": "fines.??\s*penalties.??\s*.{0,3}?\s*interest"})
    tax_types_list.append({"tax_type": "revenue sources",                       "tax_regex": "revenue\s*sources"})
    tax_types_list.append({"tax_type": "total - motor license fund",            "tax_regex": "total\s*-?\s*motor\s*license\s*fund"})
    tax_types_list.append({"tax_type": "total liquid fuels taxes",              "tax_regex": "total\s*-?\s*liquid\s*fuels\s*taxes"})
    tax_types_list.append({"tax_type": "motor carriers/ifta",                   "tax_regex": "motor\s*carriers\s*\/?\s*ifta"})
    tax_types_list.append({"tax_type": "alternative fuels",                     "tax_regex": "alternative\s*fuels"})
    tax_types_list.append({"tax_type": "oil company franchise",                 "tax_regex": "oil\s*company\s*franchise"})
    tax_types_list.append({"tax_type": "total - licenses and fees",             "tax_regex": "total\s*-?\s*licenses\s*.{0,3}?\s*fees"})
    tax_types_list.append({"tax_type": "special hauling permits",               "tax_regex": "special\s*hauling\s*permits"})
    tax_types_list.append({"tax_type": "registrations other states-irp",        "tax_regex": "registrations\s*other\s*states\s*-?\s*irp"})
    tax_types_list.append({"tax_type": "operators licenses",                    "tax_regex": "operators\s*licenses"})
    tax_types_list.append({"tax_type": "real id",                               "tax_regex": "real\s*id"})
    tax_types_list.append({"tax_type": "vehicle registrations and titling",     "tax_regex": "vehicle\s*registrations\s*.{0,3}?\s*titling"})
    tax_types_list.append({"tax_type": "miscellaneous collections",             "tax_regex": "miscellaneous\s*collections"})
    tax_types_list.append({"tax_type": "treasury",                              "tax_regex": "treasury"})
    tax_types_list.append({"tax_type": "escheats",                              "tax_regex": "escheats"})
    tax_types_list.append({"tax_type": "electric vehicle",                      "tax_regex": "electric\s*vehicles?"})

    for line in lines_clean:
        line_found = False
        
        if len(line) != 0:
            m_fund = re.search(r"general\s+fund\s+comparison\s+of\s*actual\s*to\s*estimate\s*$", line) 
            m_end = re.search(r"total[ -]+other\s+motor\s+receipts", line)
            if m_fund:
                fund_zone = True
            elif m_end:
                fund_zone = False

            m_col = re.search(r"revenue\s+sources\s+(actual|estimated)\s+(actual|estimated)", line)
            if m_col:
                if m_col.group(2) == "actual":
                    col = 3
                elif m_col.group(1) == "actual": 
                    col = 2

            if fund_zone:
                for l in tax_types_list.index:
                    tax_type = tax_types_list[l]["tax_type"]
                    tax_regex = tax_types_list[l]["tax_regex"]

                    tax = "(" + tax_regex + ")" + string

                    m = re.search(tax, line)
                    if m:
                        tax_types.append(tax_type)
                        tax_values.append(clean_value(m.group(col)))
                        tax_units.append(unit)
                        tax_times.append(time)
                        line_found = True

                if not line_found:
                     tax = "^\s*([a-z]+[^\d]*?)" + string
                     m = re.search(tax, line)
                     if m:
                        tax_types.append(clean_value(m.group(1)).strip())
                        tax_values.append(clean_value(m.group(col)))
                        tax_units.append(unit)
                        tax_times.append(time)

    tts = []
    tvs = []
    tus = []
    ttms = []
    for i in range(len(tax_types)):
        if tax_types[i] not in tts:
            tts.append(tax_types[i])
            tvs.append(tax_values[i])
            tus.append(tax_units[i])
            ttms.append(tax_times[i])
    tax_types = tts
    tax_values = tvs
    tax_units = tus
    tax_times = ttms
    
    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Puerto Rico (PR)
def scrape_data_PA(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Rhode Island (RI)
def scrape_data_RI(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# South Carolina (SC)
def scrape_data_SC(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# South Dakota (SD)
def scrape_data_SD(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Tennessee (TN)
def scrape_data_TN(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Texas (TX)
def scrape_data_TX(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Utah (UT)
def scrape_data_UT(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Vermont (VT)
def scrape_data_VT(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Virginia (VA)
def scrape_data_VA(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Washington (WA)
def scrape_data_WA(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# West Virginia (WV)
def scrape_data_WV(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Wisconsin (WI)
def scrape_data_WI(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Wyoming (WY)
def scrape_data_WY(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    n_types  = len(tax_types)
    n_values = len(tax_values)
    n_units  = len(tax_units)
    n_times  = len(tax_times)

    if n_types > 0 and n_types == n_values and n_values == n_units and n_units == n_times:
        for i in range(len(tax_types)):
            data.append([state, yyyy, mm, tax_types[i], tax_values[i], tax_units[i], tax_times[i]])
    return data

# Name:        create_output
# Purpose:     Create output TXT file containing scraped data
# Parameters:  data (scraped data)
#              loc (path of output file)
# Returns:     

def create_output(data, loc):
    if len(data) > 0:
        f = codecs.open(loc, 'w', encoding="utf8")
        varbs = ["state", "year", "month", "tax_type", "tax_value", "tax_unit", "tax_time"]
        f.write("|".join(varbs) + "\n")
        for i in range(len(data)):
            f.write("|".join(data[i]) + "\n")
        f.close()
    return

# Name:        scrape_data
# Purpose:     Iterate through states and scrape data from previously downloaded PDFs
# Parameters:  projName (project name)
#              yyyy (4-digit year)
#              mm (2-digit month)
# Returns:     

def scrape_data(projName, yyyy, mm):
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

    # List to store all of the scraped data
    prod = []
    prodLoc = "./{}/prod/{}_{}.txt".format(projName, yyyy, mm)

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
    states = ["CA", "CT", "NJ", "PA"]

    for state in states:
        print_section_name(statesDict[state])
        docName = "{}_{}_{}".format(state, yyyy, mm)
        pdfLoc = "./{}/pdf/{}.pdf".format(projName, docName)
        txtLoc = "./{}/txt/{}.txt".format(projName, docName)
        datLoc = "./{}/dat/{}.txt".format(projName, docName)

        if os.path.isfile(pdfLoc):
            print("PDF exists.")
        else:
            print("No PDF exists.")
            print("No converted TXT file created.")
            print("No output TXT file created.")

        if os.path.isfile(txtLoc):
            print("Converted TXT file already exists.")
        elif os.path.isfile(pdfLoc):
            convert_pdf_to_txt(pdfLoc, txtLoc)
            if os.path.isfile(txtLoc):
                print("Converted TXT file created.")
            else:
                print("No converted TXT file created.")
        
        if os.path.isfile(datLoc):
            print("Output TXT file already exists.  Removing ...")
            os.system("rm {}".format(datLoc))
        if os.path.isfile(txtLoc):
            data = []
            lines_clean = get_text(txtLoc)
            if state == "AL":
                data = scrape_data_AL(lines_clean, state, yyyy, mm)
            elif state == "AK":
                data = scrape_data_AK(lines_clean, state, yyyy, mm)
            elif state == "AZ":
                data = scrape_data_AZ(lines_clean, state, yyyy, mm)
            elif state == "AR":
                data = scrape_data_AR(lines_clean, state, yyyy, mm)
            elif state == "CA":
                data = scrape_data_CA(lines_clean, state, yyyy, mm)
            elif state == "CO":
                data = scrape_data_CO(lines_clean, state, yyyy, mm)
            elif state == "CT":
                data = scrape_data_CT(lines_clean, state, yyyy, mm)
            elif state == "DE":
                data = scrape_data_DE(lines_clean, state, yyyy, mm)
            elif state == "DC":
                data = scrape_data_DC(lines_clean, state, yyyy, mm)
            elif state == "FL":
                data = scrape_data_FL(lines_clean, state, yyyy, mm)
            elif state == "GA":
                data = scrape_data_GA(lines_clean, state, yyyy, mm)
            elif state == "HI":
                data = scrape_data_HI(lines_clean, state, yyyy, mm)
            elif state == "ID":
                data = scrape_data_ID(lines_clean, state, yyyy, mm)
            elif state == "IL":
                data = scrape_data_IL(lines_clean, state, yyyy, mm)
            elif state == "IN":
                data = scrape_data_IN(lines_clean, state, yyyy, mm)
            elif state == "IA":
                data = scrape_data_IA(lines_clean, state, yyyy, mm)
            elif state == "KS":
                data = scrape_data_KS(lines_clean, state, yyyy, mm)
            elif state == "KY":
                data = scrape_data_KY(lines_clean, state, yyyy, mm)
            elif state == "LA":
                data = scrape_data_LA(lines_clean, state, yyyy, mm)
            elif state == "ME":
                data = scrape_data_ME(lines_clean, state, yyyy, mm)
            elif state == "MD":
                data = scrape_data_MD(lines_clean, state, yyyy, mm)
            elif state == "MA":
                data = scrape_data_MA(lines_clean, state, yyyy, mm)
            elif state == "MI":
                data = scrape_data_MI(lines_clean, state, yyyy, mm)
            elif state == "MN":
                data = scrape_data_MN(lines_clean, state, yyyy, mm)
            elif state == "MS":
                data = scrape_data_MS(lines_clean, state, yyyy, mm)
            elif state == "MO":
                data = scrape_data_MO(lines_clean, state, yyyy, mm)
            elif state == "MT":
                data = scrape_data_MT(lines_clean, state, yyyy, mm)
            elif state == "NE":
                data = scrape_data_NE(lines_clean, state, yyyy, mm)
            elif state == "NV":
                data = scrape_data_NV(lines_clean, state, yyyy, mm)
            elif state == "NH":
                data = scrape_data_NH(lines_clean, state, yyyy, mm)
            elif state == "NJ":
                data = scrape_data_NJ(lines_clean, state, yyyy, mm)
            elif state == "NM":
                data = scrape_data_NM(lines_clean, state, yyyy, mm)
            elif state == "NY":
                data = scrape_data_NY(lines_clean, state, yyyy, mm)
            elif state == "NC":
                data = scrape_data_NC(lines_clean, state, yyyy, mm)
            elif state == "ND":
                data = scrape_data_ND(lines_clean, state, yyyy, mm)
            elif state == "OH":
                data = scrape_data_OH(lines_clean, state, yyyy, mm)
            elif state == "OK":
                data = scrape_data_OK(lines_clean, state, yyyy, mm)
            elif state == "OR":
                data = scrape_data_OR(lines_clean, state, yyyy, mm)
            elif state == "PA":
                data = scrape_data_PA(lines_clean, state, yyyy, mm)
            elif state == "PR":
                data = scrape_data_PR(lines_clean, state, yyyy, mm)
            elif state == "RI":
                data = scrape_data_RI(lines_clean, state, yyyy, mm)
            elif state == "SC":
                data = scrape_data_SC(lines_clean, state, yyyy, mm)
            elif state == "SD":
                data = scrape_data_SD(lines_clean, state, yyyy, mm)
            elif state == "TN":
                data = scrape_data_TN(lines_clean, state, yyyy, mm)
            elif state == "TX":
                data = scrape_data_TX(lines_clean, state, yyyy, mm)
            elif state == "UT":
                data = scrape_data_UT(lines_clean, state, yyyy, mm)
            elif state == "VT":
                data = scrape_data_VT(lines_clean, state, yyyy, mm)
            elif state == "VA":
                data = scrape_data_VA(lines_clean, state, yyyy, mm)
            elif state == "WA":
                data = scrape_data_WA(lines_clean, state, yyyy, mm)
            elif state == "WV":
                data = scrape_data_WV(lines_clean, state, yyyy, mm)
            elif state == "WI":
                data = scrape_data_WI(lines_clean, state, yyyy, mm)
            elif state == "WY":
                data = scrape_data_WY(lines_clean, state, yyyy, mm)
            prod.extend(data)
            create_output(data, datLoc)
            if os.path.isfile(datLoc):
                print("Output TXT file created.")
                print("Number of line items scraped: {}".format(len(data)))
            else:
                print("No output TXT file created.")
    
    print_section_name("Product")
    if os.path.isfile(prodLoc):
        print("Product already exists.  Removing ...")
        os.system("rm {}".format(prodLoc))
    create_output(prod, prodLoc)
    if os.path.isfile(prodLoc):
        print("Product created.")
    else:
        print("No product created.")
    
    print("")
    return

def main():
    # Check valid arguments
    if valid_arguments():
        scrape_data(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("\nInvalid arguments\n")
    return   

if __name__ == "__main__":
    main()
