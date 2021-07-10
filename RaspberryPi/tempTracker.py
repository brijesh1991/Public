#!/usr/bin/python3
import os
from time import sleep
from subprocess import Popen, PIPE
import re
from datetime import datetime
import csv
import threading
import plotter

csvname = "reading.csv"
logname = "reading.txt"
indexArray = list()
tempArray = list()

def fileWrite(index, time, temp):
    txt_file =open(logname,"a")
    txt_file.write("{} {} {}\n".format(index, time, temp))
    txt_file.close()


def csvWrite(index, time, temp):
    with open(csvname,"a") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([index, time, temp])


def getClockFreq():
    '''

    '''
    cmd = Popen('vcgencmd measure_clock arm', shell=True, stdout = PIPE)
    for i in cmd.stdout:
        s= i.decode('UTF-8')
        temp = re.search(r'[0-9]{3,10}',s).group(0)
    freq_str = str(temp)
    stlen =len(freq_str)
    freq = int(freq_str[:-6])
    print("reading {} {} Mhz".format(temp,int(freq)))

def getTemp():
    '''

    '''
    cmd = Popen('vcgencmd measure_temp', shell=True, stdout = PIPE)

    for j in cmd.stdout:
        s = j.decode('UTF-8')
        temp =re.search(r'\d+(\.\d{1,2})?',s).group(0)
        print("Temp {}".format(temp))
    return (temp)


def getMem():
    cmd = Popen('free', shell = True, stdout = PIPE)

    for i in cmd.stdout:
        s= i.decode('UTF-8')
        if "Mem:" in s :
            lst = re.findall(r'[0-9]+',s)
            #print(lst)
            return(lst[0:3])


def printer():
    i=0
    while 1:
        i+=1

        now = datetime.now()
        currentTime = now.strftime("%H:%M:%S")
        
        getClockFreq()
        temp =getTemp()
        print(getMem())   
        fileWrite(i,currentTime, temp)
        csvWrite(i,currentTime, temp)
        indexArray.append(i)
        tempArray.append(i)
        sleep(10)

if __name__  == "__main__":
    if os.path.exists(csvname):
        os.remove(csvname)
    if os.path.exists(logname):
        os.remove(logname)

    t1 = threading.Thread(target =printer, name='plotter')
    
    t1.start()

    plotter.defPlotter()
