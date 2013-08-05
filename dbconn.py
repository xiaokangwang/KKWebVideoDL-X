from pymongo import MongoClient
import time
import configure
import eventID
import genUserID
import dbResult
import genTaskId
import genFileList

#DataBase Connection Create
def Db_Get_LogCollection():
    client = MongoClient(configure.The_MongoDB_URL)
    db = client[configure.The_MongoDB_Db]
    collection = db['Log']
    return collection

def Db_Get_UserCollection():
    client = MongoClient(configure.The_MongoDB_URL)
    db = client[configure.The_MongoDB_Db]
    collection = db['User']
    return collection

def Db_Get_TaskCollection():
    client = MongoClient(configure.The_MongoDB_URL)
    db = client[configure.The_MongoDB_Db]
    collection = db['Task']
    return collection

def Db_Get_FileCollection():
    client = MongoClient(configure.The_MongoDB_URL)
    db = client[configure.The_MongoDB_Db]
    collection = db['File']
    return collection

def Db_Get_StatusCollection():
    client = MongoClient(configure.The_MongoDB_URL)
    db = client[configure.The_MongoDB_Db]
    collection = db['Status']
    return collection


#Loging system
def Db_LogEvent(Event,Details):
    Log={}
    Log["Event"]=Event
    Log["Details"]=Details
    Log["Time"]=time.time()
    Db_Get_LogCollection().insert(Log)
    



#Account management
def Db_User_Add(UserEmail):
    User=genUserID.genUserID()
    User["UserEmail"]=UserEmail
    User["Enabled"]=configure.User_immediate_Enable
    Db_Get_UserCollection().insert(User)
    return User

def Db_User_Vef(UserId,UserSecret):
    User=Db_Get_UserCollection().find_one({"UserId":UserId,"UserSecret":UserSecret})
    if User is not None:
            if User["Enabled"]==1:
                return dbResult.VerifyUser_Success
            else:
                return dbResult.VerifyUser_Disabled
    else:
        return dbResult.VerifyUser_Deny
    
    

def Db_User_Disable(UserId,action):
    User=Db_Get_UserCollection().find_one({"UserId":UserId})
    User["Enabled"]=action
    Db_Get_UserCollection().update({"UserId":UserId},{"$set":{ "Enabled" : action } },upsert=False, multi=False )
    



#Download Task management
def Db_Dl_ListTask(UserId):
    TaskList=Db_Get_TaskCollection().find({"UserID":UserId})
    if TaskList is not None:
        return TaskList
    else:
        return None
    

def Db_Dl_AddTask(weburl,UserId):
    AddingTask={}
    Task["weburl"]=weburl
    Task["UserId"]=UserId
    Task["TaskId"]=genTaskId.genTaskID()
    Task["Enabled"]=configure.Task_immediate_Enable
    Task["AddTime"]=time.time()
    Db_Get_TaskCollection().insert(Task)
    return Task
    

def Db_Dl_GetTaskProgress(DlTaskID):
    theTask=Db_Get_TaskCollection().find_one({"DlTaskID":DlTaskID})
    return theTask["Progress"]
    

def Db_Dl_GetTaskResult(DlTaskID):
    theTask=Db_Get_TaskCollection().find_one({"DlTaskID":DlTaskID})
    return theTask["Result"]
    

def Db_Dl_SetTaskProgress(DlTaskID,Progress):
    theTask=Db_Get_TaskCollection().update({"DlTaskID":DlTaskID},{ "$set": { "Progress" : Progress } } )
    

def Db_Dl_SetTaskResult(DlTaskID,Result):
    theTask=Db_Get_TaskCollection().update({"DlTaskID":DlTaskID},{ "$set": { "Result" : Result } } )
    

def Db_Dl_EnableTask(DlTaskID,action):
    theTask=Db_Get_TaskCollection().update({"DlTaskID":DlTaskID},{ "$set": { "Enabled" : action } } )

def Db_Dl_GetTaskOwner(DlTaskID):
    theTask=Db_Get_TaskCollection().find_one({"DlTaskID":DlTaskID})
    return theTask["UserId"]
    


#Downloaded File Management
def Db_File_CreateCombination(DlTaskID,File):
    Filelist=Db_Get_FileCollection().find_one({"DlTaskID":DlTaskID})
    if Filelist is not None:
        Db_Get_FileCollection().update({"DlTaskID":DlTaskID},{ "$push" : { "FileList" : {File} } })
    else:
        FileList=genFileList.genFileList(DlTaskID)
    Db_Get_FileCollection().insert(FileList)
    

def Db_File_ListCombinated(DlTaskID):
    Filelist=Db_Get_FileCollection().find_one({"DlTaskID":DlTaskID})
    return Filelist["Filelist"]

def Db_File_ReverseLookupTaskIDByFileName(FileName):
    Filelist=Db_Get_FileCollection().find({"FileList":FileName})
    return Filelist

def Db_File_AchivedTask(DlTaskID):
    Db_Get_FileCollection().update({"DlTaskID":DlTaskID},{ "$set": { "Achived" : 1 } } )


#Server Status

def Db_Server_SetStatus(StatusID):
    Db_Get_StatusCollection().update({"Domain":"Current"},{"$set": {"Status":StatusID}})
    

def Db_Server_GetStatus():
    return Db_Get_StatusCollection().find_one({"Domain":"Current"})["Status"]
    