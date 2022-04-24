"""
============================================================================
Name        : main.py
Author      : Seyed Ali Firooz Abadi
Version     : 2.0
Description : The code driver for the chat bot. This is a copy of Assignment 03.
Copyright © 2022 Ali Firooz. All rights reserved.
============================================================================
TODO :
    - find some other way to calculate the number of answers so that you don't add extra lines in the main method to make the count right.
============================================================================
"""


import chat_manager as cm
import to_string as TS
import chat_logger
import sys

if __name__ == '__main__':
    log = chat_logger.Logger()
    sys.stdout = log

    # Getting the district number and initiating the chat manager
    i = 0
    while i < 4:
        log.question = "please enter the district number you are interested in\nI support district 78 for now:\n"
        districtNum = TS.checkExit(log.loggedInput())
        if districtNum == "exit":
            log.writeCSV()
            quit(0)
        try:
            districtNum = int(districtNum)
            # Create an instance of the chat manager
            chat = cm.ChatManager(districtNum)
            i = 5
        except:
            i += 1
            if i == 3:
                print("You tried too many times, please contact someone for help")
                log.writeCSV()
                quit(0)
            print("Couldn't find the district you chose, please enter a valid number")

    print("\nWelcome"
          "\nNow let's play a game"
          "\nRemember that you can just type quit or exit anytime to exit the program"
          "\nHave fun")

    # answering questions
    while True:
        log.question = "\nWhat do you want to know?\n"
        userQuestion = TS.checkExit(log.loggedInput())

        if userQuestion == "exit":
            log.writeCSV()
            quit(0)
        tempP01 = chat.answerQuestions(userQuestion)
        if tempP01 == chat.answerQuestions("None"):
            print()
        print(tempP01)
        if tempP01 == chat.answerQuestions("None"):
            print()
