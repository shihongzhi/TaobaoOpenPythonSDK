#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 使用指南：http://open.taobao.com/dev/index.php/ATS%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97 1.此接口用于获取异步任务处理的结果，传入的task_id必需属于当前的appKey才可以 2.此接口只返回执行完成的任务结果，未执行完的返回结果里面不包含任务结果，只有任务id，执行状态 3.执行完成的每个task的子任务结果内容与单个任务的结果结构一致。如：taobao.topats.trades.fullinfo.get返回的子任务结果就会是Trade的结构体。
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


    
from Domain.Task import Task



## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">Response: 使用指南：http://open.taobao.com/dev/index.php/ATS%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97 1.此接口用于获取异步任务处理的结果，传入的task_id必需属于当前的appKey才可以 2.此接口只返回执行完成的任务结果，未执行完的返回结果里面不包含任务结果，只有任务id，执行状态 3.执行完成的每个task的子任务结果内容与单个任务的结果结构一致。如：taobao.topats.trades.fullinfo.get返回的子任务结果就会是Trade的结构体。</SPAN>
# <UL>
# <LI>
# <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Authorize</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;"><DOM Text node "不需用户授权"></SPAN>
# </LI>
# </UL>
class TopatsResultGetResponse(object):
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

        
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">返回任务处理信息</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Task</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">true</SPAN>
        # </LI>
        # </UL>
        self.task = None
    
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
            
            "task": "Task",
        }
        levels = {
            
            "task": "Object",
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
        
        if "task" in kargs:
            self.task = self._newInstance("task", kargs["task"])
        if "code" in kargs:
            self.code = kargs["code"]
        if "msg" in kargs:
            self.msg = kargs["msg"]
        if "sub_code" in kargs:
            self.sub_code = kargs["sub_code"]
        if "sub_msg" in kargs:
            self.sub_msg = kargs["sub_msg"]
