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

def Db_User_Vef(UserID,UserSecret):
    User=Db_Get_UserCollection().find_one({"UserID":UserID,"UserSecret":UserSecret})
    if User is not None:
            if User["Enabled"]==1:
                return dbResult.VerifyUser_Success
            else:
                return dbResult.VerifyUser_Disabled
    else:
        return dbResult.VerifyUser_Deny
    
    

def Db_User_Disable(UserID,action):
    User=Db_Get_UserCollection().find_one({"UserID":UserID})
    User["Enabled"]=action
    Db_Get_UserCollection().update({"UserID":UserID},{"$set":{ "Enabled" : action } },upsert=False, multi=False )
    



#Download Task management
def Db_Dl_ListTask(UserID):
    TaskList=Db_Get_TaskCollection().find({"UserID":UserID})
    if TaskList is not None:
        return TaskList
    else:
        return None
    

def Db_Dl_AddTask(weburl,UserID):
    AddingTask={}
    AddingTask["weburl"]=weburl
    AddingTask["UserID"]=UserID
    AddingTask["TaskID"]=genTaskId.genTaskID()
    AddingTask["Enabled"]=configure.Task_immediate_Enable
    AddingTask["AddTime"]=time.time()
    AddingTask["Progress"]={"Numb":5,"Detail":"New Task"}
    AddingTask["Result"]=[]
    Db_Get_TaskCollection().insert(AddingTask)
    return AddingTask
    

def Db_Dl_GetTaskProgress(TaskID):
    theTask=Db_Get_TaskCollection().find_one({"TaskID":TaskID})
    return theTask["Progress"]
    

def Db_Dl_GetTaskResult(TaskID):
    theTask=Db_Get_TaskCollection().find_one({"TaskID":TaskID})
    return theTask["Result"]
    

def Db_Dl_SetTaskProgress(TaskID,Progress):
    theTask=Db_Get_TaskCollection().update({"TaskID":TaskID},{ "$set": { "Progress" : Progress } } )
    

def Db_Dl_SetTaskResult(TaskID,Result):
    theTask=Db_Get_TaskCollection().update({"TaskID":TaskID},{ "$set": { "Result" : Result } } )
    

def Db_Dl_EnableTask(TaskID,action):
    theTask=Db_Get_TaskCollection().update({"TaskID":TaskID},{ "$set": { "Enabled" : action } } )

def Db_Dl_GetTaskOwner(TaskID):
    theTask=Db_Get_TaskCollection().find_one({"TaskID":TaskID})
    return theTask["UserID"]
    


#Downloaded File Management
def Db_File_CreateCombination(TaskID,File):
    Filelist=Db_Get_FileCollection().find_one({"TaskID":TaskID})
    if Filelist is not None:
        Db_Get_FileCollection().update({"TaskID":TaskID},{ "$push" : { "FileList" : {File} } })
    else:
        FileList=genFileList.genFileList(TaskID)
    Db_Get_FileCollection().insert(FileList)
    

def Db_File_ListCombinated(TaskID):
    Filelist=Db_Get_FileCollection().find_one({"TaskID":TaskID})
    return Filelist["FileList"]

def Db_File_ReverseLookupTaskIDByFileName(FileName):
    Filelist=Db_Get_FileCollection().find({"FileList":FileName})
    return Filelist

def Db_File_AchivedTask(TaskID):
    Db_Get_FileCollection().update({"TaskID":TaskID},{ "$set": { "Achived" : 1 } } )
    Db_Get_TaskCollection().update({"TaskID":TaskID},{ "$set": { "Enabled" : 7 }})


#Server Status

def Db_Server_SetStatus(StatusID):
    Db_Get_StatusCollection().update({"Domain":"Current"},{"$set": {"Status":StatusID}})
    

def Db_Server_GetStatus():
    return Db_Get_StatusCollection().find_one({"Domain":"Current"})["Status"]
    