#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 描述：根据客服ID和日期，获取该客服"当日在线时长"。  备注：1、如果是操作者ID=被查者ID，返回被查者ID的"当日在线时长"。      2、如果操作者是组管理员，他可以查询他的组中的所有子帐号的"当日在线时长"。      3、如果操作者是主账户，他可以查询所有子帐号的"当日在线时长"。     4、被查者ID可以是多个，用 "," 隔开，id数不能超过30。     5、日累计在线时长定义：当日该用户累计的旺旺在线时长      6、开始时间与结束时间之间的间隔不能超过7天     7、不能查询90天以前的数据     8、不能查询当天的记录
# @author wuliang@maimiaotech.com
# @date 2012-06-26 21:24:21
# @version: 0.0.0

from datetime import datetime
import os
import sys
import time

def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))
    
__parentPath = os.path.normpath(os.path.join(__getCurrentPath(), os.path.pardir))
if __parentPath not in sys.path:
    sys.path.insert(0, __parentPath)


    
from Domain.OnlineTimesOnDay import OnlineTimesOnDay



## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">Response: 描述：根据客服ID和日期，获取该客服"当日在线时长"。  备注：1、如果是操作者ID=被查者ID，返回被查者ID的"当日在线时长"。      2、如果操作者是组管理员，他可以查询他的组中的所有子帐号的"当日在线时长"。      3、如果操作者是主账户，他可以查询所有子帐号的"当日在线时长"。     4、被查者ID可以是多个，用 "," 隔开，id数不能超过30。     5、日累计在线时长定义：当日该用户累计的旺旺在线时长      6、开始时间与结束时间之间的间隔不能超过7天     7、不能查询90天以前的数据     8、不能查询当天的记录</SPAN>
# <UL>
# <LI>
# <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Authorize</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;"><DOM Text node "必须用户授权"></SPAN>
# </LI>
# </UL>
class WangwangEserviceOnlinetimeGetResponse(object):
    def __init__(self, kargs=dict()):
        super(self.__class__, self).__init__()

        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">请求的返回信息,包含状态等</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">dict</SPAN>
        # </LI>
        # </UL>
        self.responseStatus = None

        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">请求的响应内容</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">str</SPAN>
        # </LI>
        # </UL>        
        self.responseBody = None

        self.code = None

        self.msg = None

        self.sub_code = None

        self.sub_msg = None

        
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">客服在线时长（按天统计，排列）</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">OnlineTimesOnDay</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object Array</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">true</SPAN>
        # </LI>
        # </UL>
        self.online_times_list_on_days = None
    
        self.__init(kargs)

    def isSuccess(self):
        return self.code == None and self.sub_code == None
    
    def _newInstance(self, name, value):
        types = self._getPropertyType(name)
        propertyType = types[0]
        isArray = types[1]
        if propertyType == bool:
            if isArray:
                return [x for x in value[value.keys()[0]]]
            else:
                return value
        elif propertyType == datetime:
            format = "%Y-%m-%d %H:%M:%S"
            if isArray:
                return [datetime.strptime(x, format) for x in value[value.keys()[0]]]
            else:
                return datetime.strptime(value, format)
        elif propertyType == str:
            if isArray:
                return [x.encode("utf-8") for x in value[value.keys()[0]]]
            else:
                #like taobao.simba.rpt.adgroupbase.get, response.rpt_adgroup_base_list is a json string,but will be decode into a list via python json lib 
                if not isinstance(value,str):
                    #the value should be a json string 
                    return value
                return value.encode("utf-8")
        else:
            if isArray:
                return [propertyType(x) for x in value[value.keys()[0]]]
            else:
                return propertyType(value)
        
    def _getPropertyType(self, name):
        properties = {
            
            "online_times_list_on_days": "OnlineTimesOnDay",
        }
        levels = {
            
            "online_times_list_on_days": "Object Array",
        }
        
        nameType = properties[name]
        nameTypeToPythonType = {"Number":int, "String":str, "Boolean":bool, "Date":datetime, "Price":float, "byte[]":str}
        pythonType = nameTypeToPythonType.get(nameType, getattr(sys.modules["Domain.%s" % nameType], nameType))
        
        # 是单个元素还是一个对象
        level = levels[name]
        if "Array" in level:
            return (pythonType, True)
        else:
            return (pythonType, False)

    def __init(self, kargs):
        
        if "online_times_list_on_days" in kargs:
            self.online_times_list_on_days = self._newInstance("online_times_list_on_days", kargs["online_times_list_on_days"])
        if "code" in kargs:
            self.code = kargs["code"]
        if "msg" in kargs:
            self.msg = kargs["msg"]
        if "sub_code" in kargs:
            self.sub_code = kargs["sub_code"]
        if "sub_msg" in kargs:
            self.sub_msg = kargs["sub_msg"]
