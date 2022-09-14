# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: mysql_conn_pool
@create date: 2022/9/4 17:04
@description:
"""

import pymysql
from dbutils.pooled_db import PooledDB

from config import configuration
from utils.log_config import logger


class MysqlConn(object):
    """
    MySql线程池
    """
    __my_pool = None

    # ##以何种方式返回数据集
    TUPLE_CURSOR_MODE = pymysql.cursors.Cursor
    DICT_CURSOR_MODE = pymysql.cursors.DictCursor
    SS_TUPLE_CURSOR_MODE = pymysql.cursors.SSCursor
    SS_DICT_CURSOR_MODE = pymysql.cursors.SSDictCursor

    def __init__(self, database_name='DB', cur_type=TUPLE_CURSOR_MODE):
        self.conn = MysqlConn.get_connection(database_name)
        self.cur = self.conn.cursor(cursor=cur_type)
        logger.info('连接数据库')

    @staticmethod
    def get_connection(database_name):
        """
        获取数据库连接
        :return:
        """
        database = configuration.get_database_configuration(database_name)
        host = database.get('host')
        port = int(database.get('port'))
        user = database.get('user')
        password = database.get('pwd')
        if MysqlConn.__my_pool is None:
            MysqlConn.__my_pool = PooledDB(creator=pymysql, mincached=1, maxcached=10, maxconnections=100,
                                           blocking=True,
                                           host=host, port=port, user=user, passwd=password,
                                           charset='utf8')
        return MysqlConn.__my_pool.connection()

    def close(self):
        """
        释放当前连接
        :return:
        """
        self.conn.close()
        self.cur.close()
        logger.info('关闭数据库')
