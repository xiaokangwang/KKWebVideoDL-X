import dbconn
import eventID

def AquireLogsBwt(bgn,due):
	return dbconn.Db_Get_LogRange(bgn,due)
	

def ClassifyLogItem(Logitem):
	result={}
	resultclass=[]

	for logi in Logitem:
		if !resultclass.count(logi["Event"])
		    resultclass.append(logi["Event"])

    for insclass in resultclass:
    	result[insclass]=[]

    for logi in Logitem:
    	result[logi["Event"]].append(logi)

    return result

def ReportGener_DownloadRequest_Sum(LogCed):
	result={}

	ReportGener={"Gener":"ReportGener_DownloadRequest_Sum","Show":"Download Requset"}
	result["Gener"]=ReportGener

	ReportCont={}

	downloadsum=0

	for LogCedid in LogCed[eventID.AddTask]:
		downloadsum=downloadsum+1

	ReportCont["Download_Request"]=downloadsum

	result["cont"]=ReportCont
	
	return result

def PrepareReportGener():
	pass

def ProgressLog(LogCed):
	pass

def MakeReport(bgn,due):
	OrigLog=AquireLogsBwt(bgn,due)
	Cedl=ClassifyLogItem(OrigLog)
	ProgressLog(Cedl)

def AquireLogReport(bgn,due):
	pass