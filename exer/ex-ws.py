
#! -*- coding: utf-8 -*-

##    Description    Flame web-service
##
##    Authors:       Marc Serret i Garcia (marcserret@live.com)
##
##    Copyright 2018 Marc Serret i Garcia
##
##    This file is part of Flame
##
##    Flame is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation version 3.
##
##    Flame is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with Flame. If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import shutil
import tempfile
import json
import re
import cherrypy
import datetime as time
from pathlib import Path
from cherrypy.lib.static import serve_file

def writeToFile(name, planet):
    """Writes the name of the rebel and 
    the planet in a text file"""
    try:
        filee = open("../../test/lmao.txt", "a")
        filee.write("Rebel " + name + " on " + planet + " at "+ str(time.datetime.now()) +"\n")
        filee.close()
        return "1"  #CherryPy can't return integer
    except IOError:
        return ("PERMERROR", "Permission denied")


# THIS PATH MUST BE DEFINED IN DEVELOPMENT ENVIRONMENTS WHERE FLAME
# WAS NOT INSTALLED AS A PACKAGE
class EmpireIndex(object):
    @cherrypy.expose
    def index(self):
        return open('./templates/index.html')

@cherrypy.expose
class UploadRebel(object):
    def GET(self, name = "", planet = ""):
        if name == "" or planet == "":
            return ("FIELDERROR", "Please fill the two fields")
        result = writeToFile(name, planet)
        return result


if __name__ == '__main__':
    conf = {
        '/addRebel': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')]
        },
        '/': {
            'tools.sessions.on': False,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public',
        }
    }

    webapp = EmpireIndex()
    webapp.addRebel = UploadRebel()
    cherrypy.quickstart(webapp, '/', conf)