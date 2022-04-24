"""
============================================================================
Name        : main.py
Author      : Seyed Ali Firooz Abadi
Version     : 5.2
Copyright   : copyright notice
Description : Extracting data about district 78, and saving it to a file
============================================================================
Version Changes :
    1-      Handling error in requesting data from the website (using local copy as a fail safe)
    2-      If statement to check district input
    3-      Write the variables in a text file
    4-      Counting the number of lines, words, char of the extracted content
    5-      Clean text output
    5.1-    Creating a sample output file
    5.2-    Create a Pickle to use your parsed (processed) data in Project 2
    6-      Remove hard coding from the code (look for "# Hard Coded")
    7-      getting the source code of the district image and opening the browser with the image to show the user,
            or at least show the alt tag content:
                img = soup.find('img', attrs = {'class':'allowcontextmenu'})
                print(img)
============================================================================
"""

import requests
from bs4 import BeautifulSoup
from CountingLinesWordsChar import *
import pickle


print("\nWelcome\nEnter number 78")

districtNum = int(0)
i = int(0)
while type(districtNum) == str or districtNum <= 0:
    if i == 3:
        print("You entered too many wrong inputs, please contact a professional for help\n")
        quit(0)
    try:
        districtNum = int(input("Please enter the district number of your choice: "))
        if districtNum < 0:
            # noinspection PyUnresolvedReferences
            print(error)       # Just a way to go to the except statement.
    except:
        districtNum = "try again"
        print("\nWhat you entered was not valid. Please enter a valid number, maybe try number: 78\n")
    i = i+1

if districtNum == 78:

    try:
        req = requests.get("https://www.scstatehouse.gov/member.php?code=0141477256")
        # Each parsing technique is different in organizing HTML tags, that's why we need to do a preliminary parsing with lxml and then use html5lib
        soup = BeautifulSoup(req.content, "lxml")
        soup = BeautifulSoup(req.content, "html5lib")
    except:
        with open('../data/District78.html', 'r') as html_file:
            local_copy = html_file.read()
            soup = BeautifulSoup(local_copy, "lxml")
            soup = BeautifulSoup(local_copy, "html5lib")
            print("Due to an unexpected error, the content has been read from a local copy\nTo get the online version, you can run the program again")


    # Hard Coded
    fullName = soup.find('h2', attrs = {'class':'barheader'}).get_text(strip=True)
    fullNameList = fullName.split()
    firstName = fullNameList[1]
    middleName = fullNameList[2]
    lastName = fullNameList[3]


    county = soup.select_one("div > div > p > span").get_text(strip=True)

    party = soup.select("div > div > p")[1].get_text(strip=True)
    party = party.split()[0]

    district = soup.select("div > div > p")[2].get_text(strip=True)
    district = district.split()[1]

    columbia_address = soup.select("div > div > p")[3].get_text("\n", strip=True)

    home_address = soup.select("div > div > p")[5].get_text("\n", strip=True)

    phoneNum01 = soup.select("div > div > p")[4].get_text(" ", strip=True)
    phoneNum01 = phoneNum01.split()[2:]

    phoneNum02 = soup.select("div > div > p")[6].get_text(" ", strip=True)
    phoneNum02 = phoneNum02.split()[2:]

    """
    # One way to remove the Hard Coding is by processing the block of text, rather than choosing the number of list element we need by hand
    # personal_info = soup.select("div > div > table > tbody > tr > td")[0].get_text("\n", strip=True)
    # The above code will generate just one block of information, while the code below will give each personal info as a string
    """
    # Hard Coded
    personal_info = soup.select("div > div > table > tbody > tr > td > ul > li")[0:19]

    # Hard Coded
    committee_assignments = soup.select("div > div > table > tbody > tr > td > ul > li")[19:21]

    # Hard Coded
    service_time = soup.select("div > div > table > tbody > tr > td > ul > li")[21].get_text(strip=True)
    # ---------------------------------------------------------------
    with open('../data/Extracted Data.txt', 'w') as exText:
        exText.write("Full Name:\n")
        exText.writelines(firstName + " ")
        exText.write(middleName + " ")
        exText.write(lastName)
        exText.write('\n')
        exText.write("\n--------------------------------------\n\n")

        exText.write("County:\n")
        exText.write(county)
        exText.write('\n')
        exText.write("\n--------------------------------------\n\n")

        exText.write('Political Party:\n')
        exText.write(party)
        exText.write('\n')
        exText.write("\n--------------------------------------\n\n")

        exText.write('District:\n')
        exText.write(district)
        exText.write('\n')
        exText.write("\n--------------------------------------\n\n")

        exText.write('Columbia Address:\n')
        exText.write(columbia_address)
        exText.write('\n')
        exText.write("\n--------------------------------------\n\n")

        exText.write('Home Address:\n')
        exText.write(home_address)
        exText.write('\n')
        exText.write("\n--------------------------------------\n\n")

        exText.write('Phone Number 01:\n')
        exText.writelines(phoneNum01)
        exText.write('\n')
        exText.write("\n--------------------------------------\n\n")

        exText.write('Phone Number 02:\n')
        exText.writelines(phoneNum02)
        exText.write('\n')
        exText.write("\n--------------------------------------\n\n")

        exText.write('Personal Information:\n\n')
        i = int(1)
        for child in personal_info:
            exText.writelines(str(i) + '- ')
            exText.write(child.get_text(strip=True))
            exText.write('\n')
            i = i + 1
        exText.write("\n--------------------------------------\n\n")

        exText.write('Committee Assignments:\n')
        i = int(1)
        for child in committee_assignments:
            exText.writelines(str(i) + '- ')
            exText.write(child.get_text(' ', strip=True))
            exText.write('\n')
            i = i + 1
        exText.write("\n--------------------------------------\n\n")

        exText.write('Service In Public Office:\n')
        exText.write(service_time)
        exText.write('\n')
        exText.write("\n--------------------------------------")

    with open('../data/Statistics.txt', 'w') as statFile:

        # Created 4 variables to store the returned values, notice that the variables and the return list must be in the same order. It is also possible to do the assignment one by one
        num_spaces, num_charc, num_lines, num_words = counter('../data/Extracted Data.txt')

        try:
            # printing total word count
            statFile.write("Number of words in text file\t\t\t: ")
            statFile.write(str(num_words))
            statFile.write('\n')

            # printing total line count
            statFile.write("Number of lines in text file\t\t\t: ")
            statFile.write(str(num_lines))
            statFile.write('\n')

            # printing total character count
            statFile.write("Number of characters in text file\t\t: ")
            statFile.write(str(num_charc))
            statFile.write('\n')

            # printing total space count
            statFile.write("Number of spaces in text file\t\t\t: ")
            statFile.write(str(num_spaces))

        except:
            statFile.write('The extracted text file was not found')

    print('\nPlease have a look at the Extracted Data.txt and the Statistics.txt files located in the data folder\n\nGoodbye')
    # ---------------------------------------------------------------
    # saving bad processed data into a list to later use in pickle dictionary
    personal_info_list = []
    for i in range(len(personal_info)):
        personal_info_list.append(personal_info[i].get_text(strip=True))

    committee_assignments_list = []
    for i in range(len(committee_assignments)):
        committee_assignments_list.append(committee_assignments[i].get_text(' ', strip=True))

    phoneNum_list = [(phoneNum01[0]+' '+phoneNum01[1]), (phoneNum02[0]+' '+phoneNum02[1])]
    # ---------------------------------------------------------------
    # Creating a Dictionary of all the extracted variables to transfer using a pickle
    processedData = dict(Full_Name=[firstName, middleName, lastName],
                         Home_Address=home_address, Columbia_Address=columbia_address,
                         Phone_Number=phoneNum_list,
                         Party=party, County=county, District=district,
                         Personal_Info=personal_info_list, Committee_Assignments=committee_assignments_list, Service_Time=service_time)

    # Creating the pickle
    pFile = open("../data/processedData.pickle", "wb")
    pickle.dump(processedData, pFile)
    pFile.close()

else:
    print("Unfortunately this district number is not supported")
    quit(0)