import os
from xml.dom.minidom import parse
import xml.dom.minidom
import sys
import xml.etree.ElementTree
from xml.etree.ElementTree import ElementTree
import shutil

def copyTargetedObjPictoFolder(type,dir,root):
    hastargetcircle = False
    objs = root.findall("object")
    for obj in objs:
        name = obj.find("name")
        if name.text == type:
            hastargetcircle = True

    if hastargetcircle == True:
        filenameobjs = root.findall("filename")
        imgname = ''
        for filenameobj in filenameobjs:
            imgname = filenameobj.text

        oldname = img_dir + "/" + imgname
        newname = dir + "/" +imgname
        shutil.copyfile(oldname, newname)



# set xml path, img path
xmls_dir = "/home/cuizhou/data/AdasData/yirenTraficData/Annotations_first_preaug"
img_dir = "/home/cuizhou/data/AdasData/yirenTraficData/JPEGImages"

# set output_path
circle_output_dir = "/home/cuizhou/codes/AdasProject/adas-color-region-proposal/images/shanghaicircle"
triangle_output_dir ="/home/cuizhou/codes/AdasProject/adas-color-region-proposal/images/shanghaitriangle"
rectangle_output_dir ="/home/cuizhou/codes/AdasProject/adas-color-region-proposal/images/shanghairectangle"
trafficlight_output_dir = "/home/cuizhou/codes/AdasProject/adas-color-region-proposal/images/shanghaitrafficlight"

xmls = os.listdir(xmls_dir)
for xml_file in xmls:

    print '----------------'
    print 'Parsing:',xml_file

    tree = ElementTree()
    tree.parse(xmls_dir+'/'+xml_file)
    root = tree.getroot()

    copyTargetedObjPictoFolder("trafficsigncircle",circle_output_dir,root)
    copyTargetedObjPictoFolder("trafficsigntriangle", triangle_output_dir,root)
    copyTargetedObjPictoFolder("trafficsignrectangle", rectangle_output_dir,root)
    copyTargetedObjPictoFolder("trafficlight", trafficlight_output_dir,root)






