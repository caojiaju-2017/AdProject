var code = "";
window.onload=function()
{
};

$(document).ready(function(e) {
    // 如果cookie已超时，则返回登陆页面
    // $.initNewVip();
    //
    code = $.GetQueryString("code");
    $.loadVipInfo(code);
    // var username = $.GetQueryString("username");
    // if (code != "" && code != "null")
    // {
    //     $("#title").val(username);
    // }
    // else
    // {
    //     $("#title").val("测试Vip");
    // }
    //
    // var sex = $.GetQueryString("sex");
    // // if (code != "" && code != "null")
    // // {
    // //     $("#title").val(username);
    // // }
    // // else
    // // {
    // //     $("#title").val("测试Vip");
    // // }
    //
    // var city = $.GetQueryString("city");
    // if (code != "" && code != "null")
    // {
    //     $("#city").val(city);
    // }
    // else
    // {
    //     $("#city").val("成都");
    // }
    //
    // var experience = $.GetQueryString("experience");
    // if (code != "" && code != "null")
    // {
    //     $("#score").val(experience);
    // }
    // else
    // {
    //     $("#score").val("10365");
    // }
    //
    // var classify = $.GetQueryString("classify");
    // if (code != "" && code != "null")
    // {
    //     $("#profession").val(classify);
    // }
    // else
    // {
    //     $("#profession").val("企业老板");
    // }
    //
    // var wealth = $.GetQueryString("wealth");
    // if (code != "" && code != "null")
    // {
    //     $("#deposity").val(wealth);
    // }
    // else
    // {
    //     $("#deposity").val("1020000");
    // }
});

$.extend({

    GetQueryString:function (name)
    {
         var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
         var r = window.location.search.substr(1).match(reg);
         if(r!=null)return  unescape(r[2]); return null;
    },

    selectVipImage: function () {
        if (code == "" || code == "null" || code == null )
        {
            alert("请先创建账户，并保存。")
            return;
        }


    },

    getVipCode:function(){
      return code;
    },
    loadVipInfo:function(vipcode)
    {
        var cmdString = "/api/ctm/?Command=Get_VipInfo&code=" + vipcode;
        // 提取用户名
        $.get(cmdString,
            function (data) {
                // 检查查询状态
                    code = data.code;
                    $("#title").val(data.username);
                    $("#city").val(data.city);
                    $("#score").val(data.experience);
                    $("#profession").val(data.classify);
                    $("#deposity").val(data.wealth);


                    $("#sex_wrap input[name='sex'][value='" + data.sex + "']").prop("checked", "checked");

                    if (data.notify == 0)
                    {
                        $('#msgpush').prop('checked',false);
                    }
                    else
                    {
                        $('#msgpush').prop('checked',true);
                    }

            },
            "json");//这里返回的类型有：json,html,xml,text
    },
    initNewVip:function(){
        $("#title").val("测试Vip");
        $("#city").val("成都");
        $("#score").val("10900");
        $("#profession").val("企业老板");
        $("#deposity").val("1020000");
        // $("#msgpush").val("曹家驹");
        $("#male").check = true;
    },

    saveVipInfo: function () {

        var title = $("#title").val();
        var city = $("#city").val();
        var score = $("#score").val();
        var profession = $("#profession").val();
        var deposity = $("#deposity").val();

        // 获取性别
        var sex_select = $('#sex_wrap input[name="sex"]:checked ').val();

        var checkPostMsg = $('#msgpush').is(":checked");

        var sendFlag = 0;
        if (checkPostMsg)
        {
            sendFlag = 1;
        }
        // //设置选中
        // $('#cb').prop('checked',true);
        // 获取是否推送消息
        // alert(checkPostMsg);


        var rtnCmd = "/api/ctm/?Command=Add_Vip";
        var params = null;
        if (code != "" && code != "null")
        {
            params = {title: title, city: city,score:score,profession:profession,deposity:deposity,postmsgflag:sendFlag,sex:sex_select,code:code};
        }
        else
        {
            params = {title: title, city: city,score:score,profession:profession,deposity:deposity,postmsgflag:sendFlag,sex:sex_select}
        }
        $.post(rtnCmd, params,
            function (data)
            {

                var  ErrorId = data.ErrorId;
                var  Result = data.Result;

                if (ErrorId == 200)
                {
                    alert("操作成功!");
                    var index = parent.layer.getFrameIndex(window.name);
                    parent.layer.close(index);
                    parent.location.reload();
                }
                else
                {
                    alert(data.ErrorInfo);
                }

            },
            "json");
    },
});