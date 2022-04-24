"""
============================================================================
Name        : personal_info.py
Author      : Seyed Ali Firooz Abadi
Version     : 1.0
Copyright   : copyright notice 2022
Description : This class is responsible to answer everything about person's personal information
Copyright © 2022 Ali Firooz. All rights reserved.
============================================================================
TODO :
    - use regular expression to search for keywords in the person's personal information and return it to the user
============================================================================
"""

import abstract_chat_class as acc
import to_string as TS
import query_matching as qm


class PersonalInfo(acc.AbstractInfoManager):

    __personal = [['personal', 'personal info', 'personal information', 'tell me about the representative', 'Tell me about the rep', 'about repo']]

    # ----------------------------------------------------------------------------

    __trainingList = [__personal]
    __strTrainingList = ['personal information']

    # ----------------------------------------------------------------------------

    def basicCheck(self, question, person):
        match = qm.QueryMatching()
        ansIndex = match.fuzzRatio_3Lists(question, self.trainingList)

        if not match.uniqueAns(ansIndex):
            return None

        print(f"You requested information regarding "
              f"the {self.strTrainingList[0]} of your representative:")

        subAnsIndex = match.fuzzRatio_oneLists(question, person.personalInfo)
        if len(subAnsIndex) != 0:
            personInfoList = []
            for i in subAnsIndex:
                personInfoList.append(person.personalInfo[i])
            return TS.toString_list(personInfoList)

        i = int(ansIndex[-1][0])
        if i == 0:  # full personal information
            return TS.toString_list(person.personalInfo)
        return None

    # ----------------------------------------------------------------------------

    @property
    def trainingList(self):
        return self.__trainingList

    @property
    def strTrainingList(self):
        return self.__strTrainingList
