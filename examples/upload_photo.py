#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from PyInstagramAPI import PyInstagramAPI

PyInstagramAPI = PyInstagramAPI("login", "password")
PyInstagramAPI.login()  # login

photo_path = '/path/to/photo.jpg'
caption = "Sample photo"
PyInstagramAPI.uploadPhoto(photo_path, caption=caption)
