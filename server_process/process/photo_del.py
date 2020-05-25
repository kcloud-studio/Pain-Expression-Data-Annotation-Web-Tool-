#!/usr/bin/env python
#coding=utf-8
import os

photo_name = []
photo_name_objn = []
FileNumber = 0
dir = './photo'  #指定文件夹的路径
for root, dirs, files in os.walk(dir):                      #遍历该文件夹
    for file in files:                                      #遍历刚获得的文件名files
        (filename, extension) = os.path.splitext(file)      #将文件名拆分为文件名与后缀
        if (extension == '.jpg'):                             #判断该后缀是否为.jpg文件
            FileNumber= FileNumber+1                      #记录.jpg文件的个数为对应文件号
            photo_name.append(os.path.join(root, filename) + ".jpg")


#循环删除图片
while photo_name != [] :
    os.remove(photo_name[0])
    del  photo_name[0]