"""
============================================================================
Name        : OO_personal_info.py
Author      : Seyed Ali Firooz Abadi
Version     : 1.0
Copyright   : copyright notice
Description : This class will create a district representative based on the information imported from 1st project
              I created a template dictionary, that if populated correctly (by a programmer, or anyone), this class can work with it
============================================================================
TODO :
    001-
    100- create a method to read a text file, then populate your template dictionary (using re library) so that you don't need to load unknown pickles (for security reasons)
============================================================================
"""

import pickle


class Person:
    # Private variable
    __STARTING_VALUE = "No data found"

    # --------------------------------------------------------------------------------
    # Constructor method

    def __init__(self, *filePath):
        # (if a file path hase been given to the constructor, it will load that district)

        # Initiating all variables with a default value
        self.__firstName = self.__STARTING_VALUE
        self.__middleName = self.__STARTING_VALUE
        self.__lastName = self.__STARTING_VALUE
        self.__homeAddress = self.__STARTING_VALUE
        self.__columbiaAddress = self.__STARTING_VALUE
        self.__phoneNum = self.__STARTING_VALUE
        self.__party = self.__STARTING_VALUE
        self.__county = self.__STARTING_VALUE
        self.__district = self.__STARTING_VALUE
        self.__personalInfo = self.__STARTING_VALUE
        self.__committeeAssignments = self.__STARTING_VALUE
        self.__serviceTime = self.__STARTING_VALUE

        if len(filePath) == 0:
            try:
                # Giving the variables there real values
                self.__firstName = self.__import_district78()["Full_Name"][0]
                self.__middleName = self.__import_district78()["Full_Name"][1]
                self.__lastName = self.__import_district78()["Full_Name"][2]
                self.__homeAddress = self.__import_district78()["Home_Address"]
                self.__columbiaAddress = self.__import_district78()["Columbia_Address"]
                self.__phoneNum = self.__import_district78()["Phone_Number"]
                self.__party = self.__import_district78()["Party"]
                self.__county = self.__import_district78()["County"]
                self.__district = self.__import_district78()["District"]
                self.__personalInfo = self.__import_district78()["Personal_Info"]
                self.__committeeAssignments = self.__import_district78()["Committee_Assignments"]
                self.__serviceTime = self.__import_district78()["Service_Time"]
            except:
                raise Exception("Some problems happened when reading the data, but I tried my best")

        elif len(filePath) == 1:
            try:
                # Giving the variables there real values
                self.__firstName = self.__import_district(filePath)["Full_Name"][0]
                self.__middleName = self.__import_district(filePath)["Full_Name"][1]
                self.__lastName = self.__import_district(filePath)["Full_Name"][2]
                self.__homeAddress = self.__import_district(filePath)["Home_Address"]
                self.__columbiaAddress = self.__import_district(filePath)["Columbia_Address"]
                self.__phoneNum = self.__import_district(filePath)["Phone_Number"]
                self.__party = self.__import_district(filePath)["Party"]
                self.__county = self.__import_district(filePath)["County"]
                self.__district = self.__import_district(filePath)["District"]
                self.__personalInfo = self.__import_district(filePath)["Personal_Info"]
                self.__committeeAssignments = self.__import_district(filePath)["Committee_Assignments"]
                self.__serviceTime = self.__import_district(filePath)["Service_Time"]
            except:
                raise Exception("The path you provided didn't work, please try again")

        else:
            raise Exception("You must enter only one string that has your pickle file path")

    # --------------------------------------------------------------------------------
    # loading the pickle

    @staticmethod
    def __import_district78():
        # Getting the raw data of project01
        try:
            file = open("../../Project01 - Extractor/data/processedData.pickle", "rb")
        except:
            file = open("../data/processedData.pickle", "rb")
        processed_Data_Dic = pickle.load(file)
        file.close()
        return processed_Data_Dic

    def __import_district(self, aPath):
        # Getting the raw data of project01
        file = open(aPath, "rb")
        processed_Data_Dic = pickle.load(file)
        file.close()
        if len(processed_Data_Dic["Full_Name"])==0 :
            raise Exception("The file path provided is wrong")
        return processed_Data_Dic

    # Requesting singular piece of information
    def infoAtIndex(self, i):
        try:
            i = int(i)
            key_list = list(self.__import_district78())
            j = key_list[i]
            return self.__import_district78()[j]
        except:
            return None

    # --------------------------------------------------------------------------------
    # pickling a class object

    def exportToPickle(self, districtNumber, classObject):

        pickleFileName = str("../data/person" + str(districtNumber) + ".pickle")

        with open(pickleFileName, "wb") as pickle_out:
            pickle.dump(classObject, pickle_out)

    # --------------------------------------------------------------------------------
    # Getters

    @property
    def firstName(self):
        return self.__firstName

    @property
    def middleName(self):
        return self.__middleName

    @property
    def lastName(self):
        return self.__lastName

    @property
    def fullName(self):
        return self.firstName + " " + self.middleName + " " + self.lastName

    @property
    def homeAddress(self):
        return self.__homeAddress

    @property
    def columbiaAddress(self):
        return self.__columbiaAddress

    @property
    def phoneNum(self):
        return self.__phoneNum

    @property
    def party(self):
        return self.__party

    @property
    def county(self):
        return self.__county

    @property
    def district(self):
        return self.__district

    @property
    def personalInfo(self):
        return self.__personalInfo

    @property
    def committeeAssignments(self):
        return self.__committeeAssignments

    @property
    def serviceTime(self):
        return self.__serviceTime

    # --------------------------------------------------------------------------------
