# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: start.py
@create date: 2022/8/19 21:39
@description:
"""
import os

from api import create_app
from config import configuration

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    host, port, debug = configuration.get_start_config()
    app.run(host=host, port=port, debug=eval(debug))
