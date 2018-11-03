#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import cv2
from xml.etree.ElementTree import Element, SubElement, ElementTree

#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

def changetxt(s):
    if s == '粤':
        return 'GD_yue'
    elif s == '京':
        return 'BJ_jing'
    elif s == '津':
        return 'TJ_jin'
    elif s == '沪':
        return 'SH_hu'
    elif s == '渝':
        return 'CQ_yu'
    elif s == '冀':
        return 'HB_ji'
    elif s == '豫':
        return 'HN_yu'
    elif s == '云':
        return 'YN_yun'
    elif s == '辽':
        return 'LN_liao'
    elif s == '黑':
        return 'HLJ_hei'
    elif s == '湘':
        return 'HN_xiang'
    elif s == '皖':
        return 'Ah_wan'
    elif s == '鲁':
        return 'SD_lu'
    elif s == '新':
        return 'XJ_xin'
    elif s == '苏':
        return 'JS_su'
    elif s == '浙':
        return 'ZJ_zhe'
    elif s == '赣':
        return 'JX_gan'
    elif s == '鄂':
        return 'HB_e'
    elif s == '桂':
        return 'GX_gui'
    elif s == '甘':
        return 'GS_gan'
    elif s == '晋':
        return 'SX_jin'
    elif s == '蒙':
        return 'NMG_meng'
    elif s == '陕':
        return 'SX_shan'
    elif s == '吉':
        return 'JL_ji'
    elif s == '闽':
        return 'FJ_min'
    elif s == '贵':
        return 'GZ_gui'
    elif s == '青':
        return 'QH_qing'
    elif s == '藏':
        return 'XZ_zang'
    elif s == '川':
        return 'SC_chuan'
    elif s == '琼':
        return 'HN_qiong'
    elif s == '宁':
        return 'NX_ning'
    elif s == '警':
        return 'Jing'
    elif s == '领':
        return 'Ling'
    elif s == '使':
        return 'Shi'
    elif s == '港':
        return 'Gang'
    elif s == '澳':
        return 'Ao'
    elif s == '学':
        return 'XUE'
    else:
        #print('unchanged label:',s)
        return s

def genXml(imgpath, fn, img, label, rects):
    eroot = Element('annotation')
    folder = SubElement(eroot, 'folder')
    folder.text = 'Plate'
    filename = SubElement(eroot, 'filename')
    filename.text = fn
    path = SubElement(eroot, 'path')
    path.text = os.path.join(imgpath, fn)
    source = SubElement(eroot, 'source')
    database = SubElement(source, 'database')
    database.text = 'Unknown'
    size = SubElement(eroot, 'size')
    width_1 = SubElement(size, 'width')
    width_1.text = str(img.shape[1])
    height_1 = SubElement(size, 'height')
    height_1.text = str(img.shape[0])
    depth_1 = SubElement(size, 'depth')
    depth_1.text = str(img.shape[2])
    segmented = SubElement(eroot, 'segmented')
    segmented.text = '0'
    for i in range(len(label)):
        object = SubElement(eroot, 'object')
        name = SubElement(object, 'name')
        newlabel = changetxt(label[i])
        name.text = newlabel
        #print('name.text=',newlabel)
        pose = SubElement(object, 'pose')
        pose.text = 'Unspecified'
        truncated = SubElement(object, 'truncated')
        truncated.text = '0'
        difficult = SubElement(object, 'difficult')
        difficult.text = '0'
        bndbox = SubElement(object, 'bndbox')
        xmin = SubElement(bndbox, 'xmin')
        ymin = SubElement(bndbox, 'ymin')
        xmax = SubElement(bndbox, 'xmax')
        ymax = SubElement(bndbox, 'ymax')


        xmin.text = str(int(rects[i][0]))
        ymin.text = str(int(rects[i][1]))
        xmax.text = str(int(rects[i][2]))
        ymax.text = str(int(rects[i][3]))
        #print('ymax.text',ymax.text)

    tree = ElementTree(eroot)
    return tree




def generate_rects(row,col):
    rects = []
    updown_f = 10
    platewidth=226+8#247+10
    plateheight=70

    widthratio=float(col)/platewidth
    heightratio=float(row)/plateheight

    xmax=0
    for i in range(7):
        if i < 2:
            xmin_ = float(2. + 8 + (23 + 6) * i)*widthratio
            ymin_ = float(0. + updown_f)*heightratio
            xmax_ = float(2. + 8 + 23 + (23 + 6) * i)*widthratio
            ymax_ = float(70. - updown_f)*heightratio
            rect = [xmin_,ymin_,xmax_,ymax_]
            rects.append(rect)

        else:
            xmin_ = float(2. + 8 + 23 + 6 + 23 + 17 + (23 + 6) * (i - 2))*widthratio
            ymin_ = float(0. + updown_f)*heightratio
            xmax_ = float(2. + 8 + 23 + 6 + 23 + 17 + (23 + 6) * (i - 2) + 23)*widthratio
            ymax_ = float(70. - updown_f)*heightratio
            xmax=xmax_
            rect = [xmin_,ymin_,xmax_,ymax_]
            rects.append(rect)
    #print('examing rests:')
    #print('xmax:',xmax)
    #print('image width:',col)
    return rects


rootdir='/home/steven/Desktop/lishuidata/plateNumber20171015/VOCdevkit2007/VOC2007/JPEGImages'
xmlpath='/home/steven/Desktop/lishuidata/plateNumber20171015/VOCdevkit2007/VOC2007/Annotations'
for parent,folder,filenames in os.walk(rootdir):
    for filename in filenames:
        print(filename)

        src=cv2.imread(os.path.join(parent,filename))
        row=src.shape[0]
        col=src.shape[1]
        rects=generate_rects(row, col)

        l=len(filename)
        label=filename[l-17:l-10]

        etree=genXml(parent, filename, src, label, rects)
        targetFile=os.path.join(xmlpath,filename[0:l-4]+'.xml')
        etree.write(targetFile, encoding='utf-8')
