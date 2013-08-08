import hashlib
import dbconn
import eventID
import os
import configure
import platform

###
###Create SHA512
###



def genSHA512(FileName, block_size=2**20):
    f = open(FileName, 'rb')
    h = hashlib.sha256()
    while True:
        data = f.read(block_size)
        if not data:
                break
        h.update(data)

    f.close()
    return h.hexdigest()



###
###User
###

def User_Add(UserEmail):
    User=dbconn.Db_User_Add(UserEmail)
    dbconn.Db_LogEvent(eventID.AddUser,User)
    return User

def User_Verify(UserId,UserSecret):
    Result=dbconn.Db_User_Vef(UserId,UserSecret)
    #dbconn.Db_LogEvent(eventID.VefUse,{"UserID":UserID,"Result":Result})
    return Result

def User_Disable(UserId,action,Operater):
    dbconn.Db_User_Disable(UserId,action)
    dbconn.Db_LogEvent(eventID.DisableUser,{"UserID":UserId,"action":action,"Operater":Operater})
    
###
###Task
###

def Task_Add(weburl,UserId):
    Task=dbconn.Db_Dl_AddTask(weburl,UserId)
    dbconn.Db_LogEvent(eventID.AddTask,Task)
    return Task

def Task_List(UserID):
    return dbconn.Db_Dl_ListTask(UserID)

def Task_GetProgress(DlTaskID):
    return dbconn.Db_Dl_GetTaskProgress(DlTaskID)

def Task_SetProgress(DlTaskID,Progress):
    return dbconn.Db_Dl_SetTaskProgress(DlTaskID,Progress)

def Task_GetVideoID(DlTaskID):
    return dbconn.Db_Dl_GetTaskResult(DlTaskID)

def Task_SetVideoID(DlTaskID,VideoID):
    return dbconn.Db_Dl_SetTaskResult(DlTaskID,VideoID)

def Task_Enable(DlTaskID,action):
    return dbconn.Db_Dl_EnableTask(DlTaskID,action)

def Task_GetUserID(DlTaskID):
    return dbconn.Db_Dl_GetTaskOwner(DlTaskID)

def Task_Picksome_L():
    return dbconn.Db_Dl_Pick_tasks_L()

def Task_Pickone_D():
    return dbconn.Db_Dl_Pick_a_task_D()

###
###File
###

def File_CreateCombination(VideoID,FileName):

    dbconn.Db_File_CreateCombination(DlTaskID["VideoID"],FileName,genSHA512(FileName))
    dbconn.Db_LogEvent(eventID.CreateFile,{"TaskID":DlTaskID,"FileName":FileName})

def File_ListCombinated(VideoID):
    return dbconn.Db_File_ListCombinated(DlTaskID)

def File_ReverseLookupVideoIDByFileName(VideoID):
    return dbconn.Db_ReverseLookupTaskIDByFileName(VideoID)

def File_Achive(VideoID,Operater):
    Db_File_AchivedTask(VideoID)
    dbconn.Db_LogEvent(eventID.AchivedFile,{"TaskID":VideoID,"Operater":Operater})

    return dbconn.Db_File_AchivedTask(DlTaskID)


def File_freemore():
    fd=os.statvfs(os.getcwd())
    fdhr=(fd.f_bavail * fd.f_frsize) / 1024
    if fdhr <= configure.Clean_thresholds:
        filelist=dbconn.Db_File_Get_unlink_list()
        nowclean=0
        while fdhr <= configure.Clean_thresholds and len(filelist) !=nowclean:
            Db_File_unlinked_file(filelist[nowclean])
            os.unlink(filelist[nowclean].FileName)
            fd=os.statvfs(os.getcwd())
            fdhr=(fd.f_bavail * fd.f_frsize) / 1024
            nowclean=nowclean+1


        

    


###
###Status
###

def Status_Set(StatusID,Operater):
    dbconn.Db_Server_SetStatus(StatusID)
    dbconn.Db_LogEvent(eventID.SetStatus,{"StatusID":StatusID,"Operater":Operater})

def Status_Get():
    return dbconn.Db_Server_GetStatus()


def Usege_Put(size):
    dbconn.Db_Usege_Download_Finished(size)

def Usege_Get():
    return dbconn.Db_Usege_Download_show()