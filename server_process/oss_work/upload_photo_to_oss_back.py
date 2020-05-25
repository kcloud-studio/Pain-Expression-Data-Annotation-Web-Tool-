# -*- coding: utf-8 -*-
import oss2
import os

#查询文件夹下图片文件
photo_name = []
photo_name_objn = []
FileNumber = 0
dir = '../process/alignment' #指定文件夹的路径
for root, dirs, files in os.walk(dir):                      #遍历该文件夹
    for file in files:                                      #遍历刚获得的文件名files
        (filename, extension) = os.path.splitext(file)      #将文件名拆分为文件名与后缀
        if (extension == '.jpg'):                             #判断该后缀是否为.jpg文件
            FileNumber= FileNumber+1                      #记录.jpg文件的个数为对应文件号
            photo_name.append(os.path.join(root, filename) + ".jpg")
            photo_name_objn.append(filename + ".jpg")


# 循环请求上传
while photo_name != []:


    # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
    auth = oss2.Auth('<yourAccessKeyId>', '<yourAccessKeySecret>')
    # Endpoint以杭州为例，其它Region请按实际情况填写。
    bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', '<yourBucketName>')

    # 必须以二进制的方式打开文件，因为需要知道文件包含的字节数。
    with open(photo_name[0], 'rb') as fileobj:
    #文件上传。
        bucket.put_object_from_file(photo_name_objn[0], photo_name[0])
    # Tell方法用于返回当前位置。
        current = fileobj.tell()
        bucket.put_object(photo_name_objn[0], fileobj)

    #删除已上传的对象路径、对象名
    del photo_name[0]
    del photo_name_objn[0]

