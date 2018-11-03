#! /bin/python
# -*- coding:utf-8 -*-

import os
import os.path as osp
from xml.etree.ElementTree import ElementTree

import xmlHandler as xh

import shutil
import cv2
'''
1. 从xml拷贝图片
2. 修改xml名
3. 删除特定类型的节点
4. 删除bbox太小的节点
5. 将png改成jpg
'''
def mode1():

    xmlpathTop='/media/NEWDATA/newdata/TrafficBigData/trainingdata/labeled_images_by_yiren_04-01/20180320'
    xmlrootpath_new="/media/NEWDATA/newdata/TrafficBigData/trainingdata/TrafficBigData-CarBusTruck-new/Annotations"
    img_root_path_new="/media/NEWDATA/newdata/TrafficBigData/trainingdata/TrafficBigData-CarBusTruck-new/JPEGImages"
    for parent,folders,files in os.walk(xmlpathTop):
        for folder in folders:
            folderpath=xmlpathTop+"/"+folder
            for filenm in os.listdir(folderpath):
                houzhui=filenm[-4:]
                if houzhui=='.xml':
                    xmlpath_old=folderpath+'/'+filenm

                    print filenm

                    tree = ElementTree(xmlpath_old)
                    tree.parse(xmlpath_old)
                    root = tree.getroot()

                    #copy image
                    filenameobjs = root.findall("filename")
                    imgname = ''
                    for filenameobj in filenameobjs:
                        imgname = filenameobj.text

                    img_name_new=""
                    if imgname[-4:]==".png":
                        img_name_new=folder+"_"+imgname[:-4]+".jpg"
                        old_path=folderpath+"/"+imgname
                        srcImage = cv2.imread(old_path)
                        new_img_path=osp.join(img_root_path_new,img_name_new)
                        cv2.imwrite(new_img_path,srcImage)

                    else:

                        img_name_new=folder+"_"+imgname
                        print img_name_new
                        old_path=folderpath+"/"+imgname
                        new_img_path=osp.join(img_root_path_new,img_name_new)
                        shutil.copyfile(old_path,new_img_path)

                    #change xml and save
                    xml_path_new=xmlrootpath_new+"/"+img_name_new[:-4]+".xml"

                    xh.changeName(root,img_name_new)
                    xh.keepNode(root,"object",["bus","car","truck"])
                    xh.deleteNode(root)

                    tree = ElementTree(root)
                    tree.write(xml_path_new, encoding='utf-8')

def mode2():
    xml_path_top='/media/NEWDATA/newdata/TrafficBigData/trainingdata/labeled_images_by_yiren_04-01/20180319xml'
    img_path_top='/media/NEWDATA/newdata/TrafficBigData/trainingdata/labeled_images_by_yiren_04-01/20180319'

    target_img_path='/media/NEWDATA/newdata/TrafficBigData/trainingdata/TrafficBigData-CarBusTruck-new/JPEGImages (copy)'
    target_xml_path='/media/NEWDATA/newdata/TrafficBigData/trainingdata/TrafficBigData-CarBusTruck-new/Annotations (copy)'
    for xmlnm in os.listdir(xml_path_top):
        houzhui = xmlnm[-4:]
        if houzhui=='.xml':
            xmlpath_old = xml_path_top + '/' + xmlnm

            print xmlnm

            tree = ElementTree(xmlpath_old)
            tree.parse(xmlpath_old)
            root = tree.getroot()

            # copy image
            filenameobjs = root.findall("filename")
            imgname = ''
            for filenameobj in filenameobjs:
                imgname = filenameobj.text

            old_path = img_path_top + "/" + imgname
            new_img_path = osp.join(target_img_path, imgname)
            shutil.copyfile(old_path, new_img_path)


            # change xml and save
            xml_path_new = target_xml_path + "/" + xmlnm

            xh.keepNode(root, "object", ["bus", "car", "truck"])
            xh.deleteNode(root)

            tree = ElementTree(root)
            tree.write(xml_path_new, encoding='utf-8')

if __name__ == '__main__':
    mode2()
