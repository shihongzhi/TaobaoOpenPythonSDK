#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:
"""
@author: Wu Liang
@authors: 
@date: 12:05:40 AM Jun 5, 2012
@contact: wuliang@maimiaotech.com 
@version: 0.0.0
@deprecated:
@license:
@copyright:
"""

from Common import *
from Settings import *

class DomainParser(object):
    def __init__(self, root, output):
        self.root = root
        self.output = output
        
    def generateFiles(self):
        rootOutput = os.path.join(self.output, OUTPUT['domain'])
        if not os.path.exists(rootOutput):
            os.makedirs(rootOutput)
        imported = set()
        templateFile = Template(file(TEMPLATE['domain']).read().decode("utf-8"))
        for struct in self.root.getElementsByTagName("struct"):
            rendered = templateFile.render_unicode(struct=struct).encode("utf-8")
            rendered = rendered.replace("\\#\\#", "##")
            filename = struct.getElementsByTagName("name")[0].firstChild.data.encode("utf-8")
            imported.add(filename)
            filename += ".py"
            filename = os.path.join(rootOutput, filename)
            print "Generating %s" % (filename)
            with open(filename, 'w') as fout:
                fout.write(rendered)
        templateFile = Template(file(TEMPLATE['init']).read().decode("utf-8"))
        rendered = templateFile.render_unicode(imports=imported).encode("utf-8")
        with open(os.path.join(rootOutput, "__init__.py"), 'w') as fout:
            fout.write(rendered)
