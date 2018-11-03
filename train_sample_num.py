# -*- coding: utf-8 -*-
import os
from xml.dom.minidom import parse
import xml.dom.minidom

#path to difine
current = os.getcwd()
cls_path = 'name.txt'
xml_path = os.path.join(current,'Annotations')

# read class name
f = open(cls_path)
class_name = []
while 1:
    name = f.readline()
    name = name.strip()
    class_name.append(name)
    if not name:
        break

class_name.pop()
print 'clases =================',class_name

# dict to calculate
keys = class_name 
values = []
for i in range(94):
    values.append(0)

dic = dict(zip(keys, values))

# read xmls 
xmls = os.listdir(xml_path)
for xml_file in xmls:
    print xml_file
    DOMTree = xml.dom.minidom.parse(xml_path+'/'+xml_file)
    collection = DOMTree.documentElement
    # objects
    objs = collection.getElementsByTagName("object")
    for obj in objs:
        lab = obj.getElementsByTagName("name")[0]
        cls = lab.childNodes[0].data  # label class name
        print cls,','
        dic[cls]+=1

print dic

# write the result
f=open('sample_num.txt','w')
for k in keys:
    f.write(k+' = '+str(dic[k])+'\n')
    
    
