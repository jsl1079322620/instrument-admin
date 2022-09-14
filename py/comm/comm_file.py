# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: comm_file
@create date: 2022/8/21 20:58
@description:
"""
import os
import datetime

from comm.comm_time import string_to_date, get_system_datetime
from config import configuration
from utils.log_config import logger


def make_dirs(path: str):
    try:
        path = path.strip()
        if not os.path.exists(path):
            os.makedirs(path)
            logger.info(f'文件夹创建成功: {path}')
        else:
            logger.info(f'文件夹已经存在: {path}')
    except Exception as e:
        logger.error(f"创建日志目录失败: {str(e)}")
        exit(1)


def remove_dir(path: str) -> bool:
    """
    删除一个非空目录
    :return:
    """
    try:
        if os.path.isdir(path):
            os.rmdir(path)
            logger.info(f'文件夹删除成功: {path}')
            # todo 建议记录到数据库
            return True
        else:
            logger.warning(f'不是文件夹, 不做删除: {path}')
            return False
    except Exception as e:
        logger.error(f'文件夹 {path} 删除失败：{str(e)}')
        return False


def del_log_dir():
    """
    删除几天前的日志, 见配置文件, 日志的目录时间必须为8位
    :return:
    """
    days_ago, log_path_root = configuration.get_log_config()
    make_dirs(log_path_root)
    dirs = os.listdir(log_path_root)
    remove_success_count = 0
    remove_fail_count = 0
    for dir_name in dirs:
        path = os.path.join(log_path_root, dir_name)
        if os.path.isdir(path) and len(dir_name) == 8:
            dir_name_days_ago = string_to_date(dir_name) + datetime.timedelta(days=int(days_ago))
            now = get_system_datetime()
            logger.info(f'{path}是文件夹, 文件夹名称{days_ago}天后对应的时间({dir_name_days_ago})如果小于当前时间为({now}), 则会被清理')
            if dir_name_days_ago < now:
                ret = remove_dir(path)
                if ret:
                    remove_success_count += 1
                else:
                    remove_fail_count += 1
    logger.info(f'日志清理结束: 共 {len(dirs)} 个文件夹, 清理成功 {remove_success_count} 个, 失败 {remove_fail_count} 个')
