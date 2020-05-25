#!/usr/bin/env python
#coding=utf-8
import pymysql
import os




# 链接数据库
def push_database(get_obj_name, data_yes, data_no, mark_time):
    db = pymysql.connect(host='localhost', user='yourself_user_name', password='yourself_password', port=3306, db='yourself_database')
    cursor = db.cursor()

    # 使用格式化符%s来插入数据
    sql = 'INSERT INTO face_dataset (robj_name, data_no, data_yes, mark_time) values(%s, %s, %s, %s)'
    try:
        cursor.execute(sql, (get_obj_name, data_no, data_yes, mark_time))
        db.commit()
    except:
        db.rollback()
    db.close()