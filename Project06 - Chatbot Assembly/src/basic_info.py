"""
============================================================================
Name        : basic_info.py
Author      : Seyed Ali Firooz Abadi
Version     : 2.0
Description : This class is responsible to answer everything about person's name, address, phone number. This is a copy of Assignment 03.
Copyright © 2022 Ali Firooz. All rights reserved.
============================================================================
"""

import abstract_chat_class as acc
import to_string as TS
import query_matching as qm


class BasicInfo(acc.AbstractInfoManager):

    __firstName = ['firstname']
    __middleName = ['middlename']
    __lastName = ['lastname']
    __fullName = ['full name', 'fullname', 'name', 'who is my rep', 'who is my repo', 'who is my representative', 'what is the name']

    __trainingList_name = [__firstName, __middleName, __lastName, __fullName]

    # ----------------------------------------------------------------------------

    __fullAddress = ['full address', 'live', 'lives', 'address', 'what is the address']
    __homeAddress = ['home address', 'home address', 'home']
    __columbiaAddress = ['columbia address', 'columbiaaddress']

    __trainingList_address = [__homeAddress, __columbiaAddress, __fullAddress]

    # ----------------------------------------------------------------------------
    __phoneNumber = ['phone', 'phonenumber', 'contact', 'call', 'phone number', 'what is the phone number']

    __trainingList_phone = [__phoneNumber]

    # ----------------------------------------------------------------------------

    __trainingList = [__trainingList_name, __trainingList_address, __trainingList_phone]
    __strTrainingList = ['name', 'address', 'phone number']

    # ----------------------------------------------------------------------------

    def basicCheck(self, question, classObject):
        match = qm.QueryMatching()
        ansIndex = match.fuzzRatio_3Lists(question, self.trainingList)

        if not match.uniqueAns(ansIndex):
            return None

        i = int(ansIndex[-1][0])
        j = int(ansIndex[-1][1])

        print(f"You requested information regarding "
              f"the {self.strTrainingList[i]} of your representative:")

        if i == 0:  # name list
            if j == 0:  # first name
                return classObject.firstName

            elif j == 1:  # middle name
                return classObject.middleName

            elif j == 2:  # last name
                return classObject.lastName

            elif j == 3:  # fullname
                return classObject.fullName

        # ---------------------------------------------------------------------

        elif i == 1:  # address list
            if j == 0:  # home address
                return classObject.homeAddress

            elif j == 1:  # columbia address
                return classObject.columbiaAddress

            elif j == 2:  # full address
                return str(
                    "Home address:\n" + classObject.homeAddress + "\n\nColumbia address:\n" + classObject.columbiaAddress)

        # ---------------------------------------------------------------------

        elif i == 2:  # phone list
            return TS.toString_tap(classObject.phoneNum, 'and')

        return None

    # ----------------------------------------------------------------------------

    @property
    def trainingList(self):
        return self.__trainingList

    @property
    def strTrainingList(self):
        return self.__strTrainingList
