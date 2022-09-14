# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: comm_api_version.py
@create date: 2022/8/20 10:26
@description:
"""

from enum import Enum, unique


@unique
class apiVersion(Enum):
    """
    api 版本枚举
    """
    version1 = 'v1'
    version2 = 'v2'
