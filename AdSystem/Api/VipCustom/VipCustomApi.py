#!/usr/bin/env python
# -*- coding: utf-8 -*-

from include import *

class VipCustomApi(object):
    @staticmethod
    @csrf_exempt
    def CommandDispatch(req):
        command = req.GET.get('Command').upper()

        if command == "List_VipDatas".upper():
            return VipCustomApi.listVipDatas(req)

    @staticmethod
    def openVipHome(request):
        dict = {}
        return render(request, 'VipHome.html', dict)

    @staticmethod
    def getLastNotify(request):
        # pad主动获取 最新通知
        # 命令吗： GET_LAST_NOTIFY
        # 参数：   padcode=abc0001
        # api/ctm/?Command=GET_LAST_NOTIFY&padcode=abc0001
        # by_notify_message

        # 伪代码
        # 提取参数
        # 查询该pad最后一次数据
        # 根据最新数据， 并将数据返回给pad

        pass

    @staticmethod
    def postFaceData(request):
        # post
        # 命令吗： POST_FACE_DATA
        # 参数：imagedata
        # api/ctm/?Command=POST_FACE_DATA

        # 提取图片数据
        # 匹配当前vip数据

        # 如果老vip，则记录客户数据到 by_notify_messages
        # 如果是新用户， 则记录客户资料到  by_notify_message
        pass

    @staticmethod
    def listVipDatas(request):
        # {field: 'id', title: 'ID', width: 80, sort: true, fixed: 'left'}
        # , {field: 'username', title: '用户名', width: 80}
        # , {field: 'sex', title: '性别', width: 80, sort: true}
        # , {field: 'city', title: '城市', width: 80}
        # , {field: 'experience', title: '积分', width: 80, sort: true}
        # , {field: 'classify', title: '职业', width: 80}
        # , {field: 'wealth', title: '财富', width: 135, sort: true}

        dict = {}
        dict["code"] = 0
        dict["msg"] = "success"
        dict["count"] = 20

        dataList = []

        for index in range(20):
            oneData= {}
            oneData["id"] = 100 + index
            oneData["username"] = "ccc"
            oneData['sex'] = "男"
            oneData['city'] = '成都'
            oneData['experience'] = 1009
            oneData['classify'] = "医生"
            oneData['wealth'] = 290020
            dataList.append(oneData)

        dict["data"] = dataList

        lResut = json.dumps(dict)
        return HttpResponse(lResut)

    @staticmethod
    def addVipData(request):
        pass

    @staticmethod
    def modiVipData(request):
        pass

    @staticmethod
    def deleteVipData(request):
        pass
