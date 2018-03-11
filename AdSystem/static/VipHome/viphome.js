var openidTemp;

window.onload=function()
{
    var docHeight = $(document).height();
    $("#vip_div").height(docHeight - 140);
    // $("#demo").height(docHeight - 140);

    // var table = layui.table;
    // layer.style('height',docHeight - 140);
};

$(document).ready(function(e) {
    // 如果cookie已超时，则返回登陆页面
});

$.extend({
    exitSystem: function () {
        alert("退出功能已关闭")
    },
    openVipInfo:function(data)
    {
        layer.open({
            title: ['VIP资料修改', 'font-size:13px;margin-top:10px;'],
            type: 2,
            area: ['500px', '700px'],
            content: 'VipChange.html?code='+ data.code
        });
    },
    removeVip:function(data){
        var rtnCmd = "/api/ctm/?Command=Dele_Vip";

        $.post(rtnCmd, {code: data.code},
            function (data)
            {

                var  ErrorId = data.ErrorId;
                var  Result = data.Result;

                if (ErrorId == 200)
                {
                    //alert("删除成功!");
                }
                else
                {
                    alert(data.ErrorInfo);
                }

            },
            "json");
    },
    newVip: function () {
    //     layer.open({
    //         type: 2,
    //         title: ['个人资料-修改', 'font-size:13px;margin-top:10px;'],
    //         content: "/api/ctm/?",//con是Ajax返回的页面
    //         btn: ['确定修改', '取消'],
    //         area: ['800px', '600px'],
    //         shade: false,
    //         maxmin: true,
    //         anim: 2,
    //         yes: function (index, layero) {
    //             $("#form").length;//直接获取表单长度=0
    //             $(layero).find("#form").length;//表单长度还是等于0
    //         }
    //     })

        layer.open({
            title: ['VIP资料管理', 'font-size:13px;margin-top:10px;'],
            type: 2,
            area: ['500px', '700px'],
            content: 'VipChange.html' //这里content是一个URL，如果你不想让iframe出现滚动条，你还可以content: ['http://sentsin.com', 'no']
        });
    }
});