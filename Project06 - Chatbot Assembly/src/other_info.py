"""
============================================================================
Name        : other_info.py
Author      : Seyed Ali Firooz Abadi
Version     : 1.0
Copyright   : copyright notice 2022
Description : This class is responsible to answer everything about person's political party, county, district, committee assignments, and service time
Copyright © 2022 Ali Firooz. All rights reserved.
============================================================================
"""


import abstract_chat_class as acc
import to_string as TS
import query_matching as qm


class OtherInfo(acc.AbstractInfoManager):
    __supportedDistrictsAnswer = [78]

    __party = [['party', 'political party', 'politics']]
    __county = [['county']]
    __committee = [['committee', 'assignment', 'committee assignment', 'committee assignments', 'what committees is my repo on', 'What committees is my representative on']]
    __service = [['service time', 'service']]
    __district = [['district number']]
    __everything = [['tell me everything', 'everything you know']]
    __supportedDistricts = [['what district do you support', 'what district you know']]

    __trainingList = [__party, __county, __committee, __service, __district, __everything, __supportedDistricts]
    __strTrainingList = ['political party', 'county', 'committee assignments', 'service time', 'district number', 'full extend of information', 'supported districts']

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

        if i == 0:                                              # political party
            return classObject.party
        # ---------------------------------------------------------------------
        elif i == 1:                                            # county
            return classObject.county
        # ---------------------------------------------------------------------
        elif i == 2:                                            # committee assignments
            return TS.toString_space(classObject.committeeAssignments, 'and')
        # ---------------------------------------------------------------------
        elif i == 3:                                            # service time
            return classObject.serviceTime
        # ---------------------------------------------------------------------
        elif i == 4:                                            # district
            return classObject.district
        # ---------------------------------------------------------------------
        elif i == 5:                                            # everything
            return repr(classObject)
        # ---------------------------------------------------------------------
        elif i == 6:                                            # supported districts
            return TS.toString_list(self.__supportedDistrictsAnswer, "District ")
        # ---------------------------------------------------------------------
        return None
    # ----------------------------------------------------------------------------

    @property
    def trainingList(self):
        return self.__trainingList

    @property
    def strTrainingList(self):
        return self.__strTrainingList
