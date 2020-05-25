# coding = utf-8

from flask import Flask, render_template, Response, request
import importlib
import json
from flask import jsonify
import time
from database import dataset as base_data
from oss_work import del_object_from_oss as del_oss


# 引入必要的模块


app = Flask(__name__)  # 初始化一个Flask对象作为服务器


# 定义“路由”
@app.route('/')
# 定义一个函数，它将响应并返回一个html描述的页面：index.html
def gotoindex():
    return render_template('index.html')


# 定义“路由”
@app.route('/tagging/')
# 定义一个函数，它将响应并返回一个html描述的页面：tagging.html
def tagging():
    return render_template('tagging.html')


@app.route('/tag_end/')
def gototagend():
    return render_template('tag_end.html')


# 定义“路由”
@app.route('/change_photo/', methods=['POST', 'GET'])
def change_photo():
    from oss_work import get_url_from_oss as oss_url
    importlib.reload(oss_url)
    url = oss_url.face_url
    return Response(url)



@app.route('/time/', methods=['POST', 'GET'])
def get_time():
    t = time.time()
    t = int(t)
    t = str(t)
    return Response(t)



@app.route('/object_name/', methods=['POST', 'GET'])
def object_name():
    from oss_work import get_object_from_oss as name
    importlib.reload(name)
    obj_name = name.name_obj
    return Response(obj_name)



@app.route('/dataset/', methods=['POST','GET'])
def data_input():
    data = request.get_data()     # 获取回传的json数据
    data = str(data, encoding='utf-8')        # 转化为字符串
    data_dict = json.loads(data)
    # 定义数据
    get_obj_name = str(data_dict['obj_name'])
    data_yes = str(data_dict['data_yes'] - 2)
    data_no = str(data_dict['data_no'])
    mark_time = str(data_dict['time'])
    print(data_no, data_yes, get_obj_name, mark_time)
    base_data.push_database(get_obj_name, data_yes, data_no, mark_time)
    del_oss.del_oss_object(get_obj_name)
    return jsonify('OK')




if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)  # 运行！
