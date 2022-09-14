# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: comm_error
@create date: 2022/9/1 16:40
@description:
"""
from utils.log_config import logger


class ERROR(object):
    def __init__(self, error_code, error_msg):
        self._error_code = error_code
        self._error_msg = error_msg
        logger.error(f'{self._error_code}: {self._error_msg}')
        pass


class request_param_format_error(ERROR('1001', '用户名或者密码错误')):
    pass
