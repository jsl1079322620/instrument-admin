# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: interface_user.py
@create date: 2022/8/21 7:59
@description:
"""
from flask import request
from flask_restful import Resource

from api.user.user_singleton import user_singleton
from comm.comm_model_enum import modelEnum
from comm.comm_request_process import req
from comm.comm_response_process import response_result_process
from utils.log_config import logger

from comm.comm_response_code import response_code


class InterfaceUser(Resource):
    def get(self):
        try:
            data = {
                'code': 20000,
                'data': {
                    'token': 'admin-token'
                }
            }
            return response_result_process(data)
        except Exception as e:
            logger.error(e)
            error_data = response_code.GET_DATA_FAIL
            return response_result_process(error_data)

    def post(self):
        xml = request.args.get('format')
        try:
            request_data = req.request_process(request, xml, modelEnum.department.value)
            if isinstance(request_data, bool):
                request_data = response_code.REQUEST_PARAM_FORMAT_ERROR
                return response_result_process(request_data)
            if not request_data:
                data = response_code.REQUEST_PARAM_MISSED
                return response_result_process(data)
            fields = ['username', 'password']
            must = req.verify_all_param_must(request_data, fields)
            if must:
                return response_result_process(must)
            par_type = {'username': str, 'password': str}
            param_type = req.verify_all_param_type(request_data, par_type)
            if param_type:
                return response_result_process(param_type)
            data = {
                'code': 20000,
                'data': {
                    'token': 'admin-token'
                }
            }
            return response_result_process(data)
        except Exception as e:
            logger.error(e)
            error_data = response_code.TEST
            return response_result_process(error_data)
