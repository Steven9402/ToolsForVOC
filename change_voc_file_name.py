#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import os.path as osp

from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement
from lxml import etree
import codecs

import sys

import shutil


# Step1: input xml path
old_xmls_dir='/media/NEWDATA/newdata/Lishui/dj/lishui_lukou_det_xmls/33.241.138.100'
# Step2: output xml path
new_xmls_dir='/media/NEWDATA/newdata/Lishui/dj/lishui_lukou_det_xmls/xmls'
# Step3: input img path
old_img_path='/media/NEWDATA/newdata/Lishui/dj/lishui_lukou_pics/33.241.138.100'
# Step4: output img path
new_img_path='/media/NEWDATA/newdata/Lishui/dj/lishui_lukou_pics/imgs'
# Step5: set prefix
prefix='d'

def prettify(elem):
    """
        Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf8')
    root = etree.fromstring(rough_string)
    return etree.tostring(root, pretty_print=True)


for xml_file in os.listdir(old_xmls_dir):
    print '----------------'

    parser = etree.XMLParser(encoding='utf-8')
    xmltree = ElementTree.parse(osp.join(old_xmls_dir,xml_file), parser=parser).getroot()
    filename = xmltree.find('filename').text

    newfilename=prefix+filename # 修改xml内容
    xmltree.find('filename').text = newfilename

    out_file = codecs.open(osp.join(new_xmls_dir,prefix+xml_file), 'w', encoding='utf-8') # 修改xml文件名
    prettifyResult = prettify(xmltree)
    out_file.write(prettifyResult.decode('utf8'))
    out_file.close()

    print xml_file


for imgnm in os.listdir(old_img_path):
    print '--------------'
    shutil.copyfile(osp.join(old_img_path,imgnm),osp.join(new_img_path,prefix+imgnm))
    print imgnm
