# -*- coding:utf-8 -*-

import xml.etree.ElementTree
from xml.etree.ElementTree import ElementTree

'''改变图片名字'''
def changeName(root_parent,img_name_new):
    root_parent.find('filename').text = img_name_new

'''
只保留特定类别的节点"object"，保留类型在node_type_list中定义
'''
def keepNode(root_parent,node_name,node_type_list):
    for node_temp in root_parent.findall(node_name):
        type=node_temp.find("name").text
        delete=True
        for elem in node_type_list:
            if type==elem:
                delete=False

        if delete:
            root_parent.remove(node_temp)

'''
删除box满足一定条件的节点"object"
'''
def deleteNode(root_parent):
    for obj in root_parent.findall('object'):
        bndboxXml = obj.find('bndbox')
        xmin = int(bndboxXml.find('xmin').text)
        ymin = int(bndboxXml.find('ymin').text)
        xmax = int(bndboxXml.find('xmax').text)
        ymax = int(bndboxXml.find('ymax').text)

        width = xmax-xmin
        height = ymax-ymin
        if width<50 or height<50:
            root_parent.remove(obj)