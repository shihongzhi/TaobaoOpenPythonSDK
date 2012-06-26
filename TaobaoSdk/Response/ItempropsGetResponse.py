#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief Q：能否通过图形化界面获取特定类目下面的属性及属性值? A：请点击属性工具，通过图形化界面直接获取上述数据 Q：关键属性，非关键属性，销售属性有什么区别？ A：产品的关键属性是必填的，关键属性＋类目id确定一个产品，非关键属性，是分类上除了关键属性和销售属性以外的属性。销售属性是只有一件实物的商品才能确定的一个属性，如：N73　红色，黑色。没有实物不能确定。 Q：销售属性与SKU之间有何关联？ A：销售属性是组成SKU的特殊属性，它会影响买家的购买和卖家的库存管理，如服装的"颜色"、"套餐"和"尺码"。  SKU 即我们常说的销售属性，最小购买单位或最小库存单位。它是销售属性的一个组合。比如"红色的诺基亚N95"就是一个SKU。
# @author wuliang@maimiaotech.com
# @date 2012-06-26 21:24:20
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


        
from Domain.ItemProp import ItemProp



## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">Response: Q：能否通过图形化界面获取特定类目下面的属性及属性值? A：请点击属性工具，通过图形化界面直接获取上述数据 Q：关键属性，非关键属性，销售属性有什么区别？ A：产品的关键属性是必填的，关键属性＋类目id确定一个产品，非关键属性，是分类上除了关键属性和销售属性以外的属性。销售属性是只有一件实物的商品才能确定的一个属性，如：N73　红色，黑色。没有实物不能确定。 Q：销售属性与SKU之间有何关联？ A：销售属性是组成SKU的特殊属性，它会影响买家的购买和卖家的库存管理，如服装的"颜色"、"套餐"和"尺码"。  SKU 即我们常说的销售属性，最小购买单位或最小库存单位。它是销售属性的一个组合。比如"红色的诺基亚N95"就是一个SKU。</SPAN>
# <UL>
# <LI>
# <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Authorize</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;"><DOM Text node "不需用户授权"></SPAN>
# </LI>
# </UL>
class ItempropsGetResponse(object):
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

        
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">最近修改时间(只有取全量或增量的时候会返回该字段)。格式:yyyy-MM-dd HH:mm:ss</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Date</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">true</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Sample</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">2010-01-01 00:00:00</SPAN>
        # </LI>
        # </UL>
        self.last_modified = None
        
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">类目属性信息(如果是取全量或者增量，不包括属性值),根据fields传入的参数返回相应的结果</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">ItemProp</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object Array</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">true</SPAN>
        # </LI>
        # </UL>
        self.item_props = None
    
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
            
            "last_modified": "Date",
            
            "item_props": "ItemProp",
        }
        levels = {
            
            "last_modified": "Basic",
            
            "item_props": "Object Array",
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
        
        if "last_modified" in kargs:
            self.last_modified = self._newInstance("last_modified", kargs["last_modified"])
        
        if "item_props" in kargs:
            self.item_props = self._newInstance("item_props", kargs["item_props"])
        if "code" in kargs:
            self.code = kargs["code"]
        if "msg" in kargs:
            self.msg = kargs["msg"]
        if "sub_code" in kargs:
            self.sub_code = kargs["sub_code"]
        if "sub_msg" in kargs:
            self.sub_msg = kargs["sub_msg"]
