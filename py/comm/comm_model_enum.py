# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: comm_model_enum.py
@create date: 2022/8/20 10:46
@description:
"""

from enum import Enum, unique


@unique
class modelEnum(Enum):
    """
    请求模块枚举类
    """

    user = {'root': 'users', 'body': 'user'}
    department = {'root': 'departments', 'body': 'department'}
    role = {'root': 'roles', 'body': 'role'}
    user_group = {'root': 'user_groups', 'body': 'user_group'}
    login = {'root': 'logins', 'body': 'login'}
    permission = {'root': 'permissions', 'body': 'permission'}
    role_permission = {'root': 'role_permissions', 'body': 'role_permission'}
