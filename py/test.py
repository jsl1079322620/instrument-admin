# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: test
@create date: 2022/9/4 14:21
@description:
"""


class StringUtils(str):

    def __init__(self, s):
        self._s = s

    def ret_str(self, default=789):
        if self._s == 0:
            return self.__str__()
        else:
            return default


if __name__ == '__main__':
    a = StringUtils(1).ret_str()
    print(a, type(a))
