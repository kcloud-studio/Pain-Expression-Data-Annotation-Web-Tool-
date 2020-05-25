#!/usr/bin/env python
#coding=utf-8

import cv2
import os

# 查询文件夹下的视频文件名,这里这样写是因为只有一个视频文件，不必列出多个
f_list = os.listdir("./")
for video in f_list:
	if os.path.splitext(video)[1] == '.mp4':     # os.path.splitext():分离文件名与扩展名
            video_name = video




# 读入视频文件
vc = cv2.VideoCapture(video_name)
c = 1

# 判断是否正常打开
if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

timeF = 150   # 视频帧计数间隔频率

# 提取视频文件名
video_name = video_name.replace(".mp4","")

# 循环读取视频帧
while rval:
    rval, frame = vc.read()
    if (c%timeF == 0):  # 每隔timeF帧进行存储操作
        cv2.imwrite('./photo/' + video_name + "_" +str(c) + '.jpg', frame)  # 存储为图像
    c = c + 1
    cv2.waitKey(1)
vc.release()


