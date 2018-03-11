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
        elif command == "Add_Vip".upper():
            return VipCustomApi.addVipData(req)
        elif command == "Modi_Vip".upper():
            return VipCustomApi.modiVipData(req)
        elif command == "Dele_Vip".upper():
            return VipCustomApi.deleteVipData(req)
        elif command == "Get_VipInfo".upper():
            return  VipCustomApi.GetVipInfo(req)

    @staticmethod
    def openVipHome(request):
        dict = {}
        return render(request, 'VipHome.html', dict)

    @staticmethod
    def openVipDetail(request):
        dict = {}
        return render(request, 'VipChange.html', dict)

    @staticmethod
    @csrf_exempt
    def uploadFile(request):
        try:
            code = request.GET.get('code')
        except Exception, e:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 2999, "Result": {}})
            return HttpResponse(loginResut)

        myFile = request.FILES.get("file", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")

        destination = os.path.join(STATIC_ROOT, "VipHome")
        destination = os.path.join(destination, "Images")
        destination = destination.encode('utf-8')
        destination = open(os.path.join(destination, code + ".png"), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()

        return HttpResponse(myFile.name)
        pass

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


        dataList = []
        vips = ByVipTable.objects.all()
        for oneVip in vips:
            oneData= {}
            oneData["id"] = oneVip.id
            oneData["code"] = oneVip.code
            oneData["username"] = oneVip.name
            oneData['sex'] = oneVip.sex
            oneData['city'] = oneVip.city
            oneData['experience'] = oneVip.score
            oneData['classify'] = oneVip.classify
            oneData['wealth'] = oneVip.wealth

            if oneVip.notify == 1:
                oneData['notify'] = "是"
            else:
                oneData['notify'] = "否"

            dataList.append(oneData)
        dict["count"] = len(vips)
        dict["data"] = dataList

        lResut = json.dumps(dict)
        return HttpResponse(lResut)

    @staticmethod
    def addVipData(request):
        postDataList = {}
        postDataList = getPostData(request)

        newVip = True
        code = None
        try:
            code = postDataList['code']
        except:
            pass

        try:
            title = postDataList['title']
            city = postDataList['city']
            score = postDataList['score']
            profession = postDataList['profession']
            deposity = postDataList['deposity']
            postmsgflag = postDataList['postmsgflag']
            sex = postDataList['sex']
        except Exception,ex:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 9999, "Result": {}})
            return HttpResponse(loginResut)

        vipHandle = None
        if code:
            vipHandle = ByVipTable.objects.filter(code = code).first()

        if not vipHandle:
            vipHandle = ByVipTable()
            vipHandle.code = uuid.uuid1().__str__().replace("-", "")

        vipHandle.name = title
        vipHandle.city = city
        vipHandle.score = score
        vipHandle.classify = profession
        vipHandle.wealth = deposity
        vipHandle.notify = postmsgflag
        vipHandle.sex = sex

        try:
            vipHandle.save()
        except:
            loginResut = json.dumps({"ErrorInfo": "数据存储错误", "ErrorId": 29999, "Result": {}})
            return HttpResponse(loginResut)

        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": vipHandle.code})
        return HttpResponse(loginResut)

    @staticmethod
    def modiVipData(request):
        pass

    @staticmethod
    def deleteVipData(request):
        postDataList = {}
        postDataList = getPostData(request)
        code = None
        try:
            code = postDataList['code']
        except Exception, ex:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 9999, "Result": {}})
            return HttpResponse(loginResut)

        vipData = ByVipTable.objects.filter(code = code).first()

        if vipData:
            try:
                vipData.delete()
            except Exception,ex:
                loginResut = json.dumps({"ErrorInfo": "数据删除失败", "ErrorId": 1999, "Result": {}})
                return HttpResponse(loginResut)


        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": None})
        return HttpResponse(loginResut)

    @staticmethod
    def GetVipInfo(request):
        try:
            code = request.GET.get('code')
        except Exception, e:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 2999, "Result": {}})
            return HttpResponse(loginResut)

        vipHandle = ByVipTable.objects.filter(code = code).first()

        if not vipHandle:
            loginResut = json.dumps({"ErrorInfo": "未找到VIP数据", "ErrorId": 1999, "Result": {}})
            return HttpResponse(loginResut)

        oneData = {}
        oneData["id"] = vipHandle.id
        oneData["code"] = vipHandle.code
        oneData["username"] = vipHandle.name
        oneData['sex'] = vipHandle.sex
        oneData['city'] = vipHandle.city
        oneData['experience'] = vipHandle.score
        oneData['classify'] = vipHandle.classify
        oneData['wealth'] = vipHandle.wealth
        oneData['notify'] = vipHandle.notify

        lResut = json.dumps(oneData)
        return HttpResponse(lResut)