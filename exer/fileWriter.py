import os
import sys
import json
from logger import errorLog
from pathlib import *
import datetime as time

def writeToFile(name, planet):
    """Writes the name of the rebel and 
    the planet in a text file"""
    config = getConfig()
    if config == 0:
        errorLog("Configuration file not found")
        return ("CONFERROR", "Configuration file not found")
    try:
        filee = open(config, "a")
        filee.write("Rebel " + name + " on " + planet + " at "+ str(time.datetime.now()) +"\n")
        filee.close()
        getConfig()
        return "1"  #CherryPy can't return integer
    except IOError:
        errorLog("Permission error")
        return ("PERMERROR", "Permission denied")

def getConfig():
    try:
        with open('config.json') as conf:
            conf = json.load(conf)
        if ":" in conf['path']:                     # if path contains : is Windows  #TODO: Better os path handling
            conf = PureWindowsPath(conf['path'])    # if a dir (or file) contains : in Linux the program will fail
        return conf
    except (IOError, Exception):
        errorLog("Error reading configuration")
        return 0
