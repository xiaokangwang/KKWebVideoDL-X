var Get_AJAX=$.ajax({
        dataType: "json",
        url: 'ajax/CheckURL.json',
        async:false,
    }
    ).done(function(datas){
        sessionStorage.URLRegExp=JSON.stringify(datas);});
var checkinputer=function(event) {
  var el = event.target;
  var str=el.value;
  var finded=false;
  if (str=="")
  {
    modifydivURLNotice("{{UI_Task_penel_Blank}}");
    return;
  }
  $.each(jQuery.parseJSON(sessionStorage.URLRegExp),function(i,o)
  {
    var reg = new RegExp(o);
    if(reg.test(str))
    {
      modifydivURLNotice(i);
	  finded=true;
      return;
    }
  });
  if(!finded)
  modifydivURLNotice("{{UI_Task_penel_Download_As_File}}");
  //Download as a file
  return;
}
var modifydivURLNotice=function(str)
{
	var contain=document.getElementById("URLNotice");
	contain.innerHTML=str;
}
$("#weburladd").blur(checkinputer);
