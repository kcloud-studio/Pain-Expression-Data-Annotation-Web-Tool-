#!/usr/bin/env python
#coding=utf-8

import os

# 查询文件夹下的视频文件名,这里这样写是因为只有一个视频文件，不必列出多个
f_list = os.listdir("./")
for video in f_list:
	if os.path.splitext(video)[1] == '.mp4':     # os.path.splitext():分离文件名与扩展名
            video_name = video


path = "./" + video_name   # 文件路径
os.remove(path)