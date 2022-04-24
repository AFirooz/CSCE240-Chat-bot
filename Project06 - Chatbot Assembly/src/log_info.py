"""
============================================================================
Name        : log_info.py
Author      : Seyed Ali Firooz Abadi
Version     : 1.0
Description : This class is responsible for answering questions in regard to the statistics
Copyright © 2022 Ali Firooz. All rights reserved.
============================================================================
TODO :
    - summary
    - show chat summary #
    - show chat #
    - exception handling ex: There are only 12 chat sessions. Please choose a valid number.
============================================================================
"""

import abstract_chat_class as acc
import to_string as TS
import query_matching as qm


class logInfo (acc.AbstractInfoManager):

    __summary = [['summary', 'show me summary', 'showchat summary', 'show chat summary']]
    __oneChat = [['showchat ', 'show chat ']]
    __oneChatSummary = [['showchat-summary ']]

    __trainingList = [__summary, __oneChatSummary, __oneChat]
    __strTrainingList = ['the performance summary of the chat bot', 'the summary of a specific chat', 'one chat specifically']

    def basicCheck(self, question, person):
        match = qm.QueryMatching()
        ansIndex = match.fuzzRatio_3Lists(question, self.trainingList)

        if not match.uniqueAns(ansIndex):
            return None

        i = int(ansIndex[-1][0])  # index of each of the trainingList items
        j = int(ansIndex[-1][1])  # index of the sub lists inside each of the trainingList items

        print(f"You requested information regarding {self.strTrainingList[i]}")

        if i == 0:                      # summary
            pass
        if i == 1:                      # oneChat
            pass
        if i == 2:                      # oneChatSummary
            pass

        return None

    @property
    def trainingList(self):
        pass

    @property
    def strTrainingList(self):
        pass