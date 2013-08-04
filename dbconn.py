from pymongo import MongoClient
import time
import configure
import eventID
import genUserID
import dbResult
import genTaskID

#DataBase Connection Create
def Db_Get_LogCollection():
    client = MongoClient(configure.The_MongoDB_URL)
    db = client[The_MongoDB_Db]
    collection = db['Log']
    return collection

def Db_Get_UserCollection():
    client = MongoClient(configure.The_MongoDB_URL)
    db = client[The_MongoDB_Db]
    collection = db['User']
    return collection

def Db_Get_TaskCollection():
    client = MongoClient(configure.The_MongoDB_URL)
    db = client[The_MongoDB_Db]
    collection = db['Task']
    return collection

def Db_Get_FileCollection():
    client = MongoClient(configure.The_MongoDB_URL)
    db = client[The_MongoDB_Db]
    collection = db['File']
    return collection

def Db_Get_StatusCollection():
    client = MongoClient(configure.The_MongoDB_URL)
    db = client[The_MongoDB_Db]
    collection = db['Status']
    return collection


#Loging system
def Db_LogEvent(Event,Details):
    Log={}
    Log["Event"]=Event
    Log["Details"]=Details
    Log["Time"]=time.time()
    Db_Get_LogCollection().insert(Log)
	pass



#Account management
def Db_User_Add(UserEmail):
    User=genUserID.genUserID()
    User["UserEmail"]=UserEmail
    User["Enabled"]=configure.User_immediate_Enable
    Db_Get_UserCollection().insert(User)
	return User

def Db_User_Vef(UserId,UserSecret):
	User=Db_Get_UserCollection().findOne({"UserId":UserId,"UserSecret":UserSecret})
	if User is not None:
			if User["Enabled"]==1:
                return dbResult.VerifyUser_Success
            else:
                return dbResult.VerifyUser_Disabled
	else:
		return dbResult.VerifyUser_Deny
    
	pass

def Db_User_Disable(UserId,action):
    User=Db_Get_UserCollection().findOne({"UserId":UserId})
    User["Enabled"]=action
    Db_Get_UserCollection().update({"UserId":UserId},{ $set: { "Enabled" : action } } )
	pass



#Download Task management
def Db_Dl_ListTask(UserId):
    TaskList=Db_Get_TaskCollection().find({"UserID":UserId})
    if TaskList is not None:
        return TaskList
    else:
        return None
	pass

def Db_Dl_AddTask(weburl,UserId):
    AddingTask={}
    Task["weburl"]=weburl
    Task["UserId"]=UserId
    Task["TaskId"]=genTaskID.genTaskID()
    Task["AddTime"]=time.time()
    Db_Get_TaskCollection().insert(Task)
    return Task
	pass

def Db_Dl_GetTaskProgress(DlTaskID):
    theTask=Db_Get_TaskCollection().findOne({"DlTaskID":DlTaskID})
    return theTask["Progress"]
	pass

def Db_Dl_GetTaskResult(DlTaskID):
    theTask=Db_Get_TaskCollection().findOne({"DlTaskID":DlTaskID})
    return theTask["Result"]
	pass

def Db_Dl_SetTaskProgress(DlTaskID,Progress):
    theTask=Db_Get_TaskCollection().update({"DlTaskID":UserId},{ $set: { "Progress" : Progress } } )
    pass

def Db_Dl_SetTaskResult(DlTaskID,Result):
    theTask=Db_Get_TaskCollection().update({"DlTaskID":UserId},{ $set: { "Result" : Result } } )
    pass



#Downloaded File Management
def Db_File_CreateCombination(DlTaskID,FileName):
	pass

def Db_File_ListCombinated(DlTaskID):
	pass

def Db_File_ReverseLookupTaskIDByFileName(FileName):
	pass

def Db_File_AchivedTask(DlTaskID):
	pass


#Server Status

def Db_Server_SetStatus(StatusID):
	pass

def Db_Server_GetStatus():
	pass