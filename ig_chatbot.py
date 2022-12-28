#!/usr/bin/env python# -*- coding: utf-8 -*-

from instabot_py import InstaBot


print('ENTER YOUR USERNAME HERE->>>')
name = input()
print('ENTER YOUR PASSWORD HERE->>>')
password = input()


bot = InstaBot('login','password')
bot.auto_mod()
