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
        }
    });

    Core_NewUser_ReqAJAX.fail(function(jqXHR, textStatus) {
        console.log( "Core_NewUser_Reqfail: " + textStatus );
        FailCallBack("AJAX_FAIL")
    })
}


Core_GetServerStatus=function (SuccCallback,FailCallBack) {
    var Core_NewUser_ReqAJAX=$.ajax({
        url:configure_KKWebVideoDL_API_Base_URL+"GetServerStatus",
        async:true,
        cache:false,
        timeout:30000,
        type:"POST",
        data: "",
    });

    Core_NewUser_ReqAJAX.done(function(msg) {
        console.log( "Core_GetServerStatus_Reqsucc");
        console.log( msg );
        ServerRespond=msg
        if(ServerRespond.Success!="YES"){
            FailCallBack(ServerRespond.Reason)
        }else{
            SuccCallback(msg)
        }
    });

    Core_NewUser_ReqAJAX.fail(function(jqXHR, textStatus) {
        console.log( "Core_GetServerStatus_Reqfail: " + textStatus );
        FailCallBack("AJAX_FAIL")
    })
}

Core_UserDisable=function (TargetUserID,UserID,UserSecret,SuccCallback,FailCallBack) {
    var Core_NewUser_ReqAJAX=$.ajax({
        url:configure_KKWebVideoDL_API_Base_URL+"UserDisable",
        async:true,
        cache:false,
        timeout:30000,
        type:"POST",
        data: "",
    });

    Core_NewUser_ReqAJAX.done(function(msg) {
        console.log( "Core_UserDisable_Reqsucc");
        console.log( msg );
        ServerRespond=msg
        if(ServerRespond.Success!="YES"){
            FailCallBack(ServerRespond.Reason)
        }else{
            SuccCallback(msg)
        }
    });

    Core_NewUser_ReqAJAX.fail(function(jqXHR, textStatus) {
        console.log( "Core_UserDisable_Reqfail: " + textStatus );
        FailCallBack("AJAX_FAIL")
    })
}


Core_initLang=function(lang){
    var initLang_AJAX=$.ajax({
        dataType: "json",
        url: 'ajax/lang_'+lang+'.json',
        async:true,

    }
    ).done(function(langms){
        sessionStorage.langtrs=JSON.stringify(langms);});

}

Core_Lang_Out=function(shortdes){
    return JSON.parse(sessionStorage.langtrs)[shortdes];
}