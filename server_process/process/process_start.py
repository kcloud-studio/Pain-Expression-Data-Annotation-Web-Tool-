# coding:utf-8
from datetime import datetime
import os



#执行处理操作函数
def process():
    os.system("python ./video_frema.py")
    os.system("python ./video_del.py")
    os.system("python ./face_alignment.py")
    os.system("python ../oss_work/upload_photo_to_oss.py")            #工作调用目录
    os.system("python ../oss_work/upload_photo_to_oss_back.py")       #数据调用目录
    os.system("python ./photo_del.py")
    os.system("python ./ali_photo_del.py")





# 定时执行函数
from apscheduler.schedulers.blocking import BlockingScheduler

def tick():
    process()

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds=90)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
