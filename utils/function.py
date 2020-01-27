# -*- coding:utf-8 -*-
"""
公共函数库
"""
from flask import jsonify
import datetime
import decimal
import json as _json
import hashlib
import base64


class ClsEncoder(_json.JSONEncoder):
    """
    解决时间无法序列化问题
    """

    def default(self, obj):
        if isinstance(obj, datetime.date):
            return obj.__str__()
        if isinstance(obj, datetime.datetime):
            return obj.__str__()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, db.Model):
            obj_dict = obj.__dict__
            return dict((key, obj_dict[key]) for key in obj_dict if not key.startswith("_"))
        elif isinstance(obj, bytes):
            return obj.decode()
        return _json.JSONEncoder.default(self, obj)


def json_stringify(data):
    """
    将对象转换为字符串
    :param value: 字典，列表，元祖
    :return:
    """
    return _json.dumps(data, cls=ClsEncoder, ensure_ascii=False)


def json_parse(text):
    """
    解析json字符串
    :param text: JSON字符串
    :return:
    """
    return _json.loads(text)


def response_success(data):
    """
    输出json数据
    :param data:
    :return:
    """
    return_data = {"status": 1, "message": "success", "data": data}
    return jsonify(json_parse(json_stringify(return_data)))


def response_error(message, data=None):
    """
    错误输出 json
    :param message:
    :param data:
    :return:
    """
    return_data = {"status": -1, "message": message, "data": data}
    return jsonify(return_data)


def response_token_error():
    """
    token 错误
    :return:
    """
    return_data = {"status": -2, "message": "token fail", "data": None}
    return jsonify(return_data)


def md5(value):
    """
    字符串获得md5值
    :param value:
    :return:
    """
    return hashlib.md5(str(value).encode("utf-8")).hexdigest()


def sha1(value):
    return hashlib.sha1(str(value).encode("utf-8")).hexdigest()


def base64_encode(base_str):
    """
    将字符串编码为 base64字符串
    :param base_str:
    :return: base64 str
    """
    return base64.b64encode(base_str.encode()).decode()


def base64_decode(base64_str):
    """
    解码BASE64字符串
    :param base64_str:
    :return: str
    """
    return base64.b64decode(base64_str).decode()


def string_is_empty(text):
    """
    判断字符串是否为空
    :param str:
    :return:
    """
    if text is None:
        return True
    if text == "":
        return True
    return False


def ischildof(obj, cls):
    """
    判断类或者对象是否继承至某类 cls
    :param obj:
    :param cls:
    :return:
    """
    try:
        for i in obj.__bases__:
            if i is cls or isinstance(i, cls):
                return True
        for i in obj.__bases__:
            if ischildof(i, cls):
                return True
    except AttributeError:
        return ischildof(obj.__class__, cls)
    return False


isSubClassOf = ischildof
