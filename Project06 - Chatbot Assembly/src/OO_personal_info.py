"""
============================================================================
Name        : OO_personal_info.py
Author      : Seyed Ali Firooz Abadi
Version     : 2.0
Description : Just a class to get the pickle to work, I also added the __repr__() method to return everything in a string
Copyright © 2022 Ali Firooz. All rights reserved.
============================================================================
TODO:
    - change the name of the file. Remove "info" at the end !
"""

import to_string as TS


class Person:

    def __repr__(self):
        allInfo: str
        allInfo = "\n--------------------------------------\n\n" \
                  "Full Name:\n" + \
                  self.fullName + \
                  "\n\n--------------------------------------\n\n" \
                  "County:\n" + \
                  self.county + \
                  "\n\n--------------------------------------\n\n" \
                  "Political Party:\n" + \
                  self.party + \
                  "\n\n--------------------------------------\n\n" \
                  "District:\n" + \
                  self.district + \
                  "\n\n--------------------------------------\n\n" + \
                   str("Home address:\n" + self.homeAddress + "\n\nColumbia address:\n" + self.columbiaAddress) + \
                  "\n\n--------------------------------------\n\n" \
                  "Phone Number:\n" + \
                  TS.toString_tap(self.phoneNum, 'and') + \
                  "\n\n--------------------------------------\n\n" \
                  "Personal Information:\n\n" + \
                  TS.toString_list(self.personalInfo) + \
                  "\n--------------------------------------\n\n" \
                  "Committee Assignments:\n" + \
                  TS.toString_space(self.committeeAssignments, 'and') + \
                  "\n\n--------------------------------------\n\n" \
                  "Service In Public Office:\n" + \
                  self.serviceTime + \
                  "\n\n--------------------------------------"

        return allInfo

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
