#!/usr/bin/env python
#coding=utf-8

import pymysql

db = pymysql.connect(host='localhost', user='yourself_user_name', password='yourself_password', port=3306, db='yourself_database')
cursor = db.cursor()



#创建一个名为face的数据表
sql = 'CREATE TABLE IF NOT EXISTS face_dataset ' \
      '(robj_name VARCHAR(255) NOT NULL, ' \
      'data_no VARCHAR(255) NOT NULL, ' \
      'data_yes VARCHAR(255) NOT NULL,' \
      'mark_time VARCHAR(255) NOT NULL,' \
      'PRIMARY KEY (robj_name))'

cursor.execute(sql)
db.close()