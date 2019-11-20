var editing = '';

function add_section(elem, auto_add_paragraph) {
    var current_id = parseInt(elem.attr("id").split("_")[1]);
    var next_id = current_id + 1;
    var section = "       <tr class=\"tr_btn\" id=\"section_" + next_id + "\">\n" +
        "                    <td></td>\n" +
        "                    <td class=\"center\">章节</td>\n" +
        "                    <td></td>\n" +
        "                    <td><span onclick=\"edit(this, 0)\" class=\"text_span col-md-2 sp_1 title\">标题：</span> <span onclick=\"edit(this, 0)\" class=\"text_span col-md-2 sp_2 author\">作者：</span><span onclick=\"edit(this, 0)\" class=\"text_span col-md-2 sp_3 dynasty\">时期：</span><span onclick=\"edit(this, 0)\" class=\"text_span col-md-2 sp_4 category\">类别：</span>\n" +
        "                        <div class=\"btn-group btn_config\">\n" +
        "                            <button class=\"btn btn-default btn-xs\" type=\"button\" onclick=\"add_section($(this).parent().parent().parent(), true);\">章</button>\n" +
        "                            <button class=\"btn btn-default btn-xs\" type=\"button\" onclick=\"add_paragraph($(this).parent().parent().parent());\">段</button>\n" +
        "                            <button class=\"btn btn-default btn-xs\" type=\"button\" onclick=\"remove_section($(this).parent().parent().parent());\">删</button>\n" +
        "                        </div>\n" +
        "                    </td>\n" +
        "                </tr>";
    $("tr[id^=section_]").each(function () {
        var elem_id = parseInt($(this).attr("id").split("_")[1]);
        var elem_id_after = elem_id+1;
        if (elem_id > current_id){
            $(this).attr({"id": "section_" + elem_id_after})
        }
    });
    var p_count = 0;
    $("tr[id^=paragraph_" + current_id + "_]").each(function () {
        p_count ++;
    });
    $("tr[id^=paragraph_]").each(function () {
        var elem_id = parseInt($(this).attr("id").split("_")[1]);
        var elem_postfix = "_" + $(this).attr("id").split("_")[2];
        var elem_id_after = elem_id+1;
        if (elem_id > current_id){
            $(this).attr({"id": "paragraph_" + elem_id_after + elem_postfix})
        }
    });
    if(p_count===0){
        $(elem).after(section);
        auto_add_paragraph? add_paragraph(elem.next(), 0):1;
    }
    else{
        var target_elem = $("#paragraph_" + current_id + "_" +p_count);
        target_elem.next().after(section);
        auto_add_paragraph? add_paragraph(target_elem.next().next(), 0):1;
    }
    set_default($(elem).next());
}

function remove_section(elem) {
    var current_id = parseInt(elem.attr("id").split("_")[1]);
    $("tr[id^=section_]").each(function () {
        var elem_id = parseInt($(this).attr("id").split("_")[1]);
        var elem_id_after = elem_id-1;
        if (elem_id > current_id){
            $(this).attr({"id": "section_" + elem_id_after})
        }
    });
    $("tr[id^=paragraph_" + current_id + "]").each(function () {
        $(this).next().remove();
        $(this).remove();
    });
    $("tr[id^=paragraph_]").each(function () {
        var elem_id = parseInt($(this).attr("id").split("_")[1]);
        var elem_postfix = $(this).attr("id").substring($(this).attr("id").lastIndexOf("_"));
        var elem_id_after = elem_id-1;
        if (elem_id > current_id){
            $(this).attr({"id": "paragraph_" + elem_id_after + elem_postfix})
        }
    });
    $(elem).remove()
}

function add_paragraph(elem) {
    var current_id = "";
    var id_prefix = "";
    if($(elem).attr("id")!==undefined&&$(elem).attr("id").indexOf("section_")>=0){
        id_prefix = "paragraph_" + $(elem).attr("id").split("_")[1];
        current_id = 0;
    }
    else{
        id_prefix = $(elem).attr("id").substring(0, $(elem).attr("id").lastIndexOf("_"));
        current_id = parseInt($(elem).attr("id").split("_")[$(elem).attr("id").split("_").length-1]);
    }
    var next_id = current_id + 1;
    var paragraph = "    <tr class=\"tr_btn\" id=\"" + id_prefix + "_" + next_id + "\">\n" +
        "                    <td></td>\n" +
        "                    <td></td>\n" +
        "                    <td class=\"center\">段</td>\n" +
        "                    <td><span onclick=\"edit(this, 0)\" class=\"text_span col-md-2 sp_2 col-md-offset-2 author\">作者：</span><span onclick=\"edit(this, 0)\" class=\"text_span col-md-2 sp_3 dynasty\">时期：</span><span onclick=\"edit(this, 0)\" class=\"text_span col-md-2 sp_4 category\">类别：</span>\n" +
        "                        <div class=\"btn-group btn_config\">\n" +
        "                            <button class=\"btn btn-default btn-xs\" type=\"button\" onclick=\"add_paragraph($(this).parent().parent().parent());\">段</button>\n" +
        "                            <button class=\"btn btn-default btn-xs\" type=\"button\" onclick=\"remove_paragraph($(this).parent().parent().parent());\">删</button>\n" +
        "                        </div></td>\n" +
        "                </tr>" +
        "                <tr>\n" +
        "                    <td></td>\n" +
        "                    <td></td>\n" +
        "                    <td></td>\n" +
        "                    <td class=\"text_div\"><span onclick=\"edit(this, 1)\" class=\"text_span col-md-12 sp_1 input_area\" >文本：</span></td>\n" +
        "                </tr>";
    $("tr[id^=" + id_prefix+ "]").each(function () {
        var this_id = $(this).attr("id");
        var elem_id = parseInt(this_id.split("_")[this_id.split("_").length-1]);
        var elem_id_after = elem_id+1;
        if (elem_id > current_id){
            $(this).attr({"id": this_id.substring(0, this_id.lastIndexOf("_")+1) + elem_id_after})
        }
    });
    if(current_id===0){$(elem).after(paragraph);set_default($(elem).next())}
    else{$(elem).next().after(paragraph);set_default($(elem).next().next());}

    // alert($(elem).next().attr("class"));
    // alert(1)
}

function remove_paragraph(elem) {
    var current_id = parseInt(elem.attr("id").split("_")[elem.attr("id").split("_").length-1]);
    var id_prefix = elem.attr("id").substring(0, elem.attr("id").lastIndexOf("_"));
    $("tr[id^=" + id_prefix+ "]").each(function () {
        var elem_id = parseInt($(this).attr("id").split("_")[elem.attr("id").split("_").length-1]);
        var elem_id_after = elem_id-1;
        if (elem_id > current_id){
            $(this).attr({"id": id_prefix + "_" + elem_id_after})
        }
    });
    if(current_id!==0){$("#"+elem.attr("id")).next().remove()}
    $("#"+elem.attr("id")).remove();
}

function edit(span, type){
    remove_select();
    forever_elem.blur();
    focus_elem = $(span);
    var text = $(span).text().trim();
    var pos_split = text.indexOf('：');
    var attr = text.substring(0, pos_split);
    var value = text.substring(pos_split+1);
    forever_elem.attr({"placeholder": attr});
    forever_elem.val(value);
    locate_input();
    editing = true;
    if(type===0) {
        input_elem.focus();
        input_elem.css({"z-index":100});
        input_elem.attr({"value": value, "placeholder": attr});
        input_elem.blur(function () {
            input_elem.css({"z-index":-100});
        })
    }
    else{
        textarea_elem.focus();
        textarea_elem.css({"z-index":100, "width": $(".input_area").eq(0).outerWidth()});
        textarea_elem.attr({"placeholder": attr});
        textarea_elem.text(value);
        textarea_elem.blur(function () {
            textarea_elem.css({"z-index":-100});
        });
    }
    if(focus_elem.text().split("：")[0]==="类别"){
        $(".list-group").children(".active").removeClass("active");
        $(".list-group").css({"z-index":500});
        locate_list()
    }
    forever_elem.blur(function () {
        editing = false;
    })
}

function gather_data(){
    var data = {};
    $(".tr_btn").each(function () {
        var id_val = $(this).attr("id").substring($(this).attr("id").indexOf("_")+1).replace('_','.');
        var id = "";
        if(id_val!=="0"){id = document_id + "." + id_val}
        else{id = document_id}
        var title = "";
        var author = "";
        var dynasty = "";
        var category = "";
        var text = "";
        var update_user = $("#user_name").val();
        $("#" + $(this).attr("id") + " .text_span").each(function () {
            var attr = $(this).text().substring(0, $(this).text().indexOf("："));
            var value = $(this).text().substring($(this).text().indexOf("：")+1).trim();
            switch (attr){
                case "标题":
                    title = value.trim();
                    break;
                case "作者":
                    author = value.trim();
                    break;
                case "时期":
                    dynasty = value.trim();
                    break;
                case "类别":
                    category = value.trim();
                    break;
            }
        });
        if($(this).attr("id").indexOf("paragraph_")>=0){
            var text_elem = $(this).next().children(".text_div").children(".text_span");
            text = text_elem.text().substring(text_elem.text().indexOf('：')+1).trim();
        }
        if(id.indexOf('.')<0){
            data[id] = {"document": title, "author": author, "dynasty": dynasty, "category": category, "username": update_user};
        }
        else if(id.split('.').length===2){
            data[id] = {"section": title, "author": author, "dynasty": dynasty, "category": category};
        }
        else{
            data[id] = {"author": author, "dynasty": dynasty, "category": category, "text":text};
        }
    });
    alert(JSON.stringify(data));
    return data;
}

function data_submit(json_data, link){
    // if (data_check(json_data)){
        $.post(link, JSON.stringify(json_data),function () {
            window.location.href = "/corpus/manage";
        });
    // }
}

function data_check(json_data){
    var messages = [];
    var confirm = true;
    for (var key in json_data){
        if(!json_data.hasOwnProperty(key)) continue;
        var key_type = key.split(".").length;
        if (key_type === 1){
            if (json_data[key]['document']===""){
                messages.push({"id": "section_0", "message": "文档标题不能为空"});
                $("#section_0").addClass("alert alert-danger");
                confirm = false;
            }
        }
        if (key_type === 2){
            if (json_data[key]['section']==="") {
                var section_id = 'section_' + key.split('.')[1];
                var row = {};
                row["id"] = section_id;
                row["message"] = "章节标题不能为空";
                messages.push(row);
                $("#"+section_id).addClass("alert alert-danger");
                confirm = false;
            }
        }
        if (key_type === 3){
            if (json_data[key]['text']==="") {
                var paragraph_id = 'paragraph_' + key.split('.')[1] + '_' + key.split('.')[2]
                var row = {};
                row["id"] = paragraph_id;
                row["message"] = "文本内容不能为空";
                messages.push(row);
                $("#"+paragraph_id).next().addClass("alert alert-danger");
                confirm = false;
            }
        }
    }
    if (messages.length>0){
        var href_elem = $("#"+messages[0]["id"]);
        $("html,body").animate({scrollTop: href_elem.offset().top-$(window).height()*0.5-href_elem.height()*0.5}, 1000);
    }

    // var str_msg = '';
    // for(var i in messages){
    //     str_msg += JSON.stringify(messages[i]);
    // }
    // alert(str_msg);
    return confirm;
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // 这些HTTP方法不要求CSRF包含
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function event_binding () {
    var text = focus_elem.text().trim();
    var pos_split = text.indexOf('：');
    var attr = text.substring(0, pos_split);
    var value = text.substring(pos_split+1);
    forever_elem.val(value);
    forever_elem.attr({"placeholder": attr});

    forever_elem.blur(function () {
        var elem = "";
        if(focus_elem.attr("class").indexOf("input_area")>=0)
            elem = textarea_elem;
        else
            elem = input_elem;
        var attr = elem.attr("placeholder");
        var val = elem.val().trim();
        forever_elem.css({"z-index":-100});
        focus_elem.html(attr+"："+val);
        editing = false;
        if(focus_elem.attr("class").indexOf("default_")>=0){
             // alert(1);
            set_default();
        }
    });
    $(document).keydown(function (ev) {
        var input_event = false;
        var move_event = false;
        var keyCode = ev.keyCode;
        var preventKeyCodeArr = [37, 38, 39, 40, 9, 13, 18, 8];
        var letterKeyCodeArr = new Array(46);
        for (var l = 48, c = 0; l <= 90; l++, c++){letterKeyCodeArr[c] = l;}
        letterKeyCodeArr[43] = 8;
        letterKeyCodeArr[44] = 229;
        for (var i in preventKeyCodeArr){
            if(keyCode === preventKeyCodeArr[i]){
                if(editing&&keyCode!==9){
                    if($(".list-group").css("z-index")<0){
                        continue;
                    }
                }
                if(keyCode===8&&!ev.altKey){continue}
                ev.preventDefault();
                move_event = true;
                if($(".selected").length===0){focus_elem = $("#document_attr span:first");}
                forever_elem.blur();
                var pos_in_td = 1;
                var next_elem = '';
                var current_elem = focus_elem;
            }
        }
        for (var j in letterKeyCodeArr){
            if (keyCode === letterKeyCodeArr[j]){
                if(keyCode===8&&ev.altKey){continue}
                input_event = true;
                editing = true;
                if(focus_elem.text().split("：")[0]==="类别"){
                    $(".list-group").children(".active").removeClass("active");
                    $(".list-group").css({"z-index":500});
                    locate_list()
                }
                focus_elem.text("<input>");
                if(focus_elem.attr("class").indexOf("input_area")>=0){
                    textarea_elem.css({"z-index":100, "width": $(".input_area").eq(0).outerWidth()});
                }
                else{
                    input_elem.css({"z-index":100});
                }
                // alert(focus_elem.text().split("：")[0]);
            }
        }
        if(move_event === true){
            switch (event.keyCode){
                //方向键左
                case 37:
                    if($(".list-group").css("z-index")>0) break;
                    next_elem = current_elem.prev();
                    if(next_elem.length>0){
                        focus_elem = next_elem;
                        locate_input();
                    }
                    break;
                //方向键上
                case 38:
                    //出现列表时的操作
                    var list_elem = $(".list-group");
                    if(list_elem.css("z-index")>0){
                        if(list_elem.children(".active").length===0){}
                        else{
                            var active_elem = list_elem.children(".active");
                            if(active_elem.prev().length>0){
                                active_elem.prev().addClass("active");
                                active_elem.removeClass("active");
                            }
                        }
                        input_elem.val(list_elem.children(".active").text().trim());
                        focus_elem.text("类别："+list_elem.children(".active").text().trim());
                        break;
                    }

                    pos_in_td = parseInt(current_elem.attr("class").split(' ')[2].split('_')[1])-1;
                    next_elem = current_elem.parent().parent().prev().find("td:eq(3) span:eq(" + pos_in_td + ")");
                    while(pos_in_td>=0&&next_elem.length===0){
                        pos_in_td --;
                        next_elem = current_elem.parent().parent().prev().find("td:eq(3) span:eq(" + pos_in_td + ")");
                    }
                    if(next_elem.length>0){
                        focus_elem = next_elem;
                        locate_input();
                    }
                    break;
                //方向键右
                case 39:
                    if($(".list-group").css("z-index")>0) break;
                    next_elem = current_elem.next();
                    if(next_elem.length>0&&next_elem.prop("tagName")==="SPAN"){
                        focus_elem = next_elem;
                        locate_input();
                    }
                    break;
                //方向键下
                case 40:
                    //出现列表时的操作
                    var list_elem = $(".list-group");
                    if(list_elem.css("z-index")>0){
                        if(list_elem.children(".active").length===0){
                            list_elem.children("a").eq(0).addClass("active");
                        }
                        else{
                            var active_elem = list_elem.children(".active");
                            if(active_elem.next().length>0){
                                active_elem.next().addClass("active");
                                active_elem.removeClass("active");
                            }
                        }
                        input_elem.val(list_elem.children(".active").text().trim());
                        focus_elem.text("类别："+list_elem.children(".active").text().trim());
                        break;
                    }

                    pos_in_td = parseInt(current_elem.attr("class").split(' ')[2].split('_')[1]);
                    next_elem = current_elem.parent().parent().next().find("td:eq(3) [class*=sp_" + pos_in_td + "]");
                    while(pos_in_td>1&&next_elem.length===0){
                        pos_in_td --;
                        next_elem = current_elem.parent().parent().next().find("td:eq(3) [class*=sp_" + pos_in_td + "]");
                    }
                    if(current_elem.parent().parent().next().find("td:eq(3) [class*=sp_1]").length===0&&parseInt(current_elem.attr("class").split(' ')[2].split('_')[1])<=2)
                        next_elem = current_elem.parent().parent().next().find("td:eq(3) [class*=sp_2]");
                    if(next_elem.length>0){
                        focus_elem = next_elem;
                        locate_input();
                    }
                    break;
                //tab
                case 9:
                    //向右寻找
                    next_elem = current_elem.next();
                    if(next_elem.length===0||next_elem.prop("tagName")!=="SPAN"){
                        //下一列第一个
                        next_elem = current_elem.parent().parent().next().find("td:eq(3) span:eq(0)");
                    }
                   if(next_elem.length>0){
                        $(".list-group").css("z-index", -666);
                        focus_elem = next_elem;
                        locate_input();
                    }
                    //没有下一层的元素
                   else {
                        //如果是text
                        if(current_elem.parent().parent().attr("id")===undefined){
                            add_paragraph(current_elem.parent().parent().prev());
                        }//如果id是section
                        else{
                        //如果是id=section_0，不允许创建paragraph，创建section
                            if(current_elem.parent().parent().attr("id")!=="section_0"){
                                add_paragraph(current_elem.parent().parent())
                            }else{
                                add_section(current_elem.parent().parent(),true)
                            }
                        }
                   }
                   break;
                //enter
                case 13:
                    if($(".list-group").css("z-index")>0) {
                        $(".list-group").css("z-index", -666);
                        break;
                    }
                    next_elem = current_elem.parent().parent();
                    if(event.altKey){
                        if(next_elem.attr("id")===undefined){
                            var section_id = parseInt(next_elem.prev().attr("id").split("_")[1]);
                            var current_section = $("#section_"+section_id);
                            add_section(current_section, true);
                            var next_section_id = section_id+1;
                            focus_elem = $("#section_"+next_section_id).find("td .text_span").eq(0);
                        }
                         else if(next_elem.attr("id").indexOf('section_')>=0){
                            add_section(next_elem, true);
                            var next_section_id = parseInt(next_elem.attr("id").split("_")[1])+1;
                            var next_section = $("#section_"+next_section_id);
                            focus_elem = next_section.find("td .text_span").eq(0);
                        }
                        else {
                            var section_id = parseInt(next_elem.attr("id").split("_")[1]);
                            var current_section = $("#section_"+section_id);
                            add_section(current_section, true);
                            var next_section_id = section_id+1;
                            focus_elem = $("#section_"+next_section_id).find("td .text_span").eq(0);
                        }
                        locate_input();
                        break;
                    }
                    if(next_elem.attr("id")==='section_0') {
                        add_section(next_elem, true);
                        focus_elem = next_elem.next().find("td .text_span").eq(0);
                    }
                    else if(next_elem.attr("id")===undefined) {
                        add_paragraph(next_elem.prev());
                        focus_elem = next_elem.next().find("td .text_span").eq(0);
                    }
                    else {
                        add_paragraph(next_elem);
                        if(next_elem.attr("id").indexOf("section_")>=0) {
                            focus_elem = next_elem.next().find("td .text_span").eq(0);
                        }
                        else
                            focus_elem = next_elem.next().next().find("td .text_span").eq(0);
                    }
                    locate_input();
                    break;
                //backspace
                case 8:
                    if($(".list-group").css("z-index")>0) break;
                    next_elem = current_elem.parent().parent();
                    if(event.which === 8){
                        if(next_elem.attr("id")===undefined){
                            focus_elem = next_elem.prev().prev().find("td .text_span").eq(0);
                            remove_paragraph(next_elem.prev());
                        }
                        else if(next_elem.attr("id").indexOf("paragraph_")>=0){
                            focus_elem = next_elem.prev().find("td .text_span").eq(0);
                            remove_paragraph(next_elem);
                        }
                        else if(next_elem.attr("id")!==("section_0")){
                            focus_elem = next_elem.prev().find("td .text_span").eq(0);
                            remove_section(next_elem);
                        }
                    }
                    locate_input();
                    break;
            }



            if(focus_elem.attr("class").indexOf("input_area")>=0){
                textarea_elem.focus();
            }
            else{
                input_elem.focus();
            }

            var text = focus_elem.text().trim();
            var pos_split = text.indexOf('：');
            var attr = text.substring(0, pos_split);
            var value = text.substring(pos_split+1);
            forever_elem.val(value);
            forever_elem.attr({"placeholder": attr});
            select();
        }
    });
}

function set_default(elem) {
    function get_val(data) {
        return data.substring(data.indexOf('：')+1)
    }
    var default_title = $(".default_title").text().trim();
    var default_author = $(".default_author").text().trim();
    var default_dynasty = $(".default_dynasty").text().trim();
    var default_category = $(".default_category").text().trim();
    var overwrite = false;
    $("#overwrite").attr("class").indexOf("active")>=0 ? overwrite = true:overwrite = false;
    if(elem === undefined){
        if(get_val(default_title)!=="")
            $(".title").each(function () {
                if(get_val($(this).text().trim())===""||(get_val(default_title)!==""&&overwrite))
                    $(this).text(default_title);
            });
        if(get_val(default_author)!=="")
            $(".author").each(function () {
                if(get_val($(this).text().trim())===""||(get_val(default_author)!==""&&overwrite))
                    $(this).text(default_author);
            });
        if(get_val(default_dynasty)!=="")
            $(".dynasty").each(function () {
                if(get_val($(this).text().trim())===""||(get_val(default_dynasty)!==""&&overwrite))
                    $(this).text(default_dynasty);
            });
        if(get_val(default_category)!=="")
            $(".category").each(function () {
                if(get_val($(this).text().trim())===""||(get_val(default_category)!==""&&overwrite))
                    $(this).text(default_category);
            });
    }
    else{
        if(default_title) elem.find("td [class*=title]").text(default_title);
        if(default_author) elem.find("td [class*=author]").text(default_author);
        if(default_dynasty) elem.find("td [class*=dynasty]").text(default_dynasty);
        if(default_category) elem.find("td [class*=category]").text(default_category);
    }
}

function select() {
    var last_elem = $(".selected");
    last_elem.css({"border": "none"});
    last_elem.removeClass("selected");
    $(focus_elem).addClass("selected");
    $(focus_elem).css({"border": "2px solid #6495ED"});
}

function remove_select() {
    $(".selected").css({"border": ""});
}

function load_table_view(json_data) {
    if(json_data==='') return;
    var previous_is_section = false;
    // console.log(JSON.stringify(json_data));
    for(var key in json_data){
        if(!json_data.hasOwnProperty(key)) continue;
        if(key.indexOf('.')<0){
            previous_is_section = true;
            $("#document_attr").children('span').each(function () {
                // console.log(json_data[key]['document']);
                if($(this).text()==='标题：'){this.innerHTML = '标题：'+json_data[key]['document']}
                else if($(this).text()==='作者：'){this.innerHTML = '作者：'+json_data[key]['author']}
                else if($(this).text()==='时期：'){this.innerHTML = '时期：'+json_data[key]['dynasty']}
                else if($(this).text()==='类别：'){this.innerHTML = '类别：'+json_data[key]['category']}
            })
        }
        else if(key.split('.').length===2){
            previous_is_section = true;
            var section_id_pre = 'section_' + (parseInt(key.split('.')[1])-1).toString();
            var section_id = 'section_' + (parseInt(key.split('.')[1])).toString();
            add_section($("#"+section_id_pre), false);
            $("#" + section_id + " .text_span").each(function () {
                if($(this).text()==='标题：'){this.innerHTML = '标题：'+json_data[key]['section']}
                else if($(this).text()==='作者：'){this.innerHTML = '作者：'+json_data[key]['author']}
                else if($(this).text()==='时期：'){this.innerHTML = '时期：'+json_data[key]['dynasty']}
                else if($(this).text()==='类别：'){this.innerHTML = '类别：'+json_data[key]['category']}
            })
        }
        else {
            console.log(key);
            var para_id_pre = 'paragraph_' + (parseInt(key.split('.')[1])).toString() + '_' + (parseInt(key.split('.')[2])-1).toString();
            var para_id = 'paragraph_' + (parseInt(key.split('.')[1])).toString() + '_' + (parseInt(key.split('.')[2])).toString();
            var sec_id = 'section_' + (parseInt(key.split('.')[1])).toString();
            if(previous_is_section){
                add_paragraph($("#"+sec_id))
            }
            else{
                add_paragraph($("#"+para_id_pre))
            }
            $("#" + para_id + " .text_span").each(function () {
                if($(this).text()==='作者：'){this.innerHTML = '作者：'+json_data[key]['author']}
                else if($(this).text()==='时期：'){this.innerHTML = '时期：'+json_data[key]['dynasty']}
                else if($(this).text()==='类别：'){this.innerHTML = '类别：'+json_data[key]['category']}
            });
            $("#"+para_id).next().children(".text_div").children(".text_span").text('文本：' + json_data[key]['text']);
            previous_is_section = false;
        }
    }
}

function load_text_view(json_data) {
    var container = $("#document_display");
    container.text("");
    for(var k in json_data){
        if(!json_data.hasOwnProperty(k)) continue;
        var type = k.split('.').length;
        switch (type){
            case 1:
                container.append("<h3 id=\"doc_title\" class=\"center\">" + json_data[k]['document'] + "</h3><br><br>");
                break;
            case 2:
                var p_id = k.replace('.', '_');
                container.append(
                    "<p class=\"doc_section\" id=\"p_" + p_id + "\">\n" +
                    "    <span class=\"section_title\">" + json_data[k]['section'] + "</span>\n" +
                    "</p>");
                break;
            case 3:
                var p_container = $("#p_"+k.substring(0, k.lastIndexOf('.')).replace('.', '_'));
                var author = "";
                var t_type = "";
                var t_class = "";
                if(json_data[k]['author']!==""){
                    author = json_data[k]['author'];
                    t_type = json_data[k]['category'];
                    if(t_type==="原文") t_type = "";
                    else if(t_type==="注解") {
                        t_type="註 ";
                        t_class = "zhu";
                    }
                    else if(t_type==="义疏") {
                        t_type="疏 ";
                        t_class = "shu";
                    }
                }
                p_container.append(t_type + "<span class=\"section_text " + t_class + "\">" + json_data[k]['text'] + "</span>");
        }
    }
}

function text_view() {
    var button_elem = $("#view_button");
    button_elem.removeAttr("onclick");
    button_elem.attr({"onclick": "table_view()"});
    button_elem.text("表格视图");
    $("#document_table").addClass("hidden");
    $("#document_display").removeClass("hidden");
}

function table_view() {
    var button_elem = $("#view_button");
    button_elem.removeAttr("onclick");
    button_elem.attr({"onclick": "load_text_view(gather_data());text_view();"});
    button_elem.text("文本视图");
    $("#document_display").addClass("hidden");
    $("#document_table").removeClass("hidden");
}

function locate_input(){
    var input_elem = $(".forever_input");
    var top = focus_elem.offset().top;
    var left = focus_elem.offset().left;
    input_elem.css({"position": "absolute", "top": top, "left": left});
}

function locate_list(){
    var list_elem = $(".list-group");
    var top = focus_elem.offset().top+input_elem.height();
    var left = focus_elem.offset().left;
    list_elem.css({"position": "absolute", "top": top, "left": left, 'width':input_elem.width()});
}

function reset_table(){
    var container = $("#main_container");
    container.html(table_cache);
}



