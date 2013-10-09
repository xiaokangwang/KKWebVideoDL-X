import youtube_dl
import coreMan
import configure
import time
import os
now_Dprogressing={}
now_Lprogressing=[]

def genprogress(status):
    progress={}
    progress['Numb']=5+(status['total_bytes']/total_bytes)*90
    progress['Detail']="Downloading..."

def progresshook(status):
    if status["status"]=="downloading":
        coreMan.Task_SetProgress(now_Dprogressing["TaskID"],genprogress(status))
    if status["status"]=="downloading":
        coreMan.File_CreateCombination(now_Dprogressing["TaskID"],status["FileName"])

def subthook(filen):
    coreMan.File_CreateCombination(now_Dprogressing["TaskID"],filen)

def isServerRunning():
    if(coreMan.Task_Picksome_L() is None and coreMan.Task_Pickone_D() is None):
        time.sleep(20)
    return 1


def DownloadTask():
    global now_Dprogressing
    Task=now_Dprogressing
    coreMan.Task_Enable(Task['TaskID'],3)
    //TODO: Progress Download

def DeepProgress():
    ydl=youtube_dl.YoutubeDL({
    'forcedescription': False,
    'forceurl': False,
    'forceid': False,
    'forcetitle': False,
    'max_filesize': None, 
    'continuedl': True, 
    'restrictfilenames': False, 
    'verbose': True, 
    'buffersize': 1024, 
    'allsubtitles': True, 
    'listsubtitles': False, 
    'username': None, 
    'subtitleslang': None, 
    'skip_download': False, 
    'consoletitle': False, 
    'quiet': False, 
    'dump_intermediate_pages': False, 
    'playlistend': -1, 
    'writethumbnail': False, 
    'keepvideo': False, 
    'format': None, 
    'writesubtitles': True, 
    'matchtitle': None, 
    'daterange': youtube_dl.DateRange(), 
    'rejecttitle': None, 
    'retries': 10, 
    'password': None, 
    'updatetime': True, 
    'format_limit': None, 
    'forceformat': False, 
    'simulate': False, 
    'writedescription': False, 
    'usenetrc': False, 
    'noprogress': False, 
    'forcethumbnail': False, 
    'forcefilename': False, 
    'prefer_free_formats': False, 
    'ignoreerrors': False, 
    'writeinfojson': False, 
    'noresizebuffer': False, 
    'videopassword': None, 
    'outtmpl': u'%(autonumber)s-%(id)s.%(ext)s', 
    'writeautomaticsub': False, 
    'listformats': None, 
    'subtitlesformat': 'srt', 
    'nopart': False, 
    'logtostderr': False, 
    'test': False, 
    'min_filesize': None, 
    'max_downloads': None, 
    'progress_with_newline': False, 
    'playliststart': 1, 
    'autonumber_size': None, 
    'nooverwrites': False, 
    'ratelimit': None,
    'progresshook':progresshook,
    'subthook':subthook})
    ydl.add_default_info_extractors()
    
    global now_Dprogressing
    Task=now_Dprogressing
    coreMan.Task_Enable(Task['TaskID'],3)
    urls=[Task["weburl"]]
    if Task['TaskID'][0,3]=="File":
        DownloadTask()

    try:
        retcode=ydl.download(urls)
    except Exception:
        coreMan.Task_Enable(Task['TaskID'],5)
    else:
        coreMan.Task_Enable(Task['TaskID'],5)

    
    if retcode==0:
        coreMan.Task_Enable(Task['TaskID'],4)


def LightProgress():
    ydl=youtube_dl.YoutubeDL({
    'forcedescription': False,
    'forceurl': False,
    'forceid': False,
    'forcetitle': False,
    'max_filesize': None, 
    'continuedl': True, 
    'restrictfilenames': False, 
    'verbose': True, 
    'buffersize': 1024, 
    'allsubtitles': True, 
    'listsubtitles': False, 
    'username': None, 
    'subtitleslang': None, 
    'skip_download': False, 
    'consoletitle': False, 
    'quiet': False, 
    'dump_intermediate_pages': False, 
    'playlistend': -1, 
    'writethumbnail': False, 
    'keepvideo': False, 
    'format': None, 
    'writesubtitles': True, 
    'matchtitle': None, 
    'daterange': youtube_dl.DateRange(), 
    'rejecttitle': None, 
    'retries': 10, 
    'password': None, 
    'updatetime': True, 
    'format_limit': None, 
    'forceformat': False, 
    'simulate': False, 
    'writedescription': False, 
    'usenetrc': False, 
    'noprogress': False, 
    'forcethumbnail': False, 
    'forcefilename': False, 
    'prefer_free_formats': False, 
    'ignoreerrors': False, 
    'writeinfojson': False, 
    'noresizebuffer': False, 
    'videopassword': None, 
    'outtmpl': u'%(autonumber)s-%(id)s.%(ext)s', 
    'writeautomaticsub': False, 
    'listformats': None, 
    'subtitlesformat': 'srt', 
    'nopart': False, 
    'logtostderr': False, 
    'test': False, 
    'min_filesize': None, 
    'max_downloads': None, 
    'progress_with_newline': False, 
    'playliststart': 1, 
    'autonumber_size': None, 
    'nooverwrites': False, 
    'ratelimit': None,
    'progresshook':progresshook,
    'subthook':subthook})
    ydl.add_default_info_extractors()
    
    for theTask in Tasks:
        try:
            url=theTask["weburl"]
            info=ydl.extract_infoL(urls,False)
            if(info['extractor']!="generic"):
                VideoID=info['extractor']+info['id']+Task['RES']
            else:
                VideoID="File"+theTask["weburl"]
            
            coreMan.Task_SetVideoID(theTask['TaskID'],VideoID)
            coreMan.Task_Enable(theTask['TaskID'],2)
        except Exception:
            coreMan.Task_Enable(theTask['TaskID'],5)
        else:
            coreMan.Task_Enable(theTask['TaskID'],5)
        finally:
            pass


os.chdir(configure.File_store_at)


while isServerRunning():
    Tasks=coreMan.Task_Picksome_L()
    if Tasks is not None:
        global now_Lprogressing
        now_Lprogressing=Tasks
        LightProgress()


    Task=coreMan.Task_Pickone_D()
    if Task is not None:
        global now_Dprogressing
        now_Dprogressing=Task
        DeepProgress()

