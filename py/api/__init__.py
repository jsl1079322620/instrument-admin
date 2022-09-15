# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: __init__.py
@create date: 2022/8/19 20:23
@description:
"""
import logging
import os
import random
from logging.handlers import RotatingFileHandler

from flask import Flask, request
from flask_cors import CORS

from api.resource import api
from comm.comm_time import get_system_time_str, get_system_date_str
# from utils.log_config import init_log

from config import config
from utils.log_config import logger, init_log


def create_app(config_name):
    app = Flask(__name__)
    # 验证
    CORS(app, supports_credentials=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # 初始化数据库
    # db.init_app(app)
    # 返回数据中response为中文
    app.config['JSON_AS_ASCII'] = False

    # 初始化日志###
    # init_log()

    # @app.before_request
    # def reset_log():
    #     url_rule = request.url_rule
    #     router = str(url_rule)[1:] if len(str(url_rule)) else ''
    #     init_log(router)
    @app.before_request
    def reset_log():
        import logging
        # logging.basicConfig(filename = os.path.join(os.getcwd(),'log.txt'), level = logging.DEBUG)
        url_rule = request.url_rule
        router = str(url_rule)[1:] if len(str(url_rule)) else ''
        log_path = os.path.join(os.getcwd(), '../../log', router, get_system_date_str())
        log_name = os.path.join(log_path, get_system_time_str() + '.log')
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        logging.basicConfig(filename=log_name)
        print('log_name====='+log_name)
    init_log()

    api.init_app(app)
    return app
