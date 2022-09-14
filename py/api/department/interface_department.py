# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: interface_department.py
@create date: 2022/8/19 22:38
@description:
"""
import os.path

from flask import request
from flask_restful import Resource

from api.department.department_singleton import department_singleton
from comm.comm_response_code import response_code
from comm.comm_request_process import req
from comm.comm_response_process import response_result_process

from comm.comm_model_enum import modelEnum

from utils.log_config import logger


class InterfaceDepartment(Resource):
    def get(self, dpt_id=None):
        print('get:', globals())
        try:
            if dpt_id is not None:
                data = response_code.HTTP_404_NOT_FOUND
                return response_result_process(data)
            data = department_singleton.get_department()
            body = modelEnum.department.value.get('body')
            return response_result_process(data, xml_structure_str=body)
        except Exception as e:
            logger.error(e)
            error_data = response_code.GET_DATA_FAIL
            return response_result_process(error_data)

    def post(self, dpt_id=None):
        print('post:', os.path.basename(__file__))
        xml = request.args.get('format')
        try:
            if dpt_id is not None:
                data = response_code.HTTP_404_NOT_FOUND
                return response_result_process(data)
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
            dpt_name, dpt_p_id = request_data.get('dpt_name'), request_data.get('p_id')
            data = department_singleton.add_department(dpt_name, dpt_p_id)
            return response_result_process(data)
        except Exception as e:
            logger.error(e)
            error_data = response_code.TEST
            return response_result_process(error_data)

    def put(self, dpt_id=None):
        print('put:', globals())
        xml = request.args.get('format')
        try:
            if dpt_id is None:
                data = response_code.HTTP_404_NOT_FOUND
                return response_result_process(data)

            if dpt_id is not None:
                request_data = req.request_process(request, xml, modelEnum.department.value)
                if isinstance(request_data, bool):
                    request_data = response_code.REQUEST_PARAM_FORMAT_ERROR
                    return response_result_process(request_data)
                if not request_data:
                    data = response_code.REQUEST_PARAM_MISSED
                    return response_result_process(data)

                fields = ['dpt_name', 'p_id']
                must = req.verify_all_param_must(request_data, fields)
                if must:
                    return response_result_process(must)

                par_type = {'dpt_name': str, 'p_id': int}

                param_type = req.verify_all_param_type(request_data, par_type)
                if param_type:
                    return response_result_process(param_type)
                dpt_name = request_data.get('dpt_name')
                p_id = request_data.get('p_id')
                data = department_singleton.update_department(dpt_id, dpt_name, p_id)
                return response_result_process(data)
        except Exception as e:
            logger.error(e)
            error_data = response_code.UPDATE_DATA_FAIL
            return response_result_process(error_data)

    def delete(self, dpt_id=None):
        print('delete:', globals())
        xml = request.args.get('format')
        try:
            if dpt_id is None:
                data = response_code.HTTP_404_NOT_FOUND
                return response_result_process(data)

            if dpt_id is not None:
                data = department_singleton.delete_department(dpt_id)
                return response_result_process(data)

        except Exception as e:
            logger.error(e)
            error_data = response_code.DELETE_DATA_FAIL
            return response_result_process(error_data)
