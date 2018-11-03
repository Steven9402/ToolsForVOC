# -*- coding: utf-8 -*-
import os
from xml.dom.minidom import parse
import xml.dom.minidom

import cv2
import sys
reload(sys)
sys.setdefaultencoding('utf8')


'''
set output path
'''
outpth='/home/cuizhou/Desktop/VOC_workspace/diaoche/zzd/vis_result'

current = os.getcwd()
xml_dir = '/home/cuizhou/Desktop/VOC_workspace/diaoche/zzd/label-myf'
img_dir = '/home/cuizhou/Desktop/VOC_workspace/diaoche/zzd/400'

# read xmls
xmls = os.listdir(xml_dir)
for xml_file in xmls:
    print '----------------'
    print 'Parsing:',xml_file
    DOMTree = xml.dom.minidom.parse(xml_dir+'/'+xml_file)
    annotation = DOMTree.documentElement

    # read images
    imgfn = xml_file[0:len(xml_file) - 4] + '.jpg'
    imgpth = os.path.join(img_dir, imgfn)
    src = cv2.imread(imgpth)
    if src == NoneType:
        continue
    print 'Read :',imgpth

    # objects
    objs = annotation.getElementsByTagName("object")
    roi_idx = 0
    for obj in objs:
        # label class name
        name = obj.getElementsByTagName("name")[0]
        cls = name.childNodes[0].data

        # label
        bndbox = obj.getElementsByTagName("bndbox")[0]
        xmin_ = bndbox.childNodes[1]
        ymin_ = bndbox.childNodes[3]
        xmax_ = bndbox.childNodes[5]
        ymax_ = bndbox.childNodes[7]

        xmin = int(float(xmin_.firstChild.data))
        ymin = int(float(ymin_.firstChild.data))
        xmax = int(float(xmax_.childNodes[0].data))
        ymax = int(float(ymax_.childNodes[0].data))
        #
        print cls,xmin,ymin,xmax,ymax

        #cv2.rectangle(src, (xmin,ymin), (xmax,ymax), (255, 255, 0), 2)
        #cv2.putText(src,cls,(xmin,ymin),0,0.5,(0,0,255),2)
        roi_idx+=1
        roiname = outpth +'/'+imgfn[0:len(imgfn) - 4] + str(roi_idx)+'.jpg'
        roimat = src[ymin:ymax,xmin:xmax]
        cv2.imwrite(roiname, roimat)
