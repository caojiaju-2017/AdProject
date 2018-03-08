#!/usr/bin/env python
# -*- coding: utf-8 -*-

from include import *

class ExmapleApi(object):
    @staticmethod
    @csrf_exempt
    def CommandDispatch(req):
        command = req.GET.get('Command').upper()

    @staticmethod
    def getFunction(request):
        try:
            code = request.GET.get('code')
            state = request.GET.get('state')
        except Exception, e:
            # print u"获取code和stat参数错误"
            pass
        pass

    @staticmethod
    def postFunction(request):
        postDataList = {}
        postDataList = getPostData(request)
        pass

    @staticmethod
    def htmlRenderFunction(request):
        return render(request, 'index.html', dict)

    @staticmethod
    def apiReturnFunction(request):
        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": {}})
        return HttpResponse(loginResut)

    @staticmethod
    def allService(request):
        # 获取参数
        # 验证cookie
        #
        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": {}})
        return HttpResponse(loginResut)