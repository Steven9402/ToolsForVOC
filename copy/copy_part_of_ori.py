# -*- coding:UTF-8 -*-
import os
import os.path as osp
import shutil

src_dir='/home/cuizhou/Deeplearning/caffe/trainClassificationSqueezeNet/data_bkup/val'
dst_dir='/home/cuizhou/Deeplearning/caffe/trainClassificationSqueezeNet/data/val'

idx = 1
for root,folders,files in os.walk(src_dir):
    for folder in folders:
        print folder
        print '---'
        for filename in os.listdir(osp.join(root,folder)):
            print filename
            fullpath=osp.join(root,folder,filename)
            tarfullpath=osp.join(dst_dir,folder,filename)
            if idx%7==0:
                shutil.copy(fullpath,tarfullpath)
            idx+=1
