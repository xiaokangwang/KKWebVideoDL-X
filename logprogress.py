import dbconn

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

def ProgressLog(bgn,due):
	pass

def MakeReport(bgn,due):
	OrigLog=AquireLogsBwt(bgn,due)
	ClassifyLogItem(OrigLog)

def AquireLogReport(bgn,due):
	pass