#Name:        m2_scrape.py
#Purpose:     Scrape specific tax revenue values from downloaded PDFs
#Invocation:  python3 m2_scrape.py <projName> <yyyy> <mm>

import codecs
import os
import re
import sys

#Name:       valid_arguments
#Arguments:  sys.argv (globally defined list of command-line arguments)
#Purpose:    Check whether the command-line arguments are valid

def valid_arguments():
    valid = False
    yearValid = [str(yyyy) for yyyy in range(2000, 2051)]
    monthValid = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    if len(sys.argv) == 4:
        if re.search(r"^[a-zA-Z][a-zA-Z_-]*$", sys.argv[1]) and sys.argv[2] in yearValid and sys.argv[3] in monthValid:
            valid = True
    return valid

#Name:       print_section
#Arguments:  section (section name)
#Purpose:    Print name of section

def print_section(section):
    n = len(section)
    print("")
    print("=" * (n + 12))
    print("===   " + section + "   ===")
    print("=" * (n + 12))
    print("")
    return

#Name:       convert_pdf_to_txt
#Arguments:  pdfLoc (path of PDF)
#            txtLoc (path of TXT file)
#Purpose:    Convert PDF to TXT format using the pdftotext utility

def convert_pdf_to_txt(pdfLoc, txtLoc):
    os.system("pdftotext -layout " + pdfLoc + " " + txtLoc)
    if os.path.isfile(txtLoc):
        if os.stat(txtLoc).st_size == 0:
            os.system("rm " + txtLoc)
    return

#Name:       clean_text
#Arguments:  line (line of text)
#Purpose:    Remove whitespace and convert some characters to spaces

def clean_text(line):
    l = line.lower()
    l = re.sub(r"[\f\n\r\t\v]+", "", l)
    l = re.sub(r"[^ a-z0-9\,\.\:\$\%\(\)\[\]\{\}-]+", " ", l)
    l = l.strip()
    return l

#Name:       get_text
#Arguments:  txtLoc (path of TXT file)
#Purpose:    Read in TXT file

def get_text(txtLoc):
    f = codecs.open(txtLoc, "rU", encoding="utf8")
    lines_clean = [clean_text(line) for line in f.readlines()]
    f.close()
    return lines_clean

#Name:       scrape_data_XX
#Arguments:  lines_clean (clean lines of text)
#            state
#            yyyy (4-digit year)
#            mm (2-digit month)
#Purpose:    Apply a template and scrape data from the PDF for state XX

#Alabama
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

#Alaska
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

#Arizona
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

#Arkansas
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

#California
def scrape_data_CA(lines_clean, state, yyyy, mm):
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

#Colorado
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

#Connecticut
def scrape_data_CT(lines_clean, state, yyyy, mm):
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

#Delaware
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

#Florida
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

#Georgia
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

#Hawaii
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

#Idaho
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

#Illinois
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

#Indiana
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

#Iowa
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

#Kansas
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

#Kentucky
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

#Louisiana
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

#Maine
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

#Maryland
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

#Massachusetts
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

#Michigan
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

#Minnesota
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

#Mississippi
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

#Missouri
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

#Montana
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

#Nebraska
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

#Nevada
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

#New Hampshire
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

#New Mexico
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

#New Jersey
def scrape_data_NJ(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    col = 3
    unit = "millions"
    time = "ytd"

    for line in lines_clean:
        if len(line) != 0:

            m_col = re.search(r"fy (\d{4})\s+fy (\d{4})", line)
            if m_col:
                if int(m_col.group(1)) > int(m_col.group(2)):
                    col = 2

            m_unit = re.search(r"\(\$ (thousands|millions|billions)\)", line)
            if m_unit:
                if m_unit.group(1) == "thousands":
                    unit = "thousands"
                elif m_unit.group(1) == "millions":
                    unit = "millions"
                elif m_unit.group(1) == "billions":
                    unit = "billions"

            m = re.search(r"(sales tax|sale tax)\s+\$?([\d\,\.]+)\s+\$?([\d\,\.]+)", line)
            if m:
                tax_types.append("sales")
                tax_values.append(m.group(col))
                tax_units.append(unit)
                tax_times.append(time)
            m = re.search(r"(gross income tax|gross income tax \(git\)|income tax)\s+\$?([\d\,\.]+)\s+\$?([\d\,\.]+)", line)
            if m:
                tax_types.append("individual income")
                tax_values.append(m.group(col))
                tax_units.append(unit)
                tax_times.append(time)
            m = re.search(r"(corp\. bus\. tax|corp\. bus\. tax \(cbt\)|corporation tax)\s+\$?([\d\,\.]+)\s+\$?([\d\,\.]+)", line)
            if m:
                tax_types.append("corporate income")
                tax_values.append(m.group(col))
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

#New York
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

#North Carolina
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

#North Dakota
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

#Ohio
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

#Oklahoma
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

#Oregon
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

#Pennsylvania
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

#Rhode Island
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

#South Carolina
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

#South Dakota
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

#Tennessee
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

#Texas
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

#Utah
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

#Vermont
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

#Virginia
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

#Washington
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

#West Virginia
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

#Wisconsin
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

#Wyoming
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

#Name:       create_output
#Arguments:  data (scraped data)
#            loc (path of output file)
#Purpose:    Create output TXT file containing scraped data

def create_output(data, loc):
    if len(data) > 0:
        f = codecs.open(loc, 'w', encoding="utf8")
        varbs = ["state", "year", "month", "tax_type", "tax_value", "tax_unit", "tax_time"]
        f.write("|".join(varbs) + "\n")
        for i in range(len(data)):
            f.write("|".join(data[i]) + "\n")
        f.close()
    return

#Name:       scrape_data
#Arguments:  projName (project name)
#            yyyy (4-digit year)
#            mm (2-digit month)
#Purpose:    Iterate through states and scrape data from previously downloaded PDFs

def scrape_data(projName, yyyy, mm):
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

    #List to store all of the scraped data
    prod = []
    prodLoc = "/" + projName + "/prod/" + yyyy + "_" + mm + ".txt"

    #List of states to loop through
    states = ["NJ"]
    statesDict = {"AL":"Alabama", "AK":"Alaska", "AZ":"Arizona", "AR":"Arkansas", "CA":"California",
        "CO":"Colorado", "CT":"Connecticut", "DE":"Delaware", "FL":"Florida", "GA":"Georgia",
        "HI":"Hawaii", "ID":"Idaho", "IL":"Illinois", "IN":"Indiana", "IA":"Iowa",
        "KS":"Kansas", "KY":"Kentucky", "LA":"Louisiana", "ME":"Maine", "MD":"Maryland",
        "MA":"Massachusetts", "MI":"Michigan", "MN":"Minnesota", "MS":"Mississippi", "MO":"Missouri",
        "MT":"Montana", "NE":"Nebraska", "NV":"Nevada", "NH":"New Hampshire", "NJ":"New Jersey",
        "New":"Mexico", "NY":"New York", "NC":"North Carolina", "ND":"North Dakota", "OH":"Ohio",
        "OK":"Oklahoma", "OR":"Oregon", "PA":"Pennsylvania", "RI":"Rhode Island", "SC":"South Carolina",
        "SD":"South Dakota", "TN":"Tennessee", "TX":"Texas", "UT":"Utah", "VT":"Vermont",
        "VA":"Virginia", "WA":"Washington", "WV":"West Virginia", "WI":"Wisconsin", "WY":"Wyoming"}

    for state in states:
        print_section(statesDict[state])
        docName = state + "_" + yyyy + "_" + mm
        pdfLoc = "/" + projName + "/pdf/" + docName + ".pdf"
        txtLoc = "/" + projName + "/txt/" + docName + ".txt"
        datLoc = "/" + projName + "/dat/" + docName + ".txt"

        if os.path.isfile(pdfLoc):
            print("PDF exists.")
        else:
            print("No PDF exists.")
            print("No intermediate TXT file created.")
            print("No output TXT file created.")

        if os.path.isfile(txtLoc):
            print("Intermediate TXT file already exists.")
        elif os.path.isfile(pdfLoc):
            convert_pdf_to_txt(pdfLoc, txtLoc)
            if os.path.isfile(txtLoc):
                print("Intermediate TXT file created.")
            else:
                print("No intermediate TXT file created.")
        
        if os.path.isfile(datLoc):
            print("Output TXT file already exists.  Removing ...")
            os.system("rm " + datLoc)
        if os.path.isfile(txtLoc):
            data = []
            lines_clean = get_text(txtLoc)
            if state == "AL":
                data = scrape.data_AL(lines_clean, state, yyyy, mm)
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
            else:
                print("No output TXT file created.")
    
    print_section("Product")
    if os.path.isfile(prodLoc):
        print("Product already exists.  Removing ...")
        os.system("rm " + prodLoc)
    create_output(prod, prodLoc)
    if os.path.isfile(prodLoc):
        print("Product created.")
    else:
        print("No product created.")
    
    print("")
    return

def main():
    #Check valid arguments
    if valid_arguments():
        scrape_data(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("\nInvalid arguments\n")
    return   

if __name__ == "__main__":
    main()
