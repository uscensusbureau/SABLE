# Name:        s2_convert.py
# Purpose:     Convert PDFs to TXT format
# Invocation:  python3 s2_convert.py <projName> <lng> <clss>

import codecs
import os
import re
import sys

# Name:        valid_arguments
# Purpose:     Check whether the command-line arguments are valid
# Parameters:  sys.argv (globally defined list of command-line arguments)
# Returns:     True (all arguments are valid) or False (at least one argument is invalid)

def valid_arguments():
    lngsValid = set(["danish", "dutch", "english", "finnish", "french", "german", "hungarian", "italian", "norwegian", "portuguese", "spanish", "swedish", "turkish"])
    clssesValid = set(["neg", "pos", "pred"])
    if len(sys.argv) == 4 and re.search(r"^[a-zA-Z][a-zA-Z_-]*$", sys.argv[1]) and sys.argv[2] in lngsValid and sys.argv[3] in clssesValid:
        return True
    return False

# Name:        match_page
# Purpose:     Match line to an XML page tag
# Parameters:  line (line of text from XML file)
# Returns:     Regular expression match object

def match_page(line):
    return re.search(r"<page id=\"(\d+)\"", line)

# Name:        match_textbox
# Purpose:     Match line to an XML textbox tag
# Parameters:  line (line of text from XML file)
# Returns:     Regular expression match object

def match_textbox(line):
    return re.search(r"<textbox id=\"(\d+)\"", line)

# Name:        match_textline
# Purpose:     Match line to an XML textline tag
# Parameters:  line (line of text from XML file)
# Returns:     Regular expression match object

def match_textline(line):
    return re.search(r"<textline", line)

# Name:        match_text
# Purpose:     Match line to an XML text tag
# Parameters:  line (line of text from XML file)
# Returns:     Regular expression match object

def match_text(line):
    return re.search(r"<text.*font=\"(.*)\".*bbox=\"([0-9]+\.[0-9]+),([0-9]+\.[0-9]+),([0-9]+\.[0-9]+),([0-9]+\.[0-9]+)\".*size=\"([0-9]+\.[0-9]+)\">(.*)</text>", line)

# Name:        clean_char
# Purpose:     Clean character to deal with punctuation, numbers, and foreign accent marks
# Parameters:  old (character)
# Returns:     Cleaned character

def clean_char(old):
    # Check the length of the argument
    if len(old) == 0:
        new = ""
    elif len(old) >= 2:
        new = " "
    else:
        # The function "ord" returns the integer representing the Unicode code point of a character
        ucp = ord(old)
        # Control codes
        if (0 <= ucp <= 31):
            new = " "
        # Punctuation
        elif (32 <= ucp <= 38) or (40 <= ucp <= 47) or (58 <= ucp <= 64) or (91 <= ucp <= 96) or (123 <= ucp <= 126) or ucp == 8221:
            new = " "
        # Apostrophe
        elif ucp == 39 or ucp == 8217:
            new = ""
        # Numbers
        elif (48 <= ucp <= 57):
            new = " "
        # Letters
        elif (192 <= ucp <= 198) or (224 <= ucp <= 230):
            new = "a"
        elif ucp == 199 or ucp == 231:
            new = "c"
        elif (200 <= ucp <= 203) or (232 <= ucp <= 235):
            new = "e"
        elif (204 <= ucp <= 207) or (236 <= ucp <= 239):
            new = "i"
        elif ucp == 209 or ucp == 241:
            new = "n"
        elif (210 <= ucp <= 214) or ucp == 216 or (242 <= ucp <= 246) or ucp == 248:
            new = "o"
        elif ucp == 223:
            new = "ss"
        elif (217 <= ucp <= 220) or (249 <= ucp <= 252):
            new = "u"
        elif ucp == 221 or ucp == 253 or ucp == 255:
            new = "y"
        elif ucp >= 128:
            new = " "
        else:
            new = old
    return new

# Name:        get_chars
# Purpose:     Extract the character values, coordinates, hierarchy, and font information from XML file
# Parameters:  xmlFile (location of XML file)
# Returns:     List of tuples (one for each character) containing character data

def get_chars(xmlFile):
    chars = []
    page = 0
    textbox = 0
    textline = 0
    
    # Open XML file and use regular expressions to parse contents
    f = codecs.open(xmlFile, "r", encoding="utf8")
    for l in f:
        line = l.strip()
        pageMatch = match_page(line)
        textboxMatch = match_textbox(line)
        textlineMatch = match_textline(line)
        textMatch = match_text(line)
        if pageMatch:
            page = int(pageMatch.group(1))
        elif textboxMatch:
            textline = 0
            textbox = int(textboxMatch.group(1))
        elif textlineMatch:
            textline += 1
        elif textMatch:
            font = textMatch.group(1)
            x1 = float(textMatch.group(2))
            y1 = float(textMatch.group(3))
            x2 = float(textMatch.group(4))
            y2 = float(textMatch.group(5))
            size = float(textMatch.group(6))
            value = clean_char(textMatch.group(7))
            chars.append((page, textbox, textline, x1, y1, x2, y2, size, font, value))
    f.close()
    return chars

# Name:        clean_text
# Purpose:     Clean string of text and check each word against a list of stop words
# Parameters:  text (string of text)
# Returns:     Cleaned text

def clean_text(text):
    text = text.lower()
    text = re.sub("\s+", " ", text)
    
    # Remove stop words
    textClean = []
    text = text.split(" ")
    global stopWords
    for word in text:
        word = word.strip()
        if word not in stopWords:
            textClean.append(word)
    textClean = " ".join(textClean)
    return textClean

# Name:        write_text
# Purpose:     Construct words character by character
# Parameters:  chars (list of tuples)
#              txtFile (location of TXT file)
# Returns:     

def write_text(chars, txtFile):
    text = []
    
    # Sort characters according to page, textbox, textline, y1, and x1
    chars = sorted(chars, key = lambda z: (z[0], z[1], z[2], -z[4], z[3]))
    pageCur = chars[0][0]
    textboxCur = chars[0][1]
    textlineCur = chars[0][2]

    for char in chars:
        spaceFlag = 0
        pageNew = char[0]
        textboxNew = char[1]
        textlineNew = char[2]
        if pageNew != pageCur:
            pageCur = pageNew
            spaceFlag = 1
        if textboxNew != textboxCur:
            textboxCur = textboxNew
            spaceFlag = 1
        if textlineNew != textlineCur:
            textlineCur = textlineNew
            spaceFlag = 1
        if spaceFlag == 1:
            text.append(" ")
        text.append(char[9])
    text = "".join(text)
    
    f = codecs.open(txtFile, "w")
    f.write(clean_text(text))
    f.close()
    return

# Name:        create_output
# Purpose:     Convert a PDF document of a given class to TXT format
# Parameters:  projName (project name)
#              clss ("pos" or "neg")
#              docName (document name)
# Returns:     

def create_output(projName, clss, docName):
    # Create file locations
    pdfFile  = "./{}/{}_pdf/{}.pdf".format(projName, clss, docName)
    xmlFile  = "./{}/{}_xml/{}.xml".format(projName, clss, docName)
    txtFile  = "./{}/{}_txt/{}.txt".format(projName, clss, docName)
    probFile = "./{}/{}_prob/{}.pdf".format(projName, clss, docName)

    # probFlag indicates whether there is a problem extracting text from the PDF
    # The problem PDFs are moved to separate folders where they can be inspected
    probFlag = 0
    chars = []

    # If the TXT file does not already exist, then try creating it
    if not os.path.isfile(txtFile):
        try:
            # The pdf2txt.py program comes with the PDFMiner module
            os.system("pdf2txt.py -o {} -t xml {}".format(xmlFile, pdfFile))
        except PDFTextExtractionNotAllowed:
            # Exception indicates that text cannot be extracted from the PDF
            probFlag = 1
        if not os.path.isfile(xmlFile):
            probFlag = 1
        elif os.stat(xmlFile).st_size == 0:
            probFlag = 1
        if probFlag == 0:
            chars = get_chars(xmlFile)
            if len(chars) == 0:
                probFlag = 1
        # Check probFlag value and act accordingly
        if probFlag == 0:
            write_text(chars, txtFile)
            if os.path.isfile(xmlFile):
                # The intermediate XML file is deleted because it tends to be large
                os.remove(xmlFile)
            print(docName)
        elif probFlag == 1:
            if os.path.isfile(xmlFile):
                # The intermediate XML file is deleted because it tends to be large
                os.remove(xmlFile)
            if os.path.isfile(txtFile):
                # Any text that has been extracted from the problem PDF is deleted
                os.remove(txtFile)
            os.system("mv {} {}".format(pdfFile, probFile))
            print("!!! PROBLEM: {}".format(docName))
    return

# Name:        convert_files
# Purpose:     Convert PDFs to TXT format
# Parameters:  projName (project name)
#              lng (language)
#              clss ("neg", "pos", or "pred")
# Returns:     

def convert_files(projName, lng, clss):
    # Read in stop words
    stopWordsList = []
    f = codecs.open("./stop_{}.txt".format(lng), "r")
    for word in f:
        if word.strip() != "":
            stopWordsList.append(word.strip())
    f.close()
    global stopWords
    stopWords = set(stopWordsList)

    # Iterate through PDFs of a given class, extract text, and create output files
    print("\n*****  {}  *****\n".format(clss))
    pdfs = sorted(os.listdir("./{}/{}_pdf".format(projName, clss)))
    for pdf in pdfs:
        pdfMatch = re.search(r"^(\S+)\.([pP][dD][fF])$", pdf)
        if pdfMatch:
            docName = pdfMatch.group(1)
            if pdfMatch.group(2) != "pdf":
                oldFile = "./{}/{}_pdf/{}.{}".format(projName, clss, docName, pdfMatch.group(2))
                newFile = "./{}/{}_pdf/{}.pdf".format(projName, clss, docName)
                os.system("mv {} {}".format(oldFile, newFile))
            create_output(projName, clss, docName)
    print("")
    return

def main():
    # Check valid arguments
    if valid_arguments():
        convert_files(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("\nInvalid arguments")
        print("Invocation:  python3 s2_convert.py <projName> <lng> <clss>\n")
    return

if __name__ == "__main__":
    main()
