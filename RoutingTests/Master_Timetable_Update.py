#!/usr/bin/env python
from subprocess import call
import multiprocessing
import os
import urllib
import urllib2
import pdfminer
import pdf2txt
import os.path
import convert_pdf_to_html
import re
import time
import pickle


Train_List = ['1','2','3','4','5','6','7','A','C','E','B','D','F','M','G','J','Z','N','Q','R','L']
PDF_Train_List = ['1','2','3','4','5','6','7','a','c','e','b','d','f','m','g','j','j','n','q','r','l']
PDF_Names = ['{0}_train'.format(PDF_Train_List[i]) for i in range(len(PDF_Train_List))]



                        
                                        
def Pdf_to_text(PDF):
        if os.path.isfile("C:\\Users\\Owner\\Documents\\Python\\PDFOutputs\\{0}.txt".format(PDF)) == False:
                call("python pdf2txt.py -o C:\\Users\\Owner\\Documents\\Python\\PDFOutputs\\{0}.txt C:\\Users\\Owner\\Documents\\Python\\SampleTrainPDF\\{0}.pdf".format(PDF))
        return  
def Find_Train_Original(Train):
        Train_req = urllib.urlretrieve('http://web.mta.info/nyct/service/pdf/t{0}cur.pdf'.format(Train), "C:\\Users\\Owner\\Documents\\Python\\SampleTrainPDF\\{0}_train.pdf".format(Train))
        return 

def Find_Sort_Correct_Times(train_name):
        trainopen = open('C:\\Users\\Owner\\Documents\\Python\\PDFOutputs\\{0}'.format(train_name), 'r')
        return

def Run_To_HTML(List):
        for i in range(len(List)):
                if os.path.isfile("C:\\Users\\Owner\\Documents\\Python\\PDFOutputsHTML\\{0}".format(List[i])) == False:
                        convert_pdf_to_html.convert_pdf_to_html("C:\\Users\\Owner\\Documents\\Python\\SampleTrainPDF\\{0}.pdf".format(List[i]), "C:\\Users\\Owner\\Documents\\Python\\PDFOutputsHTML\\{0}.html".format(List[i]))
##                        print i
##                        print List[i]
##                        print "C:\\Users\\Owner\\Documents\\Python\\SampleTrainPDF\\{0}.pdf".format(List[i])
        return


def Time_To_Train_Stop(Train):
        Zero_Time = '00:00'
        Raw_table = []
        Train_table = []
        Stop_Ordering = []
        Stop_Names =set()
        with open("C:\\Users\\Owner\\Documents\\Python\\HTML_Revisions\\{0}.html".format(Train+'_train'), 'r+') as TimeTable:
                linecount = 0
                Lines = TimeTable.readlines()
                for line in Lines:
##                        if linecount == 1000:
##                                break
##                        linecount += 1
##                        if linecount > 29:
                        rest = re.search('(?<=[a-zA-z]\s)(.*)',line)
                        if rest == None:
                                NoStr = line.split("\r")
        ##                        print NoStr
        ##                        print NoStr[1].rstrip('\n')
                                
                                try:
                                        TheNoStr = NoStr[1].rstrip("\n")
                                except IndexError:
                                        TheNoStr = NoStr[0].rstrip(" ")
                                        pass
                                else:
                                        TheNoStr = NoStr[1].rstrip("\n")
        ##                                print TheNoStr
                                Quicklist = list(TheNoStr)
                                try:
                                        Quicklist[1]
                                except IndexError:
                                        pass
                                else:
                                        if Quicklist[0] == '1' and Quicklist[1] == ':':
                                                TheNoStr = '0'+TheNoStr
                                try:
                                        time.strptime(TheNoStr, '%I:%M')
                                except ValueError:
                                        try:
                                                int(Quicklist[0])
                                        except ValueError:
                                                Train_table.append(time.strptime(Zero_Time, '%H:%M'))
                                                Raw_table.append(Zero_Time)
                                        else:
                                                TheNoStrr = TheNoStr.rstrip('\n').lstrip('\r')
                                                Stop_Names.add(TheNoStrr)
                                                Stop_Ordering.append(TheNoStrr)
                                else:
                                        TIME = time.strptime(TheNoStr, '%I:%M')
                                        Train_table.append(TIME)
                                Raw_table.append(TheNoStr)
                        else:
                                date = rest.group()
        ##                                        print date
                                newgroup = date.split(" ")
                                try:
                                        time.strptime(newgroup[0], "%I:%M")
                                except ValueError:
                                        if re.search('tr001',line) == None:
                                                Line = line.rstrip('\n').lstrip('\r')
                                                Stop_Names.add(Line)
                                                Stop_Ordering.append(Line)
                                        else:
                                                pass
                                else:
                                        NEWTIME = time.strptime(newgroup[0], '%I:%M')
                                        Raw_table.append(newgroup[0])
                                        Train_table.append(NEWTIME)
#        print Stop_Names
#        print Stop_Ordering
#        print Raw_table
#        print Train_table
#        print len(Train_table)
#        print Train + ' ' + str(len(Train_table)) + ' ' + str(len(Stop_Names)) + ' ' + str(len(Stop_Ordering))
        return [Train_table, Stop_Names, Stop_Ordering]

def Strip_To_Times(Train_List):
        with open("C:\\Users\\Owner\\Documents\\Python\\PDFOutputsHTML\\{0}.html".format(Train_List), 'r') as train_op:
            #    CountEmUp = sum(1 for line in train_op.readlines())
           #     print CountEmUp
                train_op.seek(0,0)
                with open("C:\\Users\\Owner\\Documents\\Python\\HTML_Revisions\\{0}.html".format(Train_List), 'w') as train_revise:
                        for i in range(0,359):
                                train_op.readline()
                        for line in train_op.readlines():
                                if '<br>' in line and 'LightItalic' not in line:
                                        train_revise.write(line)
                        train_op.flush()
        with open("C:\\Users\\Owner\\Documents\\Python\\HTML_Revisions\\{0}.html".format(Train_List), 'r+') as Second_revision:
       #         Total_Lines = sum(1 for line in Second_revision)
      #          print Total_Lines
                Second_revision.seek(0,0)
                Count = 0
                lines = Second_revision.readlines()
        #        Second_revision.truncate(0)
                for line in lines:
                        Count += 1
                        if '<br>' in line:
                                if '</span>' not in line:
                                        Time = re.search('(?<=<br>)(.*)',line)
                                #        print Time.group()
                                #        Second_revision.seek(LineStart)
                                        Second_revision.write('\r'+'{0}'.format(Time.group())+'\n')
                                elif'</span>' in line:
                                        Data = re.search('(?<=px">)(.*)',line)
                                        if Data != None:
                                #                print Data.group()
                                #                Second_revision.seek(LineStart)
                                                Second_revision.write('\r'+'{0}'.format(Data.group())+'\n')
                                        elif Data == None:
                                #                Second_revision.seek(LineStart)
                                                Second_revision.write('\n')
                        else:
                                Second_revision.write(line)
                Second_revision.flush()
                Second_revision.close()
        with open("C:\\Users\\Owner\\Documents\\Python\\HTML_Revisions\\{0}.html".format(Train_List), 'r+') as Third_revision:
                Newlines = Third_revision.readlines()
                Third_revision.seek(0)
 #               Third_revision.truncate(0)
                for line in Newlines:
                        if '</span>' in line:
                                End = re.search('(?<=px">)(.*)',line)
                                if End != None:
                                        Third_revision.write('\r'+'{0}'.format(End.group())+'\n')
                else:
                        Third_revision.write(line)
                Third_revision.flush()
                os.fsync(Third_revision.fileno())
        return


def Make_Triple_dict(Train_name, Train_times, Stop_Names, Stop_Ordering):
        TrainName = {Train_name : {'{0}_Times'.format(Train_name) : Train_times, '{0}_Stops'.format(Train_name) : Stop_Names, '{0}_Ordering'.format(Train_name) : Stop_Ordering}}
        return TrainName
                
def Get_All_Trains():
        FINAL_List = []
        for i in range(len(PDF_Train_List)):
                if os.path.isfile("C:\\Users\\Owner\\Documents\\Python\\SampleTrainPDF\\{0}_train.pdf".format(PDF_Train_List[i])) == False:
                        Find_Train_Original(PDF_Train_List[i])
#                Pdf_to_text(PDF_Names[i])
        Run_To_HTML(PDF_Names)
        for i in range(len(PDF_Names)):
                Strip_To_Times(PDF_Names[i])
                List_Of_Things = Time_To_Train_Stop(PDF_Train_List[i])
                FINAL_List.append(Make_Triple_dict(Train_List[i], List_Of_Things[0], List_Of_Things[1], List_Of_Things[2]))
##                print FINAL_List
        return FINAL_List

## Once, if ever, this gets on to a server there needs to be a function which deletes the timetable every week-month or whenever the mta updates their timetables
                
def Check_for_Write():
        BigDict = Get_All_Trains()
        with open("C:\\Users\\Owner\\Documents\\Python\\Final_Dictionary\\Finale.txt", 'wb') as final_write:
                for i in range(len(BigDict)):
                        for j in range(len(BigDict[i]['{0}'.format(Train_List[i])]['{0}_Times'.format(Train_List[i])])):
                                final_write.write(str(BigDict[i]['{0}'.format(Train_List[i])]['{0}_Times'.format(Train_List[i])][j]))
##                        for j in range(len(BigDict[i]['{0}'.format(Train_List[i])]['{0}_Stops'.format(Train_List[i])])):
##                                final_write.write(str(BigDict[i]['{0}'.format(Train_List[i])]['{0}_Stops'.format(Train_List[i])][j]))
                        for j in range(len(BigDict[i]['{0}'.format(Train_List[i])]['{0}_Ordering'.format(Train_List[i])])):
                                final_write.write(str(BigDict[i]['{0}'.format(Train_List[i])]['{0}_Ordering'.format(Train_List[i])][j]))
        return
        
if __name__ == "__main__":
        Check_for_Write()
       
