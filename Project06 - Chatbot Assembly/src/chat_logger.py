"""
============================================================================
Name        : chat_logger.py
Author      : Seyed Ali Firooz Abadi
Version     : 1.0
Description : This class will contain methods to log chat and time to the project file. There is two outputs, a text file and a CSV
Copyright © 2022 Ali Firooz. All rights reserved.
============================================================================
"""


import datetime
from timeit import default_timer as timer
import sys
import csv
import os


class Logger(object):
    """
    Creates a class that will both print and log any output text.
    See https://stackoverflow.com/a/5916874 for original source code.
    Modified to add date and time as a serial num,
    adding your own file name prefix is also optional.
    """

    def __init__(self, *args):
        self.__startTime01 = timer()
        self.__endTime01 = 0
        self.question = "empty"
        self.__numOfQuestions = 0
        self.__numOfAnswers = 0

        dtime = datetime.datetime.now()
        self.__serial = str(dtime.year) + "." + \
                        str(dtime.month) + "." + \
                        str(dtime.day) + "_" + \
                        str(dtime.hour) + "." + \
                        str(dtime.minute) + "." + \
                        str(dtime.second) + "." + \
                        str(dtime.microsecond)
        self.__path = "../data/chat_sessions/"

        # checking if the folder exists
        if not os.path.exists(self.__path):
            os.makedirs(self.__path)

        if len(args) == 0:
            self.__original_std_out = sys.stdout
            self.__filename = self.__path + self.__serial
            try:
                self.__log = open(self.__filename + '.txt', "a")
            except:
                print("seek help, couldn't save your session as a text")

        else:
            serial = str(args[0]) + "_" + self.__serial
            self.__original_std_out = sys.stdout
            self.__filename = self.__path + serial
            try:
                self.__log = open(self.__filename + '.txt', "a")
            except:
                print("seek help, couldn't save your session log as a text")

    def write(self, message, *args):
        self.__numOfAnswers += 1
        self.__original_std_out.write(message)

        # TODO uncomment this to log real time to file with user input
        #  args = [True]

        if len(args) != 0:
            self.__writeTime()
        self.__log.write(message)

    def __writeTime(self):
        self.__log.write("\n=====================\n")
        self.__log.write(str(datetime.datetime.now()))
        self.__log.write("\n")

    def flush(self):
        pass

    def loggedInput(self):
        self.__numOfQuestions += 1
        userInput = str(input(self.question))
        self.__log.write(">>> " + userInput + "\n")
        return userInput

    def writeCSV(self):
        self.__endTime01 = timer()
        processTime = round(self.__endTime01 - self.__startTime01)  # in sec

        self.__numOfQuestions -= 2
        if self.__numOfQuestions < 0:
            self.__numOfQuestions = 0

        self.__numOfAnswers -= (9 + self.__numOfQuestions)
        if self.__numOfAnswers < 0:
            self.__numOfAnswers = 0

        rowName = ['Serial Number', 'Number of user Questions', 'Number of system answers', 'Process time (sec)']
        row = [self.__serial, self.__numOfQuestions, self.__numOfAnswers, processTime]
        fileName = "../data/chat_statistics.csv"
        writeData = False
        try:
            # checking if the first line / file does exist
            try:
                with open(fileName, 'r') as tempFile:
                    reader = csv.reader(tempFile)
                    firstLine = []
                    for line in reader:
                        firstLine.append(str(line))
                        break
                    if firstLine[0] != str(rowName):
                        writeData = True

            # if file don't exist
            except:
                writeData = True

            # writing down the first line if needed
            finally:
                if writeData:
                    with open(fileName, 'w') as firstLineFile:
                        writer = csv.writer(firstLineFile)
                        writer.writerow(rowName)

            # writing the data to file
            with open(fileName, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(row)

        except:
            print("couldn't write statistics, a problem accrued")
