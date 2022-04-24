"""
============================================================================
Name        : bot_info.py
Author      : Seyed Ali Firooz Abadi
Version     : 2.0
Description : Information regarding the programmer. This is a copy of Assignment 03.
Copyright © 2022 Ali Firooz. All rights reserved.
============================================================================
"""

import re


def botInfoReq(question):
    botInfo = ['bot info', 'bot information', 'Tell me about yourself']
    for data in botInfo:
        if re.search(question, data, re.I):           # requesting information about the developer
            return "My creator is Ali Firooz, and you can contact him at \"social.mnuas@slmail.me\""
    return None
