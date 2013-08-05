import dbconn
import eventID

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
	dbconn.Db_LogEvent(eventID.DisableUser,{"UserID"=UserId,"action"=action,"Operater"=Operater})
    
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

def Task_GetResult(DlTaskID):
	return dbconn.Db_Dl_GetTaskResult(DlTaskID)

def Task_SetResult(DlTaskID,Progress):
	return dbconn.Db_Dl_SetTaskResult(DlTaskID,Progress)

def Task_Enable(DlTaskID,action):
	return dbconn.Db_Dl_EnableTask(DlTaskID,action)

###
###File
###

def File_CreateCombination(DlTaskID,File):
     dbconn.Db_File_CreateCombination(DlTaskID,File)
     dbconn.Db_LogEvent(eventID.CreateFile,{"DlTaskID"=DlTaskID,"File"=File})

def File_ListCombinated(DlTaskID):
	return dbconn.Db_File_ListCombinated(DlTaskID)

def File_ReverseLookupTaskIDByFileName(DlTaskID):
	return dbconn.Db_ReverseLookupTaskIDByFileName(DlTaskID)

def Status_Set(StatusID,Operater):
	dbconn.Db_Server_SetStatus(StatusID)
	dbconn.Db_LogEvent(eventID.SetStatus,{"StatusID"=StatusID,"Operater"=Operater})

def Status_Get():
	return dbconn.Db_Server_GetStatus()
