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
});