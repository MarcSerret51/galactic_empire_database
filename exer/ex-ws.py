
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
from pathlib import Path
from cherrypy.lib.static import serve_file

# THIS PATH MUST BE DEFINED IN DEVELOPMENT ENVIRONMENTS WHERE FLAME
# WAS NOT INSTALLED AS A PACKAGE
class FlamePredict(object):
    @cherrypy.expose
    def index(self):
        return open('./templates/index.html')
        # return open(os.path.split(os.path.realpath(__file__))[0]+ '/templates/index.html') TODO: Make it works

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': False,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public',
        },
        'global' : {
            'server.socket_host' : '0.0.0.0',
            'server.socket_port' : 8080,
            'server.thread_pool' : 8,
        }
    }

    webapp = FlamePredict()
    cherrypy.quickstart(webapp, '/', conf)