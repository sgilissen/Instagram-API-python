#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from PyInstagramAPI import PyInstagramAPI

PyInstagramAPI = PyInstagramAPI("login", "password")
PyInstagramAPI.login()                        # login
mediaId = '1469246128528859784_1520706701'    # a media_id
recipients = []                             # array of user_ids. They can be strings or ints
PyInstagramAPI.direct_share(mediaId, recipients, text='aquest es es darrer')
