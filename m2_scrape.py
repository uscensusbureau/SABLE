#Name:        m2_scrape.py
#Purpose:     Scrape specific tax revenue values from downloaded PDFs
#Invocation:  python3 m2_scrape.py <projName> <yyyy> <mm>

import codecs
import os
import re
import sys

#Name:        valid_arguments
#Purpose:     Check whether the command-line arguments are valid
#Parameters:  sys.argv (globally defined list of command-line arguments)
#Returns:     True (all arguments are valid) or False (at least one argument is invalid)

def valid_arguments():
    yearValid = [str(yyyy) for yyyy in range(2000, 2051)]
    monthValid = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    if len(sys.argv) == 4 and re.search(r"^[a-zA-Z][a-zA-Z_-]*$", sys.argv[1]) and sys.argv[2] in yearValid and sys.argv[3] in monthValid:
        return True
    return False

#Name:        print_section
#Purpose:     Print name of section
#Parameters:  section (section name)
#Returns:     

def print_section(section):
    n = len(section)
    print("")
    print("=" * (n + 12))
    print("===   {}   ===".format(section))
    print("=" * (n + 12))
    print("")
    return

#Name:        convert_pdf_to_txt
#Purpose:     Convert PDF to TXT format using the pdftotext utility
#Parameters:  pdfLoc (path of PDF)
#             txtLoc (path of TXT file)
#Returns:     

def convert_pdf_to_txt(pdfLoc, txtLoc):
    os.system("pdftotext -layout {} {}".format(pdfLoc, txtLoc))
    if os.path.isfile(txtLoc) and os.stat(txtLoc).st_size == 0:
        os.system("rm {}".format(txtLoc))
    return

#Name:        clean_text
#Purpose:     Remove whitespace and convert some characters to spaces
#Parameters:  line (line of text)
#Returns:     Cleaned line of text

def clean_text(line):
    l = line.lower()
    l = re.sub(r"[\f\n\r\t\v]+", "", l)
    l = re.sub(r"\xa0", " ", l)
    l = re.sub(u"\u2014", "-", l)
    l = re.sub(r"[^ a-z0-9,.!?:;$%&<>()[]{}/_=+-]+", " ", l)
    return l

#Name:        get_text
#Purpose:     Read in TXT file
#Parameters:  txtLoc (path of TXT file)
#Returns:     List of cleaned lines of text

def get_text(txtLoc):
    f = codecs.open(txtLoc, "r", encoding="utf8")
    lines_clean = [clean_text(line) for line in f.readlines()]
    f.close()
    return lines_clean

#Name:        clean_value
#Purpose:     Standardize negative tax value
#Parameters:  value (tax value)
#Returns:     Cleaned tax value

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

#Name:        scrape_data_XX
#Purpose:     Apply a template and scrape data from the PDF for state XX
#Parameters:  lines_clean (clean lines of text)
#             state
#             yyyy (4-digit year)
#             mm (2-digit month)
#Returns:     List of lists (one for each line item) containing scraped data

#Alabama
def scrape_data_AL(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    month_zone = False
    col = 1 
    unit = "dollars"
    time = "month"

    for line in lines_clean:
        if len(line) != 0:

            m_month = re.search(r"\S+\s+\S+\s+\S+\s+(january|february|march|april|may|june|july|august|september|october|november|december)\s+(january|february|march|april|may|june|july|august|september|october|november|december)", line)
            if m_month:
                month_zone = True

            m_col = re.search(r"\s+(\d{4})\s+(\d{4})", line) 
            if m_col and int(m_col.group(2)) > int(m_col.group(1)):
                col = 2

            if month_zone:

                m = re.search(r"bulk\s+storage\s+withdrawal\s+fee[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("bulk storage withdrawal fee")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"business\s+privilege\s+tax[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("business privilege tax")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"cmrs\s+wireless\s+911\s+service\s+charge[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("cmrs wireless 911 service charge")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"coal\s+severance\s+\(\$\.135/ton\)[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("coal severance ($.135/ton)")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"coal\s+severance\s+\(\$\.20/ton\)[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("coal severance ($.20/ton)")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"coal\s+severance\s+\(additional\)[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("coal severance (additional)")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"contractors'\s+gross\s+receipts[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("contractors gross receipts")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"deeds\s+and\s+assignments[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("deeds and assignments")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"dry\s+cleaning\s+registration fee[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("dry cleaning registration fee")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"estate\s+and\s+inheritance[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("estate and inheritance")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"financial\s+institutions\s+excise[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("financial institutions excise")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"forest\s+products\s+severance[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("forest products severance")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"freight\s+line\s+r.r.\s+equipment[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("freight line rr equipment")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"gasoline[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("gasoline")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"gasoline\s+\(aviation\s+(&|and)\s+jet\s+fuel\)[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("gasoline (aviation and jet fuel)")
                    tax_values.append(clean_value(m.group(col + 1)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"hazardous\s+waste[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("hazardous waste")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"hospital\s+assessment\s+fee[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("hospital assessment fee")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"hydro-electric\s+kwh[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("hydro-electric kwh")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"ifta\s+license\s+tax[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("ifta license tax")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"income\s+tax-corporate[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("income tax-corporate")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"income\s+tax-individual[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("income tax-individual")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"irp\s+registration\s+fees[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("irp registration fees")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"lodgings[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("lodgings")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"medicaid\s+nursing\s+facility[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("medicaid nursing facility")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"medicaid\s+pharm\.?\s+services[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("medicaid pharm services")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"miscellaneous\s+tags[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("miscellaneous tags")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"miscellaneous\s+taxes\*[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("miscellaneous taxes")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"mobile\s+telecom\s+tax[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("mobile telecom tax")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"motor\s+fuels\s+\(compressed/liquified\s+gas\)[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("motor fuels (compressed/liquified gas)")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"motor\s+fuels\s+\(diesel\)[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("motor fuels (diesel)")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"motor\s+registration\s+reinstate\s+fees[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("motor registration reinstate fees")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"motor\s+vehicle\s+title\s+fees[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("motor vehicle title fees")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"motor\s+veh\s+salv\s+inspec\s+fees[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("motor vehicle salv inspec fees")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"oil\s+&?\s+gas\s+privilege\s+\(8\%\)[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("oil and gas privilege (8%)")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"oil\s+(&|and)\s+gas\s+production\s+\(2\%\)[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("oil and gas production (2%)")
                    tax_values.append(clean_value(m.group(col + 1)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"oil\s+lubricating[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("oil lubricating")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"oil\s+wholesale\s+license[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("oil wholesale license")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"pari-mutuel\s+pool[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("pari-mutuel pool")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"petroleum\s+commodities\s+inspection\s+fee[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("petroleum commodities inspection fee")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"property\s+tax\**[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("property tax")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"rental\s+or\s+leasing[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("rental or leasing")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"sales[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("sales")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"scrap\s+tire\s+environmental\s+fee[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("scrap tire environmental fee")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"simplified\s+sellers\s+use\s+tax[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("simplified sellers use tax")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"solid\s+waste\s+disposal\s+fee[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("solid waste disposal fee")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"store\s+licenses[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("store licenses")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"tobacco\s+cigarette\s+tax[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("tobacco cigarette tax")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"tobacco\s+otp\s+tax[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("tobacco otp tax")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"use[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("use")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"utility\s+gross\s+receipts[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("utility gross receipts")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"utility\s+license\s+\(2.2\%\)[\s.]+(\(?[\d.,$]+\)?)", line)
                if m:
                    tax_types.append("utility license (2.2%)")
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

    rev_zone = False
    ref_zone = False
    indent_tct = 0
    indent_rec = 0
    line_tct = 0
    line_rec = 0
    line_num = 0
    col = 1
    unit = "dollars"
    time = "month"

    m_nn = False
    for line in lines_clean:
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
            m_table_totals = re.search(r"(totals|total\s+refunds)\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
            if m_table_totals:
                rev_zone = False
                ref_zone = False

            m_col1 = re.search(r"(type\s+of\s+revenue|type\s+of\s+refund)\s+(\d{4})\s+(\d{4})", line)
            m_col2 = re.search(r"tax\s+type\s+through\s+\S+\s+(\d{4})\s+through\s+\S+\s+(\d{4})", line)
 
            if m_col1 and int(m_col1.group(3)) > int(m_col1.group(2)):
                col = 2
            if m_col2 and int(m_col2.group(2)) > int(m_col2.group(1)):
                col = 2

            if rev_zone:

                m = re.search(r"withholding\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("withholding")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"estimates\s+and\s+finals\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("estimates and finals")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"sales\s+and\s+use\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("sales and use")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"room\s+occupancy\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("room occupancy")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"corporation\s+business\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("corporation business")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"pass-through\s+entity.\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("pass-through entity")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"unrelated\s+business\s+income\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("unrelated business income")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"cable,\s+satellite\s+and\s+video\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("cable satellite and video")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"peg\s+account\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("peg account")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"electric\s+&\s+power\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("electric and power")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"gas\s+companies\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("gas companies")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"railroads\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("railroads")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"estate\s+and\s+gift\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m and "estate and gift" not in tax_types:
                    tax_types.append("estate and gift")
                    tax_values.append(clean_value(m.group(col + 1)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"domestic\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("domestic")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"foreign\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("foreign")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"health\s+care\s+centers\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("health care centers")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m_nonadm = re.search(r"nonadmitted\s*/\s*unauthorized\s*/\s*", line)
                if m_nonadm:
                    m_nn = True
                m = re.search(r"\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m_nn and m:
                    m_nn = False
                    tax_types.append("nonadmitted unauthorized captive insurers")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"(alcoholic|alchoholic)\s+beverages\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("alcoholic beverages")
                    tax_values.append(clean_value(m.group(col + 1)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"cigarette\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("cigarette")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"electronic\s+cigarette\s+products\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("electronic cigarette products")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"tobacco\s+products\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("tobacco products")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"controlling\s+interest\s+transfer\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("controlling interest transfer")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"real\s+estate\s+conveyance\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m and "real estate conveyance" not in tax_types:
                    tax_types.append("real estate conveyance")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"petroleum\s+gross\s+earnings\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("petroleum gross earnings")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"admissions\s+&\s+dues\s+and\s+tnc\s+fee\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("admission and dues and tnc fee")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"dry\s+cleaners\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("dry cleaners")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"occupational\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("occupational")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"rental\s+surcharge\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("rental surcharge")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"solid\s+waste\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("solid waste")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"tourism\s+tax\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("tourism tax")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"controlled\s+substances\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("controlled substances")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"prepaid\s+wireless\s+e-?9-?1-?1\s+fee\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("prepaid wireless e911 fee")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"paid\s+preparer\s+fee\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("paid preparer fee")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"repealed\s+taxes\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("repealed taxes")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"nursing\s+home\s+user\s+fee\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("nursing home user fee")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"hospitals\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("hospitals")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"intermediate\s+care\s+facility\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("intermediate care facility")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"ambulatory\s+surgical\s+center\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("ambulatory surgical center")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"gasoline\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("gasoline")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"special\s+fuel\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("special fuel")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"motor\s+carrier\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("motor carrier")
                    tax_values.append(clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)

            if ref_zone:

                m = re.search(r"(income\s+tax\s+withholding|withholding)\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("withholding refund")
                    tax_values.append("-" + clean_value(m.group(col + 1)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"(income\s+tax|income\s+tax\s+finals\s+&\s+estimates)\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("income tax refund")
                    tax_values.append("-" + clean_value(m.group(col + 1)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"sales\s+and\s+use\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("sales and use refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"business\s+use\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("business use refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"room\s+occupancy\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("room occupancy refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"business\s+entity\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("business entity refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"corporation\s+business\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("corporation business refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"(r\s+&\s+d\s+credit\s+buybacks|corporation\s+r&d|corporation\s+r\s+&\s+d)\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("r and d credit buybacks refund")
                    tax_values.append("-" + clean_value(m.group(col + 1)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"unrelated\s+business\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("unrelated business refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"cable,?\s+satellite,?\s+and\s+video\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("cable satellite and video refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"electric\s+&\s+power\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("electric and power refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"gas\s+companies\s+([\d,.$-]+)\s+([\d,.$-]+)", line)
                if m:
                    tax_types.append("gas companies refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"estate\s+and\s+gift\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m and "estate and gift refund" not in tax_types:
                    tax_types.append("estate and gift refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"domestic\s+insurance\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("domestic insurance refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"foreign\s+(insurance|insurers)\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("foreign insurance refund")
                    tax_values.append("-" + clean_value(m.group(col + 1)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"(alcoholic|alchoholic)\s+beverages\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("alcoholic beverages refund")
                    tax_values.append("-" + clean_value(m.group(col + 1)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"(cigarette|cigarette\s+tax)\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("cigarette refund")
                    tax_values.append("-" + clean_value(m.group(col + 1)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"electronic\s+cigarette\s+products\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("electronic cigarette products refund")
                    tax_values.append("-" + clean_value(m.group(col + 1)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"tobacco\s+products\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("tobacco products refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"controlling\s+interest\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("controlling interest refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"real\s+estate\s+conveyance\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m and "real estate conveyance refund" not in tax_types:
                    tax_types.append("real estate conveyance refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"petroleum\s+gross\s+earnings\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("petroleum gross earnings refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"admissions\s+&\s+dues\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("admissions and dues refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"occupational\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("occupational refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"solid\s+waste\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("solid waste refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"(hospitals|hospital\s+net\s+revenue)\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("hospitals refund")
                    tax_values.append("-" + clean_value(m.group(col + 1)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"nursing\s+home\s+user\s+fee\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("nursing home user fee refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"gasoline\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("gasoline refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"special\s+fuel\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("special fuel refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"motor\s+carrier\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("motor carrier refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)
                m = re.search(r"miscellaneous\s+([\d,.()$-]+)\s+([\d,.()$-]+)", line)
                if m:
                    tax_types.append("miscellaneous refund")
                    tax_values.append("-" + clean_value(m.group(col)))
                    tax_units.append(unit)
                    tax_times.append(time)

    tax_types_sub, tax_values_sub, tax_times_sub, tax_units_sub = [], [], [], []
    tax_types2 = tax_types
    for tt in tax_types2:
        tt_r = tt + " refund"  
        idxB = tax_types.index(tt)
        unit_sub=tax_units[idxB]
        time_sub=tax_times[idxB]
        value_sub=tax_values[idxB]
        if tt_r in tax_types:
            idxA = tax_types.index(tt_r)
            value_sub = abs(float(value_sub.replace(",", ""))) - abs(float(tax_values[idxA].replace(",", "")))
        else:
            value_sub

        tax_types_sub.append(tt)
        tax_values_sub.append(str(value_sub))
        tax_times_sub.append(time_sub)
        tax_units_sub.append(unit_sub)

    for tt in range(len(tax_types_sub)):
        if "refund" in tax_types_sub[tt]:
            del tax_types_sub[tt:]
            del tax_values_sub[tt:]
            del tax_units_sub[tt:]
            del tax_times_sub[tt:]
            break

    tax_types, tax_values, tax_times, tax_units = tax_types_sub, tax_values_sub, tax_times_sub, tax_units_sub

    unique = {}
    for tt_idx in range(len(tax_types)):
        tax_type = tax_types[tt_idx]
        if tax_type not in unique:
            unique[tax_type] = tax_values[tt_idx]
        else:
            tax_types.pop(tt_idx)
            tax_values.pop(tt_idx)
    
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

#New Jersey
def scrape_data_NJ(lines_clean, state, yyyy, mm):
    data = []
    tax_types  = []
    tax_values = []
    tax_units  = []
    tax_times  = []

    col = 3
    unit = "millions"
    time = "ytd thru month"

    for line in lines_clean:
        if len(line) != 0:

            m_col = re.search(r"fy\s*(\d{4})\s+fy\s*(\d{4})", line)
            if m_col and int(m_col.group(1)) > int(m_col.group(2)):
                col = 2

            m_unit = re.search(r"\(\$\s*(dollars|thousands|millions|billions)\)", line)
            if m_unit:
                if m_unit.group(1) == "dollars":
                    unit = "dollars"
                elif m_unit.group(1) == "thousands":
                    unit = "thousands"
                elif m_unit.group(1) == "millions":
                    unit = "millions"
                elif m_unit.group(1) == "billions":
                    unit = "billions"

            m = re.search(r"(gross\s+income\s+tax|gross\s+income\s+tax\s+\(git\)|income tax)\s+([\d,.()$]+)\s+([\d,.()$]+)", line)
            if m:
                tax_types.append("gross income tax (git)")
                tax_values.append(clean_value(m.group(col)))
                tax_units.append(unit)
                tax_times.append(time)
            m = re.search(r"(sales\s+tax|sale\s+tax)\s+([\d,.()$]+)\s+([\d,.()$]+)", line)
            if m:
                tax_types.append("sales tax")
                tax_values.append(clean_value(m.group(col)))
                tax_units.append(unit)
                tax_times.append(time)
            m = re.search(r"(corp\.\s+bus\.\s+tax|corp\.\s+bus\.\s+tax\s+\(cbt\)|corporation\s+tax)\s+([\d,.()$]+)\s+([\d,.()$]+)", line)
            if m:
                tax_types.append("corporate business tax (cbt)")
                tax_values.append(clean_value(m.group(col)))
                tax_units.append(unit)
                tax_times.append(time)
            m = re.search(r"(petroleum\s+products)\s+([\d,.()$]+)\s+([\d,.()$]+)", line)
            if m:
                tax_types.append("petroleum products")
                tax_values.append(clean_value(m.group(col)))
                tax_units.append(unit)
                tax_times.append(time)
            m = re.search(r"(insurance\s+premium)\s+([\d,.()$]+)\s+([\d,.()$]+)", line)
            if m:
                tax_types.append("insurance premium")
                tax_values.append(clean_value(m.group(col)))
                tax_units.append(unit)
                tax_times.append(time)
            m = re.search(r"(motor\s+fuels)\s+([\d,.()$]+)\s+([\d,.()$]+)", line)
            if m:
                tax_types.append("motor fuels")
                tax_values.append(clean_value(m.group(col)))
                tax_units.append(unit)
                tax_times.append(time)
            m = re.search(r"(motor\s+vehicle\s+fees)\s+([\d,.()$]+)\s+([\d,.()$]+)", line)
            if m:
                tax_types.append("motor vehicle fees")
                tax_values.append(clean_value(m.group(col)))
                tax_units.append(unit)
                tax_times.append(time)
            m = re.search(r"(transfer\s+inheritance)\s+([\d,.()$]+)\s+([\d,.()$]+)", line)
            if m:
                tax_types.append("transfer inheritance")
                tax_values.append(clean_value(m.group(col)))
                tax_units.append(unit)
                tax_times.append(time)
            m = re.search(r"(realty\s+transfer)\s+([\d,.()$]+)\s+([\d,.()$]+)", line)
            if m:
                tax_types.append("realty transfer")
                tax_values.append(clean_value(m.group(col)))
                tax_units.append(unit)
                tax_times.append(time)
            m = re.search(r"(casino)\s+([\d,.()$]+)\s+([\d,.()$]+)", line)
            if m:
                tax_types.append("casino")
                tax_values.append(clean_value(m.group(col)))
                tax_units.append(unit)
                tax_times.append(time)
            m = re.search(r"(banks\s+&\s+financial|banks\s+&\s+financial\s+\(cbt\))\s+([\d,.()$]+)\s+([\d,.()$]+)", line)
            if m:
                tax_types.append("banks and financial (cbt)")
                tax_values.append(clean_value(m.group(col)))
                tax_units.append(unit)
                tax_times.append(time)
            m = re.search(r"(alcohol\s+excise)\s+([\d,.()$]+)\s+([\d,.()$]+)", line)
            if m:
                tax_types.append("alcohol excise")
                tax_values.append(clean_value(m.group(col)))
                tax_units.append(unit)
                tax_times.append(time)
            m = re.search(r"(cigarette)\s+([\d,.()$]+)\s+([\d,.()$]+)", line)
            if m:
                tax_types.append("cigarette")
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

#Name:        create_output
#Purpose:     Create output TXT file containing scraped data
#Parameters:  data (scraped data)
#             loc (path of output file)
#Returns:     

def create_output(data, loc):
    if len(data) > 0:
        f = codecs.open(loc, 'w', encoding="utf8")
        varbs = ["state", "year", "month", "tax_type", "tax_value", "tax_unit", "tax_time"]
        f.write("|".join(varbs) + "\n")
        for i in range(len(data)):
            f.write("|".join(data[i]) + "\n")
        f.close()
    return

#Name:        scrape_data
#Purpose:     Iterate through states and scrape data from previously downloaded PDFs
#Parameters:  projName (project name)
#             yyyy (4-digit year)
#             mm (2-digit month)
#Returns:     

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
    prodLoc = "/{}/prod/{}_{}.txt".format(projName, yyyy, mm)

    #List of states to loop through
    states = ["AL", "CT", "NJ"]
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
        print_section(statesDict[state])
        docName = "{}_{}_{}".format(state, yyyy, mm)
        pdfLoc = "/{}/pdf/{}.pdf".format(projName, docName)
        txtLoc = "/{}/txt/{}.txt".format(projName, docName)
        datLoc = "/{}/dat/{}.txt".format(projName, docName)

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
                print("Number of line items scraped: {}".format(len(data)))
            else:
                print("No output TXT file created.")
    
    print_section("Product")
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
    #Check valid arguments
    if valid_arguments():
        scrape_data(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("\nInvalid arguments\n")
    return   

if __name__ == "__main__":
    main()
