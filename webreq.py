from datetime import datetime
from wheezy.core.comp import u
import base64
class DlReq(object):

    def __init__(self,UserId=u(''), weburl=u('')):
        self.UserId = UserId
        self.weburl = base64.urlsafe_b64decode(weburl)