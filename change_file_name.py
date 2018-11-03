#!/usr/bin/env python
# -*- coding:utf-8 -*-

import shutil
import os
import os.path as osp

srcdir='/media/NEWDATA/newdata/Lishui/dj/lishui_lukou_det_xmls/33.241.138.58'
dstdir='/media/NEWDATA/newdata/Lishui/dj/lishui_lukou_det_xmls/xmls'
#批量更改文件名，适用于拷贝普通文件，对xml没有意义。
for filenm in os.listdir(srcdir):
    shutil.copyfile(osp.join(srcdir,filenm),osp.join(dstdir,'a'+filenm))
    print filenm
