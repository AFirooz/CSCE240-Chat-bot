"""
============================================================================
Name        : main.py
Author      : Seyed Ali Firooz Abadi
Version     : 1.0
Copyright   : copyright notice 2022
Description : The Driver code for my chat bot
============================================================================
"""

import ToString as TS
import OO_personal_info as PInfo
import pickle


if __name__ == '__main__':
    try:
        districtNum = int(input("please input the number of the district you want to load: "))
        if districtNum == 78:
            person = PInfo.Person()
        else:
            filePath = input("Please enter the district's pickle file path to load:\n")
            person = PInfo.Person(filePath)
    except:
        print("There was a problem with either the number you entered or the file path.\n")
        exit(0)

    person.exportToPickle(districtNum, person)  # to use with assignment 3

    # Here you see all the Information stored in related variables and being printed
    print(f"\n\n"
          f"My full name is: {person.fullName}\n"
          f"Which consists of:\n"
          f"first name: {person.firstName}\n"
          f"middle name: {person.middleName}\n"
          f"last name: {person.lastName}\n"
          f"\n"
          f"I'm the representor of district: {person.district}\n\n"
          f"phone number: {TS.toString_tap(person.phoneNum, 'and')}\n\n"
          f"home add: \n{person.homeAddress}\n\nwd"
          f"columbia add: \n{person.columbiaAddress}\n\n"
          f"political party: {person.party}\n"
          f"my county is: {person.county}\n"
          f"my service time: {person.serviceTime}\n"
          f"my committee assignments: {TS.toString_space(person.committeeAssignments, 'and')}\n"
          f"\n"
          f"And finally, my personal info are stored in a list which can be accessed one at a time (as needed)\n"
          f"for example: {person.personalInfo[5]}\n\n"
          f"or accessed as a full list \n"
          f"personal info:\n{TS.toString_list(person.personalInfo)}\n"
          )
