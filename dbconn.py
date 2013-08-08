from pymongo import MongoClient
import pymongo
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

def Db_Get_UsegeCollection():
    client = MongoClient(configure.The_MongoDB_URL)
    db = client[configure.The_MongoDB_Db]
    collection = db['Usege']
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

def Db_User_GetNice(UserID):
    User=Db_Get_UserCollection().find_one({"UserID":UserID})
    return User["Nice"]

def Db_User_SetNice(UserID,Nice):
    User=Db_Get_UserCollection().update({"UserID":UserID},{"$set":{"Nice":Nice}})
    return User["Nice"]

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
    AddingTask["VideoID"]=""
    AddingTask["Nice"]=Db_User_GetNice(UserID)
    Db_Get_TaskCollection().insert(AddingTask)
    return AddingTask
    

def Db_Dl_GetTaskProgress(TaskID):
    theTask=Db_Get_TaskCollection().find_one({"TaskID":TaskID})
    return theTask["Progress"]
    

def Db_Dl_GetTaskVideoID(TaskID):
    theTask=Db_Get_TaskCollection().find_one({"TaskID":TaskID})
    return theTask["VideoID"]
    

def Db_Dl_SetTaskProgress(TaskID,Progress):
    theTask=Db_Get_TaskCollection().update({"TaskID":TaskID},{ "$set": { "Progress" : Progress } } )
    

def Db_Dl_SetTaskVideoID(TaskID,VideoID):
    theTask=Db_Get_TaskCollection().update({"TaskID":TaskID},{ "$set": { "VideoID" : VideoID } } )
    

def Db_Dl_EnableTask(TaskID,action):
    theTask=Db_Get_TaskCollection().update({"TaskID":TaskID},{ "$set": { "Enabled" : action } } )

def Db_Dl_GetTaskOwner(TaskID):
    theTask=Db_Get_TaskCollection().find_one({"TaskID":TaskID})
    return theTask["UserID"]
    
def Db_Dl_Pick_tasks_L():
    theTasks=Db_Get_TaskCollection().find({"Enabled":1}).sort([("Nice",pymongo.ASCENDING),("AddTime",pymongo.ASCENDING)])
    return theTasks

def Db_Dl_Pick_a_task_D():
    theTasks=Db_Get_TaskCollection().find_one({"Enabled":2}).sort([("Nice",pymongo.ASCENDING),("AddTime",pymongo.ASCENDING)])
    return theTasks[0]



#Downloaded File Management
def Db_File_CreateCombination(VideoID,FileName,Hash_SHA51,size):
    if Db_Get_FileCollection().find_one({"Hash_SHA512":Hash_SHA512}) is None:
        FileItem={}
        FileItem["VideoID"]=VideoID
        FileItem["FileName"]=FileName
        FileItem["Hash_SHA512"]=Hash_SHA512
        FileItem["size"]=size
        FileItem["counter"]=1
        FileItem["LastUse"]=time.time()
        FileItem["AlwaysKeep"]=0
        FileItem["NowAV"]=1 #is this file ready to dowmload?
        Db_Get_FileCollection().insert(FileList)
    else:
        origc=Db_Get_FileCollection().find_one({"Hash_SHA512":Hash_SHA512})
        Db_Get_FileCollection().update({"Hash_SHA512":Hash_SHA512},{"$set":{"counter":origc + 1,"NowAV":1,"LastUse":time.time()}})




def Db_File_ListCombinated(VideoID):
    Filelist=Db_Get_FileCollection().find({"VideoID":TaskID})
    Filelistr=[]
    for FilelistItem in Filelist:
        Filelistr.append(FilelistItem["FileName"])
    return Filelistr

def Db_File_ReverseLookupVideoIDByFileName(FileName):
    VideoID=Db_Get_FileCollection().find_one({"FileName":FileName})
    return VideoID

def Db_File_AchivedVideo(VideoID):
    origFiles=Db_Get_FileCollection().find({"VideoID":VideoID})
    for origFilesItem in origFiles:
        Db_Get_FileCollection().update({"Hash_SHA512":origFilesItem["Hash_SHA512"]},{"$set":{"counter":origFilesItem["counter"]-1 }})

def Db_File_AchivedTask(TaskID):
    Db_File_AchivedVideo(Db_Dl_GetTaskVideoID(TaskID))

def Db_File_unlinked_file(FileName):
    Db_Get_FileCollection().update({"FileName":FileName},{"$set":{"NowAV":0}})

def Db_File_Get_unlink_list():
    Avl=Db_Get_FileCollection().find({"AlwaysKeep":0,"NowAV":1,"counter":0}).sort([("LastUse",pymongo.ASCENDING)])
    return Avl

    




#Server Status

def Db_Server_SetStatus(StatusID):
    Db_Get_StatusCollection().update({"Domain":"Current"},{"$set": {"Status":StatusID}})
    

def Db_Server_GetStatus():
    return Db_Get_StatusCollection().find_one({"Domain":"Current"})["Status"]
    


def Db_Usege_Download_Finished(size):
    orgsrev=Db_Get_UsegeCollection().find_one({"Type":"system"})
    Db_Get_UsegeCollection().update({"Type":"system"},"$set":{"count":orgsrev["count"]+1,"size":orgsrev["size"]+size})

def Db_Usege_Download_show(size):
    return Db_Get_UsegeCollection().find_one({"Type":"system"})
