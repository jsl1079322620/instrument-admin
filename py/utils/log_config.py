# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: log_config.py
@create date: 2022/8/19 20:27
@description:
"""
import datetime
import os
import logging
import logging.handlers

# from comm.comm_file import makeDirs as mkDirs, remove_dir as rmDirs
from comm.comm_time import get_system_date_str, get_system_time_str, string_to_date, get_system_datetime
from config import configuration


# logger = logging.getLogger("Info")
#
# log_path_root = os.path.join(os.getcwd(), '../../log')
#
#
# def init_log(router):
#     _logger = logging.getLogger()
#     configuration.set_option_value('LOG', 'log_path_root', log_path_root)
#     if not router:
#         router = 'index'
#     log_path = os.path.join(log_path_root, get_system_date_str(), router)
#     if not os.path.exists(log_path):
#         os.makedirs(log_path)
#     if len(_logger.handlers) == 0:  # 避免重复
#         # 2.创建handler(负责输出，输出到屏幕 StreamHandler,输出到文件filehandler)
#         # filename = os.path.join(log_path, 'user_api.log')
#         filename = os.path.join(log_path, get_system_time_str() + '.log')
#         fh = logging.FileHandler(filename)  # 默认mode 为a模式，默认编码方式为utf-8
#         sh = logging.StreamHandler()
#         # 3.创建formatter：
#         formatter = logging.Formatter('[%(asctime)s %(filename)s: %(lineno)d] %(message)s', '%H:%M:%S')
#         # 4.绑定关系：①logger绑定handler
#         _logger.addHandler(fh)
#         _logger.addHandler(sh)
#         # # ②为handler绑定formatter
#         fh.setFormatter(formatter)
#         sh.setFormatter(formatter)
#         # # 5.设置日志级别(日志级别两层关卡必须都通过，日志才能正常记录)
#         _logger.setLevel(logging.INFO)
#         fh.setLevel(logging.INFO)
#         sh.setLevel(logging.INFO)
#
#         _logger.info(f'初始化的日志路径：{filename}')


class Logger(object):
    def __init__(self, request_url):
        self._request_url = request_url
        self.logger = logging.getLogger()
        log_path_root = os.path.join(os.getcwd(), '../../log')
        log_path = os.path.join(log_path_root, get_system_date_str(), request_url)
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        filename = os.path.join(log_path, get_system_time_str() + '.log')
        fh = logging.FileHandler(filename)  # 默认mode 为a模式，默认编码方式为utf-8
        sh = logging.StreamHandler()
        formatter = logging.Formatter('[%(asctime)s %(filename)s: %(lineno)d] %(message)s', '%H:%M:%S')
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        self.logger.setLevel(logging.INFO)
        fh.setLevel(logging.INFO)
        sh.setLevel(logging.INFO)

    def get_logger(self):
        return self.logger


logger = Logger('trest').get_logger




