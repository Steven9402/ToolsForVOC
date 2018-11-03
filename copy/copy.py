# -*- coding:UTF-8 -*-
import os
import os.path as osp
import shutil

src_dir='/media/NEWDATA/data/sfz-org/库-身份证'
dst_dir='/media/NEWDATA/data/sfz-org/tmp'

for root,folders,files in os.walk(src_dir):
    for folder in folders:
        for filename in os.listdir(osp.join(root,folder)):
            print filename
            fullpath=osp.join(root,folder,filename)
            siz=osp.getsize(fullpath)
            if siz/1024>100:
                tarfullpath=osp.join(dst_dir,folder,filename)
                shutil.move(fullpath,tarfullpath)
                print siz/1024,'kb'