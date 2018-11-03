import os
from xml.dom.minidom import parse
import xml.dom.minidom
import sys
import xml.etree.ElementTree
from xml.etree.ElementTree import ElementTree

xmls_dir = "/home/zhida/data/ADAS-dfsfag/VOCdevkit/VOC2007/Annotations"
output_dir = "/home/zhida/data/ADAS-dfsfag/VOCdevkit/VOC2007/result"

# input dir
xmls = os.listdir(xmls_dir)

# objects to be deleted
delete_list = ["trafficlight", "trafficsignrectangle", "trafficsigncircle", "trafficsigntriangle"]

for xml_file in xmls:

    print '----------------'
    print 'Parsing:',xml_file

    tree = ElementTree()
    tree.parse(xmls_dir+'/'+xml_file)
    root = tree.getroot()

    objs = root.findall("object")
    for obj in objs:
        name = obj.find("name")
        if name.text in delete_list:
            root.remove(obj)


    if len(root.findall("object")) == 0:
        # delete empty xmls
        print xmls_dir + "/" + xml_file +" deleted"
        os.remove(xmls_dir + "/" + xml_file)
    else:
        tree.write(output_dir + "/" + xml_file)
    #tree.write(output_dir + "car.xml")







