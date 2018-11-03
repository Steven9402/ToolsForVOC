#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import cv2

#intputdir = '/home/cuizhou/projects/KaiKouXiao/1stVOCdevkit2007/negtive_additional_data/myf'
#outputdir = '/home/cuizhou/projects/KaiKouXiao/1stVOCdevkit2007/negtive_additional_data/myf1'


intputdir = '/media/cuizhou/KINGSTON/tempfiles/zzd'
outputdir = '/media/cuizhou/KINGSTON/tempfiles/zzd2'

for imagename in os.listdir(intputdir):
    #length1 = len(imagen1)
    #imagen1 = imagename[0:length1-4]
    print imagename

    srcimage = cv2.imread(intputdir+"/"+imagename)

    cv2.imwrite(intputdir+"/"+"neg_"+imagename,srcimage);
    print '.'
