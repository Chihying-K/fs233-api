from flask import jsonify

from File import file


def getParameterHandling(type, num, path):
    # 如果参数type为json 则返回json格式
    if type == 'json':
        list = file(path)

        # 判断num是否为空
        if num == None:
            a = list[0]
        else:
            a = list[0:int(num)]

        return jsonify({'msg': a})
    # 如果不是json则直接跳转图片
    else:
        list = file(path)
        a = '<script>window.location="' + list[0] + '"</script>'
        return a
