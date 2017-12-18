#Name:            classify_convert.py
#Purpose:         Convert PDFs in the /data/pos_pdf/ and /data/neg_pdf/ folders to TXT format for use with classify_model.py
#Data Layout:     See README.md
#Python Version:  2

import codecs
import os
import re
import string

#Name:       match_page
#Arguments:  line (line of text from XML file)
#Purpose:    Match line to an XML page tag

def match_page(line):
    return re.search(r"<page id=\"(\d+)\"", line)

#Name:       match_textbox
#Arguments:  line (line of text from XML file)
#Purpose:    Match line to an XML textbox tag

def match_textbox(line):
    return re.search(r"<textbox id=\"(\d+)\"", line)

#Name:       match_textline
#Arguments:  line (line of text from XML file)
#Purpose:    Match line to an XML textline tag

def match_textline(line):
    return re.search(r"<textline", line)

#Name:       match_text
#Arguments:  line (line of text from XML file)
#Purpose:    Match line to an XML text tag

def match_text(line):
    return re.search(r"<text.*font=\"(.*)\".*bbox=\"([0-9]+\.[0-9]+),([0-9]+\.[0-9]+),([0-9]+\.[0-9]+),([0-9]+\.[0-9]+)\".*size=\"([0-9]+\.[0-9]+)\">(.*)</text>", line)

#Name:       clean_char
#Arguments:  old (character)
#Purpose:    Clean character to deal with punctuation, numbers, and foreign accent marks

def clean_char(old):
    #Check the length of the argument
    if len(old) == 0:
        new = ""
    elif len(old) >= 2:
        new = " "
    #Apostrophe
    elif old == "'":
        new = ""
    #Other punctuation
    elif old in string.punctuation:
        new = " "
    #Numbers
    elif old in "0123456789":
        new = " "
    else:
        #The function "ord" returns the integer representing the Unicode code point of a character
        ucp = ord(old)
        if (192 <= ucp <= 198) or (224 <= ucp <= 230):
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

#Name:       get_chars
#Arguments:  xmlfile (location of XML file)
#Purpose:    Extract the character values, coordinates, hierarchy, and font information from XML file

def get_chars(xmlfile):
    chars = []
    page = 0
    textbox = 0
    textline = 0
    
    #Open XML file and use regular expressions to parse contents
    f = codecs.open(xmlfile, "rU", encoding="utf8")
    for l in f:
        line = l.strip()
        pagematch = match_page(line)
        textboxmatch = match_textbox(line)
        textlinematch = match_textline(line)
        textmatch = match_text(line)
        if pagematch:
            page = int(pagematch.group(1))
        elif textboxmatch:
            textline = 0
            textbox = int(textboxmatch.group(1))
        elif textlinematch:
            textline += 1
        elif textmatch:
            font = textmatch.group(1)
            x1 = float(textmatch.group(2))
            y1 = float(textmatch.group(3))
            x2 = float(textmatch.group(4))
            y2 = float(textmatch.group(5))
            size = float(textmatch.group(6))
            value = clean_char(textmatch.group(7))
            chars.append((page, textbox, textline, x1, y1, x2, y2, size, font, value))
    f.close()
    return chars

#Name:       clean_text
#Arguments:  text (string of text)
#Purpose:    Clean string of text and check each word against a list of stop words

def clean_text(text):
    text = text.lower()
    text = re.sub("\s+", " ", text)
    
    #Remove stop words
    text_clean = []
    text = text.split(" ")
    global stop_words
    for word in text:
        word = word.strip()
        if word not in stop_words:
            text_clean.append(word)
    text_clean = " ".join(text_clean)
    return text_clean

#Name:       write_text
#Arguments:  chars (list of tuples)
#            txtfile (location of TXT file)
#Purpose:    Construct words character by character

def write_text(chars, txtfile):
    text = []
    
    #Sort characters according to page, textbox, textline, y1, and x1
    chars = sorted(chars, key = lambda z: (z[0], z[1], z[2], -z[4], z[3]))
    page_cur = chars[0][0]
    textbox_cur = chars[0][1]
    textline_cur = chars[0][2]

    for char in chars:
        space_flag = 0
        page_new = char[0]
        textbox_new = char[1]
        textline_new = char[2]
        if page_new != page_cur:
            page_cur = page_new
            space_flag = 1
        if textbox_new != textbox_cur:
            textbox_cur = textbox_new
            space_flag = 1
        if textline_new != textline_cur:
            textline_cur = textline_new
            space_flag = 1
        if space_flag == 1:
            text.append(" ")
        text.append(char[9])
    text = "".join(text)
    
    f = codecs.open(txtfile, "w")
    f.write(clean_text(text))
    f.close()
    return

#Name:       create_files
#Arguments:  clss ("pos" or "neg")
#            docname (document name)
#Purpose:    Convert a PDF document of a given class to TXT format

def create_files(clss, docname):
    #Create file locations
    pdffile  = "/data/" + clss + "_pdf/"  + docname + ".pdf"
    xmlfile  = "/data/" + clss + "_xml/"  + docname + ".xml"
    txtfile  = "/data/" + clss + "_txt/"  + docname + ".txt"
    probfile = "/data/" + clss + "_prob/" + docname + ".pdf"

    #prob_flag indicates whether there is a problem extracting text from the PDF
    #The problem PDFs are moved to the /data/pos_prob/ and /data/neg_prob/ folders where they can be inspected
    prob_flag = 0
    chars = []

    #If the TXT file does not already exist, then try creating it
    if not os.path.isfile(txtfile):
        try:
            #The pdf2txt.py program comes with the PDFMiner module
            os.system("pdf2txt.py -o " + xmlfile + " -t xml " + pdffile)
        except PDFTextExtractionNotAllowed:
            #Exception indicates that text cannot be extracted from the PDF
            prob_flag = 1
        if not os.path.isfile(xmlfile):
            prob_flag = 1
        elif os.stat(xmlfile).st_size == 0:
            prob_flag = 1
        if prob_flag == 0:
            chars = get_chars(xmlfile)
            if len(chars) == 0:
                prob_flag = 1
        #Check prob_flag value and act accordingly
        if prob_flag == 0:
            write_text(chars, txtfile)
            if os.path.isfile(xmlfile):
                #The intermediate XML file is deleted because it tends to be large
                os.remove(xmlfile)
            print(docname)
        elif prob_flag == 1:
            if os.path.isfile(xmlfile):
                #The intermediate XML file is deleted because it tends to be large
                os.remove(xmlfile)
            if os.path.isfile(txtfile):
                #Any text that has been extracted from the problem PDF is deleted
                os.remove(txtfile)
            os.system("mv " + pdffile + " " + probfile)
            print("!!! PROBLEM: " + docname)
    return

def main():
    #Language of PDFs (used to remove stop words)
    lng  = "english"
    #Class of PDFs ("pos" or "neg")
    clss = "pos"

    #Read in stop words
    stop_words_list = []
    f = codecs.open("stop_" + lng + ".txt", "rU")
    for word in f:
        if word.strip() != "":
            stop_words_list.append(word)
    f.close()
    global stop_words
    stop_words = set(stop_words_list)

    #Iterate through PDFs of a given class, extract text, and create output files
    print("\n*****  " + clss + "  *****\n")
    pdfs = sorted(os.listdir("/data/" + clss + "_pdf/"))
    for pdf in pdfs:
        pdfmatch = re.search(r"^(\S+)\.([pP][dD][fF])$", pdf)
        if pdfmatch:
            docname = pdfmatch.group(1)
            if pdfmatch.group(2) != "pdf":
                oldfile = "/data/" + clss + "_pdf/" + docname + "." + pdfmatch.group(2)
                newfile = "/data/" + clss + "_pdf/" + docname + ".pdf"
                os.system("mv " + oldfile + " " + newfile)
            create_files(clss, docname)
    print("")
    return

if __name__ == "__main__":
    main()
