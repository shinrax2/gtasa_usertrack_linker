#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# main.py for gtasa_usertrack_linker by shinrax2

import os
import sys

import winshell
from win32com.client import Dispatch

def createLnk(shell, path, target):
    link = shell.CreateShortCut(path)
    link.Targetpath = target
    link.WorkingDirectory = os.path.dirname(target)
    link.save()

def getfiles(dirpath):
    f =  []
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            if os.path.isfile(os.path.join(root, file)):
                f.append(os.path.join(root, file))
    f.sort(key=str.lower)
    return f
    
def filterfiles(files):
    filetypes = [".wav", ".ogg", ".mp3", ".wma"]
    newfiles = []
    for file in files:
        for type in filetypes:
            if file.endswith(type) == True:
                newfiles.append(file)
                break
    newfiles.sort(key=str.lower)
    return newfiles

dirs = sys.argv[1:]

for dir in dirs:
    if os.path.isdir(dir) == True:
        shell = Dispatch("WScript.Shell")
        musicdir = dir
        usertrackdir = os.path.join(os.path.join(os.environ["HOMEDRIVE"], os.environ["HOMEPATH"]), "Documents\GTA San Andreas User Files\\User Tracks")
        print("scanning "+dir)
        files = filterfiles(getfiles(musicdir))
        print("found {0} matching files".format(len(files)))
        print("creating .lnk files")
        counter = 1
        for file in files:
            createLnk(shell, os.path.join(usertrackdir, os.path.basename(file)+"_"+str(counter)+"_.lnk"), file)
            counter += 1
    else:
        print("skipping {0}. its not a directory".format(dir))
        print("please provide a valid path to the music you want to use")
input("done. press enter to exit.")
