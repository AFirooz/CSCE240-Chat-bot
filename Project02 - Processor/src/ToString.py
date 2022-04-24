
def toString_space(aList, *seperator):
    if len(seperator) == 1:
        str1 = ' ' + str(seperator[0]) + ' '
    else:
        str1 = " "
    return str1.join(aList)


def toString_nextLine(aList, *seperator):
    if len(seperator) == 1:
        str1 = '\n' + str(seperator[0]) + '\n'
    else:
        str1 = "\n"
    return str1.join(aList)


def toString_tap(aList, *seperator):
    if len(seperator) == 1:
        str1 = ' \t ' + str(seperator[0]) + ' \t '
    else:
        str1 = " \t "
    return str1.join(aList)


def toString_list(aList, *seperator):
    # aList.insert(0,'')
    if len(seperator) == 1:
        # str1 = '\n' + str(seperator[0])
        strList = ''
        for element in aList:
            strList = strList + str(seperator[0]) + str(element) + '\n'
    else:
        strList = ''
        i = int(1)
        for element in aList:
            strList = strList + str(i) + '- ' + str(element) + '\n'
            i += 1
    return strList