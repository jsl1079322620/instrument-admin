# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: config.py
@create date: 2022/8/19 21:43
@description:
"""
import configparser
import os.path

from comm.comm_time import get_system_year_str
from utils.constants import Constants

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Configuration:
    """
    读取数据库配置文件中的的用户信息,密码信息，主机信息，端口信息,数据库名称信息
    config_path: 是配置文件的路径
    """
    COMPANY = ''
    EMAIL = ''
    COPYRIGHT_CUR_YEAR = '版权所有 ©' + get_system_year_str() + COMPANY

    def __init__(self):
        try:
            self.config_file_path = os.path.join(BASE_DIR, 'config.ini')
            self.conf = configparser.ConfigParser()
            self.conf.read(self.config_file_path, encoding=Constants.ENCODING)
        except Exception as e:
            # 文件不存在或者读取失败
            print(str(e))

    def set_option_value(self, section, option, value=None):
        """
        :param section:
        :param option:
        :param value:
        :return:
        """
        self.conf.set(section, option, value)

    def write_file(self):
        """
        保存对配置文件的修改
        :return:
        """
        self.conf.write(open(self.config_file_path, 'r+'))

    def get_version(self):
        """
        获取版本信息
        :return:
        """
        return self.conf.get('Version', 'version')

    def get_build(self):
        """
        获取build信息
        :return:
        """
        return self.conf.get('Version', 'build')

    @staticmethod
    def get_company_email(self):
        """
        获取公司邮箱
        :return:
        """
        return Configuration.EMAIL

    @staticmethod
    def get_copyright(self):
        """
        获取版权信息
        :return:
        """
        return Configuration.COPYRIGHT_CUR_YEAR

    def get_database_name(self, database_section='DB'):
        """
        获取数据库的名称
        :param database_section:配置文档区域名称 如IPCONFIG、DB1
        :return:
        """
        if self.conf.has_section(database_section):
            return self.conf.get(database_section, 'name')
        return None

    def get_option(self, section, option):
        """
        获取配置文件选项
        :param section:
        :param option:
        :return:
        """
        return self.conf.get(section, option)

    def set_option(self, section, option, value):
        """
        设置配置文件选项
        :param section:配置文档区域名称 如IPCONFIG、DB1
        :param option:配置文档区域中选项名称，如name、host
        :param value: 选项的值
        :return:
        """
        # 修改选项
        self.conf.set(section, option, value)
        # 保存修改
        self.write_file()

    def get_database_configuration(self, database_section):
        """
        获取数据库连接详细信息
        :param database_section:配置文档区域名称 如IPCONFIG、DB1
        :return:
        """
        return {
            'name': self.conf.get(database_section, 'name'),
            'type': self.conf.get(database_section, 'type'),
            'host': self.conf.get(database_section, 'host'),
            'port': self.conf.get(database_section, 'port'),
            'user': self.conf.get(database_section, 'user'),
            'pwd': self.conf.get(database_section, 'pwd')
        }

    def get_start_config(self, section='IPCONFIG'):
        """
        获取启动配置
        :param section:
        :return:
        """

        host = self.conf.get(section, 'host')
        port = self.conf.get(section, 'port')
        debug = self.conf.get(section, 'debug')

        return host, port, debug

    def get_log_config(self, section='LOG'):
        days_ago = self.conf.get(section, 'delete_log_days_ago')
        log_path_root = self.conf.get(section, 'log_path_root')
        return days_ago, log_path_root


configuration = Configuration()


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'USER-API'
    # ##flask-session
    SESSION_TYPE = 'null'
    SESSION_KEY_PREFIX = "session:"
    # 如果设置SESSION_PERMANENT为 True 的话，session的生命为 permanent_session_lifetime 秒（默认是31天）
    # 如果设置SESSION_PERMANENT为 False 的话，那么当用户关闭浏览器时，session便被删除了。permanent_session_lifetime也会生效
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 60 * 60 * 24 * 31

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    DB_CONFIG = {'host': '192.168.1.60', 'port': 3306, 'user': 'devuser', 'password': 'root', 'db': 'data',
                 'connect_timeout': 300, 'read_timeout': 300, 'write_timeout': 300,
                 'charset': 'utf8'}
    pass


class TestingConfig(Config):
    TESTING = False
    DB_CONFIG = {'host': '192.168.1.60', 'port': 3306, 'user': 'devuser', 'password': 'root', 'db': 'data',
                 'connect_timeout': 300, 'read_timeout': 300, 'write_timeout': 300,
                 'charset': 'utf8'}
    pass


class ProductionConfig(Config):
    DEBUG = False
    DB_CONFIG = {'host': '192.168.1.60', 'port': 3306, 'user': 'devuser', 'password': 'root', 'db': 'data',
                 'connect_timeout': 300, 'read_timeout': 300, 'write_timeout': 300,
                 'charset': 'utf8'}
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
