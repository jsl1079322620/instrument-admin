# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: test
@create date: 2022/9/4 14:21
@description:
"""
import os

from comm.comm_time import get_system_date_str, get_system_time_str


class StringUtils(str):

    def __init__(self, s):
        self._s = s

    def ret_str(self, default=789):
        if self._s == 0:
            return self.__str__()
        else:
            return default


if __name__ == '__main__':
    import logging
    # logging.basicConfig(filename=os.path.join(os.getcwd(), '../../log', '123', get_system_date_str(), get_system_time_str() + '.log'))
    print(logging)
