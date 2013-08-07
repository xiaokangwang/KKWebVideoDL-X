from datetime import datetime
from wheezy.core.comp import u


class Req_Dl(object):

    def __init__(self,UserID=u(''), UserSecret=u(''),weburl=u('')):
        self.UserID = UserID
        self.UserSecret = UserSecret
        self.weburl = weburl

class Req_NewUser(object):

    def __init__(self,UserEmail=u('')):
        self.UserEmail = UserEmail

class Req_DisableUser(object):

    def __init__(self,TargetUserID=u(''),UserID=u(''), UserSecret=u('')):
        self.UserID = UserID
        self.TargetUserID = TargetUserID
        self.UserSecret = UserSecret

class Req_SetPerf(object):

    def __init__(self,PreferFreeFormats=0,UserID=u(''), UserSecret=u('')):
        self.UserID = UserID
        self.UserSecret = UserSecret
        self.PreferFreeFormats = PreferFreeFormats

class Req_GetDlResult(object):

    def __init__(self,UserID=u(''), UserSecret=u('')):
        self.UserID = UserID
        self.UserSecret = UserSecret

class Req_AchieveFile(object):

    def __init__(self,TaskID=u(''),UserID=u(''), UserSecret=u('')):
        self.UserID = UserID
        self.UserSecret = UserSecret
        self.TaskID = TaskID