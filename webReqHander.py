from wheezy.http import HTTPResponse
from wheezy.http import WSGIApplication
from wheezy.routing import url
from wheezy.web.handlers import BaseHandler
from wheezy.web.middleware import bootstrap_defaults
from wheezy.web.middleware import path_routing_middleware_factory
from wheezy.web.handlers.file import file_handler
from wheezy.web.handlers.base import permanent_redirect_handler , redirect_handler
import ctypes
import os
import platform
import sys

import webreq
import version
import coreMan

class PingHandler(BaseHandler):

    def get(self):
        response = HTTPResponse()
        response.write('PING_SUCCESS')
        return response

class GetServerStatusHandler(BaseHandler):

    def post(self):
        response = HTTPResponse()
        ServerStatus={}
        ServerStatus["Version"]=version.the_version
        fd=os.statvfs(os.getcwd())
        fdhr=(fd.f_bavail * fd.f_frsize) / 1024
        ServerStatus["FreeSpace"]=fdhr
        return self.json_response(ServerStatus)
        

class NewUser(BaseHandler):

    def post(self):
        response = HTTPResponse()
        Respond={}
        UserInfomation=webreq.Req_NewUser()


        if self.try_update_model(UserInfomation):
            Error={}
            Error["Success"]="NO"
            Error["Reason"]="Unacceptable_Data"
            return self.json_response(Error)

        User=coreMan.User_Add(UserInfomation.UserEmail)
        Respond["Success"]="YES"
        Respond["User"]=User

        return self.json_response(Respond)
