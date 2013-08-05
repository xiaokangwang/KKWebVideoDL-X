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
import time

import webreq
import version
import coreMan
import dbResult
import configure

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
        ServerStatus["Status"]=coreMan.Status_Get()
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

class NewTask(BaseHandler):

    def post(self):
        response = HTTPResponse()
        Respond={}
        DlInfomation=webreq.Req_Dl()


        if self.try_update_model(DlInfomation):
            Error={}
            Error["Success"]="NO"
            Error["Reason"]="Unacceptable_Data"
            return self.json_response(Error)

        if coreMan.User_Verify(DlInfomation.UserID,DlInfomation.UserSecret) != dbResult.VerifyUser_Success:
            Error={}
            Error["Success"]="NO"
            Error["Reason"]="Authentication_failure"
            Error["Detail"]= coreMan.User_Verify(DlInfomation.UserID,DlInfomation.UserSecret)
            return self.json_response(Error)

        Task=coreMan.Task_Add(DlInfomation.weburl,DlInfomation.UserID)
        Respond["Success"]="YES"
        Respond["Task"]=Task

        return self.json_response(Respond)

class UserDisable(BaseHandler):

    def post(self):
        response = HTTPResponse()
        Respond={}
        DisableUserInfomation=webreq.Req_DisableUser()

        if coreMan.User_Verify(DisableUserInfomation.UserID,DisableUserInfomation.UserSecret) != dbResult.VerifyUser_Success:
            Error={}
            Error["Success"]="NO"
            Error["Reason"]="Authentication_failure"
            Error["Detail"]= coreMan.User_Verify(DisableUserInfomation.UserID,DisableUserInfomation.UserSecret)
            return self.json_response(Error)
        
        Reason=""

        if DisableUserInfomation.UserID[0] != "#":
            if DisableUserInfomation.UserID != DisableUserInfomation.TargetUserID:
                Error={}
                Error["Success"]="NO"
                Error["Reason"]="Permission_Denied"
                return self.json_response(Error)
            else Reason="Disable_Self"
        else:
            Reason="Disable_ADMIN"


        coreMan.User_Disable(DisableUserInfomation.TargetUserID,1,Reason)

        Respond["Success"]="YES"
        return self.json_response(Respond)


class ListTask(BaseHandler):

    def post(self):
        response = HTTPResponse()
        GetDlResultInfomation=webreq.Req_GetDlResult()


        if self.try_update_model(GetDlResultInfomation):
            Error={}
            Error["Success"]="NO"
            Error["Reason"]="Unacceptable_Data"
            return self.json_response(Error)

        if coreMan.User_Verify(GetDlResultInfomation.UserID,GetDlResultInfomation.UserSecret) != dbResult.VerifyUser_Success:
            Error={}
            Error["Success"]="NO"
            Error["Reason"]="Authentication_failure"
            Error["Detail"]= coreMan.User_Verify(DlInfomation.UserID,DlInfomation.UserSecret)
            return self.json_response(Error)


        Tasks=coreMan.Task_List(GetDlResultInfomation.UserID)
        
        ListingTask=[]

        for TaskItem in Tasks:
            if TaskItem["Addtime"]+configure.Task_show_time >= time.time() :
                ListingTask.append(TaskItem)

        ListingTaskWithResult=[]

        for ListingTask in Taskitem:
            Taskitemx={}
            Taskitemx["Addtime"]=Taskitem["Addtime"]
            Taskitemx["weburl"]=Taskitem["weburl"]
            Taskitemx["Enabled"]=Taskitem["Enabled"]
            Taskitemx["ProgressN"]=coreMan.Task_GetProgress(Taskitem["TaskID"])["Numb"]
            Taskitemx["ProgressD"]=coreMan.Task_GetProgress(Taskitem["TaskID"])["Detail"]
            Taskitemx["ResultF"]=coreMan.File_ListCombinated(Taskitem["TaskID"])
            ListingTaskWithResult.append(Taskitemx)

        return self.json_response(ListingTaskWithResult)

class AchiveTask(BaseHandler):

    def post(self):
        response = HTTPResponse()
        Respond={}
        AchieveInfomation=webreq.Req_AchieveFile()


        if self.try_update_model(AchieveInfomation):
            Error={}
            Error["Success"]="NO"
            Error["Reason"]="Unacceptable_Data"
            return self.json_response(Error)

        if coreMan.User_Verify(AchieveInfomation.UserID,AchieveInfomation.UserSecret) != dbResult.VerifyUser_Success:
            Error={}
            Error["Success"]="NO"
            Error["Reason"]="Authentication_failure"
            Error["Detail"]= coreMan.User_Verify(AchieveInfomation.UserID,AchieveInfomation.UserSecret)
            return self.json_response(Error)
        
        Reason=""

        if AchieveInfomation.UserID[0] != "#":
            if AchieveInfomation.UserID != coreMan.Task_GetUserID(AchieveInfomation.TaskID):
                Error={}
                Error["Success"]="NO"
                Error["Reason"]="Permission_Denied"
                return self.json_response(Error)
            else Reason="Achieve_Self"
        else:
            Reason="Achieve_ADMIN"


        Task=coreMan.File_Achive(AchieveInfomation.TaskID,AchieveInfomation.UserID)
        Respond["Success"]="YES"

        return self.json_response(Respond)