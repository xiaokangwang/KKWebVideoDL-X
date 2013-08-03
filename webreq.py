from datetime import datetime
from wheezy.core.comp import u
import base64

class Req_Dl(object):

    def __init__(self,UserId=u(''), UserSecret=u(''),weburl=u('')):
        self.UserId = UserId
        self.UserSecret = UserSecret
        self.weburl = base64.urlsafe_b64decode(weburl)

class Req_NewUser(object):

    def __init__(self,UserEmail=u('')):
        self.UserEmail = UserEmail

class Req_SetPerf(object):

    def __init__(self,PreferFreeFormats=0,UserId=u(''), UserSecret=u('')):
        self.UserId = UserId
        self.UserSecret = UserSecret
        self.PreferFreeFormats = PreferFreeFormats

class Req_GetDlProgress(object):

    def __init__(self,DlTaskID=u(''),UserId=u(''), UserSecret=u('')):
        self.UserId = UserId
        self.UserSecret = UserSecret
        self.DlTaskID = DlTaskID

class Req_GetDlResult(object):

    def __init__(self,DlTaskID=u(''),UserId=u(''), UserSecret=u('')):
        self.UserId = UserId
        self.UserSecret = UserSecret
        self.DlTaskID = DlTaskID

class Req_GetFileStatus(object):

    def __init__(self,DlTaskID=u(''),UserId=u(''), UserSecret=u('')):
        self.UserId = UserId
        self.UserSecret = UserSecret
        self.DlTaskID = DlTaskID

class Req_GetServerStatus(object):

    def __init__(self,UserId=u(''), UserSecret=u('')):
        self.UserId = UserId
        self.UserSecret = UserSecret