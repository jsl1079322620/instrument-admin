# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: interface_login
@create date: 2022/9/1 10:43
@description:
"""
import uuid

from flask import request
from flask_restful import Resource

from comm.comm_model_enum import modelEnum
from comm.comm_request_process import req
from comm.comm_response_process import response_result_process
from utils.auth import Auth
from utils.log_config import logger
from comm.comm_response_code import response_code


class InterfaceLogin(Resource):
    @staticmethod
    def post():
        try:
            request_data = req.request_process(request)
            logger.info('123')
            logger.info(request_data)
            login_user_id, login_password = request_data.get('user_id'), request_data.get('password')
            Auth.authenticate(login_user_id, login_password)

            data = {
                'code': 200,
                'data': {
                    'token': 'admin-token'
                }
            }

            return response_result_process(data)
        except Exception as e:
            logger.error(e)
            error_data = response_code.EXCEPTION_ERROR(e)
            return response_result_process(error_data)
