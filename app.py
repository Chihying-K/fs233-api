import os

from File import file
from flask import Flask, jsonify, request

IS_SERVERLESS = bool(os.environ.get('SERVERLESS'))

app = Flask(__name__)


@app.route("/")
def index():
    return '<script>window.location="https://fs233.cc/#/"</script>'


'''
涩图请求接口

可传参数：
type = json
num = {返回的图片张数}
'''


@app.route('/setu', methods=['GET'])
def setu():
    # 获取Get请求参数
    p = request.args

    # 如果参数type为json 则返回json格式
    if p.get('type') == 'json':
        num = p.get('num')
        list = file("data/img.txt")

        # 判断num是否为空
        if num == None:
            a = list[0]
        else:
            a = list[0:int(num)]

        return jsonify({'msg': a})
    # 如果不是json则直接跳转图片
    else:
        list = file("data/img.txt")
        a = '<script>window.location="' + list[0] + '"</script>'
        return a


# 涩图张数（非R18）
@app.route('/num', methods=['GET'])
def num():
    list = file("data/img.txt")
    return jsonify({'num': len(list)})


# 涩图张数（R18）
@app.route('/numr18', methods=['GET'])
def numr18():
    list = file("data/img-r18.txt")
    return jsonify({'num': len(list)})


if IS_SERVERLESS != True:
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
