# -*- coding:utf-8 -*-
"""
web 端配置文件，禁止 worker 端调用
"""
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_session import Session
# from sqlalchemy.ext.declarative import declarative_base
# from flask_jsontools import JsonSerializableBase
import logging
# import redis
# import os
# from datetime import timedelta
# from influxdb import InfluxDBClient

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s[%(lineno)d] - %(levelname)s - %(message)s')

# 配置 flask
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
# 配置 flask end