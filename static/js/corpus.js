

$(document).ready(function () {
    $(".content").click(function () {
        $("#show_content").css("visibility","visible")
    });
    $(".close_content").click(function () {
        $("#show_content").css("visibility","hidden")
    });

    $("#normal-button").click(function () {
        $("#pattern").removeAttr("checked");
        $("#normal").attr({"checked": "checked"});
        $("#normal-button").addClass("active");
        $("#pattern-button").removeClass("active");
    });
    $("#pattern-button").click(function () {
        $("#normal").removeAttr("checked");
        $("#pattern").attr({"checked": "checked"});
        $("#pattern-button").addClass("active");
        $("#normal-button").removeClass("active");
    });

    $("#modern-button").click(function () {
        $("#ancient").removeAttr("checked");
        $("#modern").attr({"checked": "checked"});
        $("#modern-button").addClass("active");
        $("#ancient-button").removeClass("active");
    });
    $("#ancient-button").click(function () {
        $("#modern").removeAttr("checked");
        $("#ancient").attr({"checked": "checked"});
        $("#ancient-button").addClass("active");
        $("#modern-button").removeClass("active");
    });

    var url = document.URL;
    var match = url.match(/page=([0-9]+)/);
    var page = 1;
    if(match != null){page = match[1]}
    $("#p_"+page).addClass("active");

    var type = url.match(/search-type=([0-9]+)/);
    var t = "";
    var field = url.match(/search-field=([0-9]+)/);
    var f = "";
    if(type != null){t = type[1]}
    if(t==="1"){
        $("#normal").removeAttr("checked");
        $("#pattern").attr({"checked": "checked"});
        $("#pattern-button").addClass("active");
        $("#normal-button").removeClass("active");
    }
    else{
        $("#pattern").removeAttr("checked");
        $("#normal").attr({"checked": "checked"});
        $("#normal-button").addClass("active");
        $("#pattern-button").removeClass("active");
    }
    if(field != null){f = field[1]}
    if(f==="0"){
        $("#ancient").removeAttr("checked");
        $("#modern").attr({"checked": "checked"});
        $("#modern-button").addClass("active");
        $("#ancient-button").removeClass("active");
    }
    else {
        $("#modern").removeAttr("checked");
        $("#ancient").attr({"checked": "checked"});
        $("#ancient-button").addClass("active");
        $("#modern-button").removeClass("active");
    }


});

