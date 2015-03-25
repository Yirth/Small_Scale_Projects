import time
import datetime
import re
import subprocess
import shlex
import matplotlib.pyplot as plt


## TO DO:
## do a regex thing and find each pin and then its registered ram that it is taking up.
## Then using a graphing module to spit out a graph or something that looks nice graphing it's change over time.
## Maybe: add a multiprocess thread which updates the graph indefinitely or something like that.
##
## There is going to be weird stuff if the milliseconds are on 000 or if the seconds contain a 00 i think
## And especially if the seconds are turning over into the minute


class task_graph:
## > C:\Users\Owner\Documents\Python\Tasks\Data\{1}.txt'.format(self.Prog+'.exe', self.Prog)
    def __init__(self):
        self.Prog = raw_input("What is the name of the program you want to watch? (No .exe extension)")

    def call_every(self):
        tme = raw_input("Please input the time for which you would like to evaluate the program for. (Minutes:Seconds)")
        Te = time.gmtime()
        try:
            time.strptime(tme, "%M:%S")
        except ValueError:
            print "This was not a correct input. Please recall the program to try again"
            return
        else:
            tme = time.strptime(tme, "%M:%S")
        TeList = eval(time.strftime("[%M,%S]", Te))
        Original_Sec = TeList[0]*60+TeList[1]
        Original_Sec_Dummy = Original_Sec
        EndTeList = eval(time.strftime("[%M,%S]", tme))
        End_Sec = EndTeList[0]*60 + EndTeList[1]
        Tot_End_Sec = Original_Sec +End_Sec
        wipefile = open(r'C:\Users\Owner\Documents\Python\Tasks\Data\task_data_{0}.txt'.format(self.Prog), 'w')
        wipefile.close()
        transfer = open(r'C:\Users\Owner\Documents\Python\Tasks\Data\{0}.txt'.format(self.Prog), 'w')
##        echo_off = r'echo off'
##        subargs = shlex.split(echo_off)
##        subprocess.Popen(subargs)
        transfer.close()
        while Original_Sec_Dummy <= Tot_End_Sec:
            Original_Sec_Dummy = Original_Sec_Dummy +1
            command = r'tasklist /fi "imagename eq {0}"'.format(self.Prog+'.exe')
            args = shlex.split(command)
            comm = subprocess.Popen(args, stdout=subprocess.PIPE)
            Output = comm.communicate()[0]
            with open('C:\Users\Owner\Documents\Python\Tasks\Data\{0}.txt'.format( self.Prog), 'w') as wri:
                wri.write(Output)
            with open(r'C:\Users\Owner\Documents\Python\Tasks\Data\task_data_{0}.txt'.format(self.Prog), 'a') as data_file:
                with open(r'C:\Users\Owner\Documents\Python\Tasks\Data\{0}.txt'.format(self.Prog), 'r') as infile:
                    data_file.write(datetime.datetime.utcnow().strftime("%H:%M:%S.%f")+'\n')
                    for line in infile:
                        data_file.write(line)
            time.sleep(1)
        return r'C:\Users\Owner\Documents\Python\Tasks\Data\task_data_{0}.txt'.format(self.Prog)
        
    def organize_data(self, file):
        TimeList = []
        BigPIDList = []
        BigMemList = []
        PIDList = []
        MemList = []
        with open(file, 'r') as data:
            lines = data.readlines()
            for line in lines:
                LineList = re.split('(\W+)', line)## regex search on the line?
                if re.search('=', line) != None:# if the line is not the equal sign then do the things. If it is the equal sign then save the Memlist to BigMemList, and PIDList to BigPIDList and then make a new list
                    BigPIDList.append(PIDList)
                    BigMemList.append(MemList)
                    PIDList = []
                    MemList = []
                else:
                    try:
                        eval(LineList[0])
                    except (SyntaxError, NameError):
                        if LineList[0] == self.Prog:# line begins with self.Prog.exe
                            #print LineList
                            NumLineList = re.split('(\W+)', line)
                            PID = NumLineList[4]
                            PIDList.append(PID)
                            try:
                                eval(NumLineList[(len(NumLineList)-7)])
                            except SyntaxError:
                                KiloBytes = eval(NumLineList[(len(NumLineList)-5)])
                            else:
                                if list(NumLineList[(len(NumLineList)-5)])[0] == '0':
                                    RidZeroList = list(NumLineList[(len(NumLineList)-5)])
                                    NumLineList.pop((len(NumLineList)-5))
                                    NumLineList.insert((len(NumLineList)-4), RidZeroList[1]+RidZeroList[2])
                                    #print NumLineList
                                if list(NumLineList[(len(NumLineList)-7)])[0] == '0':
                                    RidFirstZeroList = list(NumLineList[(len(NumLineList)-7)])
                                    NumLineList.pop((len(NumLineList-7)))
                                    try:
                                        RidFirstZeroList[2]
                                    except IndexError:
                                        NumLineList.insert((len(NumLineList)-6), RidFirstZeroList[1])
                                    else:
                                        NumLineList.insert((len(NumLineList)-6), RidFirstZeroList[1]+RidFirstZeroList[2])
                                try:
                                    eval(NumLineList[(len(NumLineList)-7)])
                                except SyntaxError:
                                    RidFirstZeroList = list(NumLineList[(len(NumLineList)-7)])
                                    NumLineList.pop((len(NumLineList-7)))
                                    try:
                                        RidFirstZeroList[2]
                                    except IndexError:
                                        NumLineList.insert((len(NumLineList)-6), RidFirstZeroList[1])
                                    else:
                                        NumLineList.insert((len(NumLineList)-6), RidFirstZeroList[1]+RidFirstZeroList[2])
                                try:
                                    eval(NumLineList[(len(NumLineList)-5)])
                                except SyntaxError:
                                    RidZeroList = list(NumLineList[(len(NumLineList)-5)])
                                    NumLineList.pop((len(NumLineList)-5))
                                    try:
                                        RidZeroList[2]
                                    except IndexError:
                                        NumLineList.insert((len(NumLineList)-4), RidZeroList[1])
                                    else:
                                        NumLineList.insert((len(NumLineList)-4), RidZeroList[1]+RidZeroList[2])
                                KiloBytes = eval(NumLineList[(len(NumLineList)-7)])*1000 + eval(NumLineList[(len(NumLineList)-5)])
                            MegaBytes = KiloBytes*(1/float(1024))
                            MemList.append(MegaBytes)
                    else:
                            if type(eval(LineList[0])) == int:# line begins with hour:minute:second.microsecond
                                                                                    TimeString = LineList[4]+LineList[5]+LineList[6]
                                                                                    TimeInt = eval(TimeString)
                                                                                    #print TimeInt
                                                                                    TimeList.append(TimeInt)

                # else: if nothing else happens we don't need to worry about shit
        return TimeList, BigPIDList, BigMemList

    def make_graph(self, TimeList, PIDList, MemList):
        BigNewMemList = []
        NewMemList = []
        for j in range(0, len(PIDList[(len(PIDList)-1)])):
            BigNewMemList.append(NewMemList)
            NewMemList = [MemList[1][j]]
            for i in range(1, len(MemList)):
                NewMemList.append(MemList[i][j])
        BigNewMemList.pop(0)
        plt.axis([TimeList[0], TimeList[(len(TimeList)-1)], 0, 150])
        for i in range(0, len(BigNewMemList)):
            plt.plot(TimeList, BigNewMemList[i])
            plt.plot(TimeList, BigNewMemList[i], 'o')

        plt.show()
            
if __name__ == "__main__":
    X = task_graph()
    print X.Prog
    X.call_every()
    Data = X.organize_data(r'C:\Users\Owner\Documents\Python\Tasks\Data\task_data_{0}.txt'.format(X.Prog))
    X.make_graph(Data[0], Data[1], Data[2])
