#!/usr/bin/env python
from subprocess import call
import os
import urllib
import urllib2
import pdfminer
import pdf2txt
import os.path
import convert_pdf_to_html

def Get_All_Trains():
        Train_List = ['1','2','3','4','5','6','7','A','C','E','B','D','F','M','G','J','Z','N','Q','R','L']
        PDF_Train_List = ['1','2','3','4','5','6','7','a','c','e','b','d','f','m','g','j','z','n','q','r','l']
        PDF_Names = ['{0}_train'.format(PDF_Train_List[i]) for i in range(len(PDF_Train_List))]
        for i in range(len(PDF_Train_List)):
                if os.path.isfile("C:\Users\Owner\Documents\Python\SampleTrainPDF\{0}_train.pdf".format(PDF_Train_List[i])) == False:
                        Find_Train_Original(PDF_Train_List[i])
                Pdf_to_text(PDF_Names[i])
        Run_To_HTML()
                                        
def Pdf_to_text(PDF):
        if os.path.isfile("C:\Users\Owner\Documents\Python\PDFOutputs\{0}.txt".format(PDF)) == False:
                call("python pdf2txt.py -o C:\Users\Owner\Documents\Python\PDFOutputs\{0}.txt C:\Users\Owner\Documents\Python\SampleTrainPDF\{0}.pdf".format(PDF))
                
def Find_Train_Original(Train):
	Train_req = urllib.urlretrieve('http://web.mta.info/nyct/service/pdf/t{0}cur.pdf'.format(Train), "C:\Users\Owner\Documents\Python\SampleTrainPDF\{0}_train.pdf".format(Train))
	return '{0}_train'.format(Train)

def Find_Sort_Correct_Times(train_name):
        trainopen = open('C:\Users\Owner\Documents\Python\PDFOutputs\{0}'.format(train_name), 'r')

def Run_To_HTML():
        for i in range(len(PDF_Names)):
                if os.path.isfile("C:\\Users\\Owner\\Documents\\Python\\PDFOutputsHTML\\{0}".format(PDF_Names[i])) == False:
                        convert_pdf_to_html.convert_pdf_to_html("C:\\Users\\Owner\\Documents\\Python\\SampleTrainPDF\\{0}_train.pdf".format(PDF_Names[i]), "C:\\Users\\Owner\\Documents\\Python\\PDFOutputsHTML\\{0}_train.html".format(PDF_Names[i]))

def Establish_Timetable():
        Get_All_Trains()

if __name__ == "__main__":
        Get_All_Trains()
        Run_To_HTML
