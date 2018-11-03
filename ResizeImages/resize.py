# -*- coding:UTF-8 -*-
import os
import os.path as osp
import cv2

src_dir='/home/cuizhou/Deeplearning/caffe/trainClassificationSqueezeNet/data/val'

for root,folders,files in os.walk(src_dir):
    for folder in folders:
        for filename in os.listdir(osp.join(root,folder)):
            print filename
            fullpath=osp.join(root,folder,filename)
            img=cv2.imread(fullpath)
            img_res=cv2.resize(img,(227,227))
            print 'writing',fullpath
            cv2.imwrite(fullpath,img_res)
