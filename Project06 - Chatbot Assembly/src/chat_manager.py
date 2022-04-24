"""
============================================================================
Name        : chat_manager.py
Author      : Seyed Ali Firooz Abadi
Version     : 2.0
Description : This class will hold the person object and handles the questions. This is a copy of Assignment 03.
Copyright © 2022 Ali Firooz. All rights reserved.
============================================================================
TODO :
    - print all information when asking "give me all information"
============================================================================
"""

import OO_personal_info
import pickle
import basic_info
import other_info
import personal_info
import bot_info as bot


class ChatManager:
    def __init__(self, dist_Num):
        self.__person = self.__importPerson(dist_Num)

    @staticmethod
    def __importPerson(dist_Num):
        dist_Num = int(dist_Num)
        filePath = "../../Project02 - Processor/data/person" + str(dist_Num) + ".pickle"
        try:
            file = open(filePath, "rb")
        except:
            if dist_Num == 78:
                file = open("../data/person78.pickle", "rb")
            else:
                raise Exception("Couldn't find the district you chose")
        tempPerson = pickle.load(file)
        file.close()
        return tempPerson

    def answerQuestions(self, question: str) -> str:
        bi = basic_info.BasicInfo()
        oi = other_info.OtherInfo()
        pi = personal_info.PersonalInfo()

        answer = bi.basicCheck(question, self.__person)
        if answer is not None:
            return answer

        answer = oi.basicCheck(question, self.__person)
        if answer is not None:
            return answer

        answer = pi.basicCheck(question, self.__person)
        if answer is not None:
            return answer

        answer = bot.botInfoReq(question)
        if answer is not None:
            return answer

        elif answer is None:
            return "Sorry I couldn't understand you, please rephrase your question."
