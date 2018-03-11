#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TEMPLATE_DIRS ['E:\\GitWorkSpace\\NewEducation\\4.Code\\Education\\HsEdu\\templates']
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ByNotifyMessage(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True,null=True)  # Field name made lowercase.
    terminalcode = models.CharField(db_column='TerminalCode', max_length=8, blank=True,null=True)  # Field name made lowercase.
    releasetime = models.CharField(db_column='ReleaseTime', max_length=20, blank=True,null=True)  # Field name made lowercase.
    rescode = models.CharField(db_column='ResCode', max_length=10, blank=True,null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'by_notify_message'
class ByNotifyHistory(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True,null=True)  # Field name made lowercase.
    ncode = models.CharField(db_column='NCode', max_length=32, blank=True,null=True)  # Field name made lowercase.
    tcode = models.CharField(db_column='TCode', max_length=8, blank=True,null=True)  # Field name made lowercase.
    notifytime = models.CharField(db_column='NotifyTime', max_length=20, blank=True,null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'by_notify_history'

class ByVipTable(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True,null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True,null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=6 , blank=True,null=True) # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=16, blank=True,null=True)  # Field name made lowercase.
    score = models.IntegerField(db_column='Score', blank=True, null=True)   # Field name made lowercase.
    classify = models.CharField(db_column='Classify', max_length=20, blank=True,null=True)  # Field name made lowercase.
    wealth = models.FloatField(db_column='Wealth', blank=True, null=True)  # Field name made lowercase.
    notify = models.IntegerField(db_column='Notify', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'by_vip_table'

class ByVipFaceFeature(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True,null=True)  # Field name made lowercase.
    vipcode = models.CharField(db_column='VipCode', max_length=32, blank=True,null=True)  # Field name made lowercase.
    feature = models.BinaryField(db_column='Feature', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'by_vip_facefeature'

class ByProductConfig(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True,null=True)  # Field name made lowercase.
    rule = models.CharField(db_column='Rule', unique=True, max_length=32, blank=True,null=True)  # Field name made lowercase.
    rescode = models.CharField(db_column='ResCode', max_length=10, blank=True,null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'by_product_config'