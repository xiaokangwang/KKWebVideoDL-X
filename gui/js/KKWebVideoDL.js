function utf8_to_b64( str ) {
    return window.btoa(unescape(encodeURIComponent( str )));
}

function b64_to_utf8( str ) {
    return decodeURIComponent(escape(window.atob( str )));
}

$("#Get_a_User_Learm_more_tigger").click(
    function(){
                $("#Get_a_User_Learm_more_data").fadeIn(1000);
                $("#Get_a_User_Learm_more_tigger").fadeOut(1000);
            }
);

$("#Get_a_User_Learm_more_data").hide();


$("#Get_a_User_Btn").click(
    function(){
                $("#Get_a_User_Dig").modal();
            }
);

$("#Get_a_User_Dig_Close").click(
    function(){
                $("#Get_a_User_Dig").modal("hide");
            }
);



$("#Get_a_User_Dig_No_PWUN_reason").click(
    function(){
                $("#Get_a_User_Dig_No_PWUN_reason").popover('show');
            }
);

$('#Get_a_User_Dig_No_PWUN_reason').on('hidden.bs.popover', function () {
    $("#Get_a_User_Dig_No_PWUN_reason").fadeOut(1000);
})


Core_NewUser=function (UserEmail,SuccCallback,FailCallBack) {
    var Core_NewUser_ReqAJAX=$.ajax({
        url:configure_KKWebVideoDL_API_Base_URL+"NewUser",
        async:true,
        cache:false,
        timeout:30000,
        type:"POST",
        data: "UserEmail="+UserEmail,
    });

    Core_NewUser_ReqAJAX.done(function(msg) {
        console.log( "Core_NewUser_Reqsucc");
        console.log( msg );
        ServerRespond=msg
        if(ServerRespond.Success!="YES"){
            FailCallBack(ServerRespond.Reason)
        }else{
            SuccCallback(msg);
        }
    });

    Core_NewUser_ReqAJAX.fail(function(jqXHR, textStatus) {
        console.log( "Core_NewUser_Reqfail: " + textStatus );
        FailCallBack("AJAX_FAIL")
    })
}


Core_GetServerStatus=function (SuccCallback,FailCallBack) {
    var Core_GetServerStatus_ReqAJAX=$.ajax({
        url:configure_KKWebVideoDL_API_Base_URL+"GetServerStatus",
        async:true,
        cache:false,
        timeout:30000,
        type:"POST",
        data: "",
    });

    Core_GetServerStatus_ReqAJAX.done(function(msg) {
        console.log( "Core_GetServerStatus_Reqsucc");
        console.log( msg );

            SuccCallback(msg)
    });

    Core_GetServerStatus_ReqAJAX.fail(function(jqXHR, textStatus) {
        console.log( "Core_GetServerStatus_Reqfail: " + textStatus );
        FailCallBack("AJAX_FAIL")
    })
}

Core_UserDisable=function (TargetUserID,UserID,UserSecret,SuccCallback,FailCallBack) {
    var Core_UserDisable_ReqAJAX=$.ajax({
        url:configure_KKWebVideoDL_API_Base_URL+"UserDisable",
        async:true,
        cache:false,
        timeout:30000,
        type:"POST",
        data: "TargetUserID="+TargetUserID+"&UserID="+UserID+"&UserSecret="+UserSecret,
    });

    Core_UserDisable_ReqAJAX.done(function(msg) {
        console.log( "Core_UserDisable_Reqsucc");
        console.log( msg );
        ServerRespond=msg
        if(ServerRespond.Success!="YES"){
            FailCallBack(ServerRespond.Reason)
        }else{
            SuccCallback(msg)
        }
    });

    Core_UserDisable_ReqAJAX.fail(function(jqXHR, textStatus) {
        console.log( "Core_UserDisable_Reqfail: " + textStatus );
        FailCallBack("AJAX_FAIL")
    })
}


Core_initLang=function(lang){
    if(sessionStorage.langtrs==undefined||lang!=sessionStorage.langtrslt){
    var initLang_AJAX=$.ajax({
        dataType: "json",
        url: 'ajax/lang_'+lang+'.json',
        async:false,
    }
    ).done(function(langms){
        sessionStorage.langtrs=JSON.stringify(langms);});

    }
    sessionStorage.langtrslt=lang
}

Core_Lang_Out=function(shortdes){
    return JSON.parse(sessionStorage.langtrs)[shortdes];
}

Core_Lang_Out_pack=function(){
    return JSON.parse(sessionStorage.langtrs);
}


Core_ListTask=function (UserID,UserSecret,SuccCallback,FailCallBack) {
    var Core_ListTask_ReqAJAX=$.ajax({
        url:configure_KKWebVideoDL_API_Base_URL+"ListTask",
        async:true,
        cache:false,
        timeout:30000,
        type:"POST",
        data: "UserID="+UserID+"&UserSecret="+UserSecret,
    });

    Core_ListTask_ReqAJAX.done(function(msg) {
        console.log( "Core_ListTask_Reqsucc");
        console.log( msg );
        ServerRespond=msg
        if(ServerRespond.Success!="YES"){
            FailCallBack(ServerRespond.Reason)
        }else{
            SuccCallback(msg["List"])
        }
    });

    Core_ListTask_ReqAJAX.fail(function(jqXHR, textStatus) {
        console.log( "Core_ListTask_Reqfail: " + textStatus );
        FailCallBack("AJAX_FAIL")
    })
}


Core_AchiveTask=function (UserID,UserSecret,TaskID,SuccCallback,FailCallBack) {
    var Core_AchiveTask_ReqAJAX=$.ajax({
        url:configure_KKWebVideoDL_API_Base_URL+"AchiveTask",
        async:true,
        cache:false,
        timeout:30000,
        type:"POST",
        data: "UserID="+UserID+"&UserSecret="+UserSecret+"&TaskID="+TaskID,
    });

    Core_AchiveTask_ReqAJAX.done(function(msg) {
        console.log( "Core_AchiveTask_Reqsucc");
        console.log( msg );
        ServerRespond=msg
        if(ServerRespond.Success!="YES"){
            FailCallBack(ServerRespond.Reason)
        }else{
            SuccCallback(msg)
        }
    });

    Core_AchiveTask_ReqAJAX.fail(function(jqXHR, textStatus) {
        console.log( "Core_AchiveTask_Reqfail: " + textStatus );
        FailCallBack("AJAX_FAIL")
    })
}

Core_AddTask=function (UserID,UserSecret,weburl,SuccCallback,FailCallBack) {
    var Core_AddTask_ReqAJAX=$.ajax({
        url:configure_KKWebVideoDL_API_Base_URL+"NewTask",
        async:true,
        cache:false,
        timeout:30000,
        type:"POST",
        data: "UserID="+UserID+"&UserSecret="+UserSecret+"&weburl="+utf8_to_b64(weburl),
    });

    Core_AddTask_ReqAJAX.done(function(msg) {
        console.log( "Core_AddTask_Reqsucc");
        console.log( msg );
        ServerRespond=msg
        if(ServerRespond.Success!="YES"){
            FailCallBack(ServerRespond.Reason)
        }else{
            SuccCallback(msg)
        }
    });

    Core_AddTask_ReqAJAX.fail(function(jqXHR, textStatus) {
        console.log( "Core_AddTask_Reqfail: " + textStatus );
        FailCallBack("AJAX_FAIL")
    })
}


User_LoadLang=function(){
    if(localStorage.langperf==undefined){
        localStorage.langperf=configure_KKWebVideoDL_User_lang_def;
    }

    Core_initLang(localStorage.langperf);

}

User_LoadLang();

User_SetLang=function(langtoset){
    localStorage.langperf=langtoset;
    sessionStorage.langtrs="";
    sessionStorage.langtrslt="";
    location.reload();
}

User_toConnect=function(UserID,UserSecret){
    localStorage.UserID=UserID;
    localStorage.UserSecret=UserSecret;

}

User_disConnect=function(){
    localStorage.UserID="";
    localStorage.UserSecret="";

}

User_isConnected=function(){
    if((localStorage.UserID==undefined||localStorage.UserID=="")&&(localStorage.UserSecret==undefined||localStorage.UserSecret=="")){
        return false;
    }else{
        return true;
    }
}

User_showContext_taskstat=function(Enabled){
    switch(Enabled) {
        case 0:
        return '<span class="glyphicon glyphicon-pause"></span>';
            break;
        case 1:
        return '<span class="glyphicon glyphicon-time"></span>';
            break;
        case 2:
        return '<span class="glyphicon glyphicon-refresh"></span>';
        break;
        case 3:
        return '<span class="glyphicon glyphicon-circle-arrow-down"></span>';
        break;
        case 4:
        return '<span class="glyphicon glyphicon-check"></span>';
        break;
        case 5:
        return '<span class="glyphicon glyphicon-exclamation-sign"></span>';
        break;

        default:
        return '<span class="glyphicon glyphicon-warning-sign"></span>';

}
}

var downloadURL = function (url) {
    var hiddenIFrameID = 'hiddenDownloader',
        iframe = document.getElementById(hiddenIFrameID);
    if (iframe === null) {
        iframe = document.createElement('iframe');
        iframe.id = hiddenIFrameID;
        iframe.style.display = 'none';
        document.body.appendChild(iframe);
    }
    iframe.src = url;
};

var firstload=1;


User_showContext_taskaction=function(task){
        switch(task.Enabled) {
        case 0:
        return '<span class="glyphicon glyphicon-play" ng-click="Activetask('+task.TaskID+');"></span>';
            break;
        case 1:
        return Core_Lang_Out("Task_Nothing_to_do");
            break;
        case 2:
        return Core_Lang_Out("Task_Nothing_to_do");
        break;
        case 3:
        return Core_Lang_Out("Task_Nothing_to_do");
        break;
        case 4:
        return '<span class="glyphicon glyphicon-download-alt" ng-click="DownloadTask('+task.TaskID+');"></span><span class="glyphicon glyphicon-fire" ng-click="AchiveTask("'+task.TaskID+'");"></span>';
        break;
        case 5:
        return Core_Lang_Out("Task_Nothing_can_do_term");
        break;

        default:
        return Core_Lang_Out("UI_Task_Nothing_unknow");

}
}


var KKWebVideoDLApp = angular.module('KKWebVideoDLApp', []);

KKWebVideoDLApp.controller('MainCtrl', function($scope,$timeout) {
    var Langpack=Core_Lang_Out_pack();

  for(LangID in Langpack){
    $scope["UI_"+LangID]=Langpack[LangID];
  }
  $scope.tavlangs=configure_KKWebVideoDL_avlang;
  $scope.toReConnect=function(){
    User_toConnect($scope.Reconnect_input_ID,$scope.Reconnect_input_Secret);
            if(User_isConnected()){
            $scope.isloggedin=true;
            $scope.UpdTL();
        }

  };

  $scope.NewAccount=function(){
    $("#Get_a_User_Dig_sub").attr("disabled", "disabled");
    $("#Get_a_User_Dig_sub").html('.....<span class="glyphicon glyphicon-time"></span>.....');
    Core_NewUser($scope.CreateAccount_input_Email,
        function(UserData){
            User_toConnect(UserData.User.UserID,UserData.User.UserSecret);
            $("#Get_a_User_Dig").modal("hide");
            $scope.isloggedin=true;
            $("#container_ExistingUser").fadeOut(1000);
            $("#container_NewUser").fadeOut(1000);

    })
  }
  $scope.isloggedin=User_isConnected();

  //Server Status Updater
   $scope.UpdSS=function(){Core_GetServerStatus(function(data){
        $scope.ServerStatus=data;
        $scope.$apply();
        $timeout($scope.UpdSS,5000);
    },function() {
        $("#Server_Status_panel").addClass("panel-danger");
        $("#Server_Status_panel_content").html($scope["UI_ServerStatus_Status_Crashed"]);
        $scope.$apply();
    });
 
  }

  $timeout($scope.UpdSS,5000);

  Core_GetServerStatus(function(data){
        $scope.ServerStatus=data;
        $scope.$apply();}) //First hit


   //Tasklist Updater

   $scope.UpdTL=function(){Core_ListTask(localStorage.UserID,localStorage.UserSecret,function(data){
        
        $scope.tasklist=[];
        
        $.each(data,function(index,val){
            var listitem={};
            listitem.Addtime=val.AddTime;
            listitem.weburl=val.weburl;
            listitem.EnabledE=User_showContext_taskstat(val.Enabled);
            listitem.ProgressN=val.ProgressN;
            listitem.ProgressD=val.ProgressD;
            listitem.ResultF=val.ResultF;
            listitem.actionlist=User_showContext_taskaction(val);
            $scope.tasklist.push(listitem);
        });

        $scope.$apply();
        $timeout($scope.UpdTL,5000);
    },function() {
        $scope.$apply();
    }
    );
}
   
  if($scope.isloggedin&&firstload==1){
    $scope.UpdTL();
    firstload=0;
  }

  $scope.DownloadTask=function(TaskID){
    $.each(scope.tasklist.ResultF,function(index,val){
downloadURL(configure_KKWebVideoDL_Download_Base_URL+val);
    });
  }
    $scope.AchiveTask=function(TaskID){
        Core_AchiveTask(localStorage.UserID,localStorage.UserSecret,TaskID,function(){},function(){});
    }
    $scope.AddTask=function(){
        Core_AddTask(localStorage.UserID,localStorage.UserSecret,$scope.weburladd,function(){
            $("#addtaskbtn").removeAttr("disabled");
        },function(){});
        $scope.weburladd="";
        $("#addtaskbtn").attr("disabled", "disabled");
    }


});