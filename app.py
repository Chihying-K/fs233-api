import os

from File import file
from flask import Flask, jsonify, request

from data.service import getParameterHandling

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
pq =  1（原图）2（中等图） (picture quality图片质量)
'''


@app.route('/setu', methods=['GET'])
def setu():
    # 获取Get请求参数
    p = request.args

    # 首先判断是否需要返回原图
    if p.get('pq') == '2':
        return getParameterHandling(p.get('type'), p.get('num'), 'data/img-min.txt')
    else:
        return getParameterHandling(p.get('type'), p.get('num'), 'data/img.txt')


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
