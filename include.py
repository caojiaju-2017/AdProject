#!/usr/local/bin/python
#-*- coding:utf-8 -*-

import httplib
import urllib
import datetime
import threading
import md5
import random
import os
import inspect
import hashlib
import base64
import pickle
import socket
import sys
import platform
import time
import json
import uuid
import re
import et
import qrcode
import urllib2
import requests
from django.template import Template, Context
from HsPlatform.Sms.HsSmsHelp import *
from HsPlatform.Sms.MobileRecord import *

# DJANGO 引用
from django.shortcuts import render,render_to_response
from django.http import  HttpResponse
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
from django.template import Template, Context
from AdSystem.models import *
from AdSystem.Api.PublicService import *

import logging
import json,uuid,time,base64,re,urllib
from django.shortcuts import render,render_to_response
from django.http import  HttpResponse,HttpResponseRedirect

from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
import qrcode,urllib2,requests
from django.db.models import F
from django.db.models import Q
from AdSystem.models import *
import xml.etree.ElementTree as ET

from AdSystem.Api.BaseEmail import *

logger = logging.getLogger('django')


# 写日志
def HsWriteLog(message):
    return
    global logger
    logger.error(message)

# 获取post参数
def getPostData(request):
    postDataList = {}
    if request.method == 'POST':
        for key in request.POST:
            try:
                postDataList[key] = request.POST.getlist(key)[0]
            except:
                pass

    import json
    if not postDataList or len(postDataList) == 0:
        try:
            bodyTxt = request.body
            postDataList = json.loads(bodyTxt)
        except Exception,ex:
            pass

    return  postDataList


# 事务提交变更
def commitCustomDataByTranslate(objHandles):
    with transaction.atomic():
        for oneObject in objHandles:
            if not oneObject.dbHandle:
                continue

            try:
                if oneObject.operatorType == 0:
                    oneObject.dbHandle.save()
                elif oneObject.operatorType == 1:
                    oneObject.dbHandle.delete()
            except Exception,ex:
                return  False

    return True