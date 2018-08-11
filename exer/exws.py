
#! -*- coding: utf-8 -*-

##    Authors:       Marc Serret i Garcia (marcserret@live.com)
##
##    Copyright 2018 Marc Serret i Garcia

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
from logger import infoLog
from fileWriter import writeToFile

class EmpireIndex(object):
    @cherrypy.expose
    def index(self):
        return open('./templates/index.html')

@cherrypy.expose
class UploadRebel(object):
    def GET(self, name = "", planet = ""):
        if name == "" or planet == "":
            return ("FIELDERROR", "Please fill the two fields")
        infoLog("Request received from " + cherrypy.request.remote.ip)
        result = writeToFile(name, planet)
        infoLog("Sending: " + result[0] + "to: " + cherrypy.request.remote.ip)
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