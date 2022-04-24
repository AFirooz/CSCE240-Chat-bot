"""
============================================================================
Name        : abstract_chat_class.py
Author      : Seyed Ali Firooz Abadi
Version     : 2.0
Description : This is an abstract class to force all other classes to have the necessary methods. This is a copy of Assignment 03.
Copyright © 2022 Ali Firooz. All rights reserved.
============================================================================
"""

from abc import ABC, abstractmethod
import query_matching as qm


class AbstractInfoManager(ABC):

    @abstractmethod
    def basicCheck(self, question, person):
        # This is a template of how should this method be written
        match = qm.QueryMatching()
        ansIndex = match.fuzzRatio_3Lists(question, self.trainingList)

        if not match.uniqueAns(ansIndex):
            return None

        i = int(ansIndex[-1][0])  # index of each of the trainingList items
        j = int(ansIndex[-1][1])  # index of the sub lists inside each of the trainingList items

        print(f"You requested information regarding "
              f"the {self.strTrainingList[i]} of your representative:")

        if i == 0:  # name list
            if j == 0:  # first name
                return
            if j == 1:  # last name
                return
        if i == 1:  # phone
            if j == 0:  # first phone
                return
            if j == 1:  # second phone
                return
        return None

    @property
    @abstractmethod
    def trainingList(self):
        return self.__trainingList

    @property
    @abstractmethod
    def strTrainingList(self):
        return self.__strTrainingList
