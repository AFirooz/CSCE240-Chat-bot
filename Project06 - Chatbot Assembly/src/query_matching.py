"""
============================================================================
Name        : query_matching.py
Author      : Seyed Ali Firooz Abadi
Version     : 1.0
Description : This file contains different methods to match a query (string) to a 3 nested lists of strings
Copyright © 2022 Ali Firooz. All rights reserved.
============================================================================
TODO :
    - change the size of __createBoolList to match the size of aList exactly
============================================================================
"""

from fuzzywuzzy import process, fuzz
import Levenshtein


class QueryMatching:
    __matchLimit = 85
    # this is the default value that can be changed while creating an instance

    def __init__(self, *matchLimit):
        if len(matchLimit) != 0:
            self.__matchLimit = matchLimit[0]

    @staticmethod
    def __createBoolList(aList):
        # this method is used to initiate a list with all False values
        a = 0
        b = 0
        c = int(len(aList))
        for subList in aList:
            a = len(subList)
            b = max(b, a)
        return [[False] * b for i in range(c)]

    @staticmethod
    def __getIndex_2List(aList):
        # aList is a True / False list
        indexList = []
        i = 0
        for innerList in aList:
            j = 0
            for data in innerList:
                if data:
                    indexList.append([i, j])
                j = j+1
            i = i+1
        return indexList

    def extractOne_3Lists(self, aQuery, aList):
        boolQuery = self.__createBoolList(aList)
        for mainList in aList:                      # mainList  ==> ex: __trainingList_name
            for innerList in mainList:              # innerList ==> ex: __firstName
                # each element of the "innerList" is now a simple list of strings
                matchRatio = process.extractOne(str(aQuery), innerList)
                matchRatio = matchRatio[1]
                if matchRatio >= self.matchLimit:
                    i = int(aList.index(mainList))
                    j = int(mainList.index(innerList))
                    boolQuery[i][j] = True
        return self.__getIndex_2List(boolQuery)

    def lev_3Lists(self, aQuery, aList):
        aQuery = str(aQuery).lower()
        boolQuery = self.__createBoolList(aList)
        for mainList in aList:                      # mainList  ==> ex: __trainingList_name
            for innerList in mainList:              # innerList ==> ex: __firstName
                for data in innerList:              # data      ==> ex: 'first name'
                    # each element "data" is now a simple string
                    matchRatio = Levenshtein.seqratio(aQuery, data)
                    matchRatio = round(matchRatio * 100)
                    if matchRatio > self.matchLimit:
                        i = int(aList.index(mainList))
                        j = int(mainList.index(innerList))
                        boolQuery[i][j] = True
        return self.__getIndex_2List(boolQuery)

    def fuzzRatio_3Lists(self, aQuery, aList):
        aQuery = str(aQuery).lower()
        boolQuery = self.__createBoolList(aList)
        for mainList in aList:                      # mainList  ==> ex: __trainingList_name
            for innerList in mainList:              # innerList ==> ex: __firstName
                for data in innerList:              # data      ==> ex: 'first name'
                    # each element "data" is now a simple string
                    matchRatio = fuzz.token_set_ratio(aQuery, data)
                    if matchRatio > self.matchLimit:
                        i = int(aList.index(mainList))
                        j = int(mainList.index(innerList))
                        boolQuery[i][j] = True
        return self.__getIndex_2List(boolQuery)

    def fuzzRatio_oneLists(self, aQuery, aList):
        aQuery = str(aQuery).lower()
        indexQuery = []
        for data in aList:
            # each element "data" is now a simple string
            matchRatio = fuzz.token_set_ratio(aQuery, data)
            if matchRatio > self.matchLimit:
                i = int(aList.index(data))
                indexQuery.append(i)
        return indexQuery

    @staticmethod
    def uniqueAns(indexList):
        if len(indexList) == 0:
            return False
        if len(indexList) != 1:
            for i in range(len(indexList) - 1):
                if indexList[i][0] != indexList[i+1][0]:
                    return False
            return True
        elif len(indexList) == 1:
            return True

    @property
    def matchLimit(self):
        return self.__matchLimit
