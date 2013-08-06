var Base64 = {
 
    // private property
    _keyStr : "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_=",
 
    // public method for encoding
    encode : function (input) {
        var output = "";
        var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
        var i = 0;
 
        input = Base64._utf8_encode(input);
 
        while (i < input.length) {
 
            chr1 = input.charCodeAt(i++);
            chr2 = input.charCodeAt(i++);
            chr3 = input.charCodeAt(i++);
 
            enc1 = chr1 >> 2;
            enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
            enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
            enc4 = chr3 & 63;
 
            if (isNaN(chr2)) {
                enc3 = enc4 = 64;
            } else if (isNaN(chr3)) {
                enc4 = 64;
            }
 
            output = output +
            this._keyStr.charAt(enc1) + this._keyStr.charAt(enc2) +
            this._keyStr.charAt(enc3) + this._keyStr.charAt(enc4);
 
        }
 
        return output;
    },
 
    // public method for decoding
    decode : function (input) {
        var output = "";
        var chr1, chr2, chr3;
        var enc1, enc2, enc3, enc4;
        var i = 0;
 
        input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");
 
        while (i < input.length) {
 
            enc1 = this._keyStr.indexOf(input.charAt(i++));
            enc2 = this._keyStr.indexOf(input.charAt(i++));
            enc3 = this._keyStr.indexOf(input.charAt(i++));
            enc4 = this._keyStr.indexOf(input.charAt(i++));
 
            chr1 = (enc1 << 2) | (enc2 >> 4);
            chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
            chr3 = ((enc3 & 3) << 6) | enc4;
 
            output = output + String.fromCharCode(chr1);
 
            if (enc3 != 64) {
                output = output + String.fromCharCode(chr2);
            }
            if (enc4 != 64) {
                output = output + String.fromCharCode(chr3);
            }
 
        }
 
        output = Base64._utf8_decode(output);
 
        return output;
 
    },
 
    // private method for UTF-8 encoding
    _utf8_encode : function (string) {
        string = string.replace(/\r\n/g,"\n");
        var utftext = "";
 
        for (var n = 0; n < string.length; n++) {
 
            var c = string.charCodeAt(n);
 
            if (c < 128) {
                utftext += String.fromCharCode(c);
            }
            else if((c > 127) && (c < 2048)) {
                utftext += String.fromCharCode((c >> 6) | 192);
                utftext += String.fromCharCode((c & 63) | 128);
            }
            else {
                utftext += String.fromCharCode((c >> 12) | 224);
                utftext += String.fromCharCode(((c >> 6) & 63) | 128);
                utftext += String.fromCharCode((c & 63) | 128);
            }
 
        }
 
        return utftext;
    },
 
    // private method for UTF-8 decoding
    _utf8_decode : function (utftext) {
        var string = "";
        var i = 0;
        var c = c1 = c2 = 0;
 
        while ( i < utftext.length ) {
 
            c = utftext.charCodeAt(i);
 
            if (c < 128) {
                string += String.fromCharCode(c);
                i++;
            }
            else if((c > 191) && (c < 224)) {
                c2 = utftext.charCodeAt(i+1);
                string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
                i += 2;
            }
            else {
                c2 = utftext.charCodeAt(i+1);
                c3 = utftext.charCodeAt(i+2);
                string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
                i += 3;
            }
 
        }
 
        return string;
    }
 
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

Core_Lang_Out_pack=function(shortdes){
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
            SuccCallback(msg)
        }
    });

    Core_ListTask_ReqAJAX.fail(function(jqXHR, textStatus) {
        console.log( "Core_ListTask_Reqfail: " + textStatus );
        FailCallBack("AJAX_FAIL")
    })
}


Core_AchiveTask=function (UserID,UserSecret,SuccCallback,FailCallBack) {
    var Core_AchiveTask_ReqAJAX=$.ajax({
        url:configure_KKWebVideoDL_API_Base_URL+"AchiveTask",
        async:true,
        cache:false,
        timeout:30000,
        type:"POST",
        data: "UserID="+UserID+"&UserSecret="+UserSecret,
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


var KKWebVideoDLApp = angular.module('KKWebVideoDLApp', []);

KKWebVideoDLApp.controller('MainCtrl', function($scope,$timeout) {
    var Langpack=Core_Lang_Out_pack();

  for(LangID in Langpack){
    $scope["UI_"+LangID]=Langpack[LangID];
  }
  $scope.tavlangs=configure_KKWebVideoDL_avlang;
  $scope.toReConnect=function(){
    User_toConnect($scope.Reconnect_input_ID,$scope.Reconnect_input_Secret);
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
    });
 
  }

  $timeout($scope.UpdSS,5000);

  Core_GetServerStatus(function(data){
        $scope.ServerStatus=data;
        $scope.$apply();}) //First hit

});