#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:
"""
@author: Wu Liang
@authors: 
@date: 11:49:01 PM Jun 4, 2012
@contact: wuliang@maimiaotech.com 
@version: 0.0.0
@deprecated:
@license:
@copyright:
"""

import os

def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))

# 模板文件夹目录
pyTemplatePath = os.path.join(__getCurrentPath(), "templates")

# 模板文件路径
TEMPLATE = {'domain':os.path.join(pyTemplatePath, "domain.template"), 
            'init':os.path.join(pyTemplatePath, "init.template"),
            'request':os.path.join(pyTemplatePath, 'request.template'),
            'response':os.path.join(pyTemplatePath, 'response.template'),
            'sdk_common':os.path.join(pyTemplatePath, "SdkCommon.template"),
            'error_response':os.path.join(pyTemplatePath, "ErrorResponse.py")}

# 输出文件路径
OUTPUT = {'domain':"Domain",
            'request':"Request",
            'response':"Response",
            'sdk_common':'SdkCommon.py',
            'error_response':'ErrorResponse.py'}
