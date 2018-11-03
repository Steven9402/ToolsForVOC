##说明
txt
>name_find_img.py 将test.txt中列举的图片拷贝到制定文件夹下面

read xml
>parsexml_draw.py 将Annotation中的xml的标注画出来
>parsexml_cut_image_roi.py 将xml中的标注框裁剪出来
>train_sample_num.py 根据Annotation统计样本数量
>find_images_which_has_specific_target.py 寻找有特定类别的图片

make xml
>make_label_with_groundtruth.py 根据车牌截取的图片，大致计算字符位置，生成xml

change xml
>filterXmlFile.py 删除xml中的特定的类别

文件操作
>change_image_name.py 更改图片名字
>change_file_name.py 更改文件名字
>change_voc_file_name.py 更改xml名，内容名和图片名