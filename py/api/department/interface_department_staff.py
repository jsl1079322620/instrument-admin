# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: interface_department_staff.py
@create date: 2022/8/20 10:16
@description:
"""
from flask import request
from flask_restful import Resource

from api.department.department_singleton import department_singleton
from utils.log_config import logger
from comm.comm_response_code import response_code
from comm.comm_model_enum import modelEnum
from comm.comm_response_process import response_result_process
from comm.comm_request_process import req


class interfaceDepartmentStaff(Resource):
    def get(self, dpt_id=None):
        xml = request.args.get('format')
        try:
            if dpt_id is None:
                data = response_code.HTTP_404_NOT_FOUND
                return response_result_process(data, xml=xml)

            request_data = req.request_process(request, xml, modelEnum.department.value)
            if isinstance(request_data, bool):
                request_data = response_code.REQUEST_PARAM_FORMAT_ERROR
                return response_result_process(request_data, xml=xml)
            if not request_data:
                data = response_code.REQUEST_PARAM_MISSED
                return response_result_process(data, xml=xml)
            fields = ['current_page', 'page_size']
            must = req.verify_all_param_must(request_data, fields)
            if must:
                return response_result_process(must, xml=xml)
            par_type = {'page_size': int, 'current_page': int}
            param_type = req.verify_all_param_type(request_data, par_type)
            if param_type:
                return response_result_process(param_type, xml=xml)

            current_page, page_size = int(request_data.get('current_page')), int(request_data.get('page_size'))
            data = department_singleton.get_dpt_user_info_by_id(dpt_id, current_page, page_size)
            body = modelEnum.department.value.get('body')
            return response_result_process(data, xml_structure_str=body, xml=xml)
        except Exception as e:
            logger.error(e)
            error_data = response_code.GET_DATA_FAIL
            return response_result_process(error_data, xml=xml)

    def post(self, dpt_id=None):
        xml = request.args.get('format')
        try:
            if dpt_id is None:
                data = response_code.HTTP_404_NOT_FOUND
                return response_result_process(data, xml=xml)
            request_data = req.request_process(request, xml, modelEnum.department.value)
            if isinstance(request_data, bool):
                request_data = response_code.REQUEST_PARAM_FORMAT_ERROR
                return response_result_process(request_data, xml=xml)
            if not request_data:
                data = response_code.REQUEST_PARAM_MISSED
                return response_result_process(data, xml=xml)
            fields = ['user_ids']
            must = req.verify_all_param_must(request_data, fields)
            if must:
                return response_result_process(must, xml=xml)
            par_type = {'user_ids': list}
            param_type = req.verify_all_param_type(request_data, par_type)
            if param_type:
                return response_result_process(param_type, xml=xml)
            user_ids = str(request_data.get('user_ids'))
            data = department_singleton.department_add_staff(dpt_id, user_ids)
            return response_result_process(data, xml=xml)
        except Exception as e:
            logger.error(e)
            error_data = response_code.ADD_DATA_FAIL
            return response_result_process(error_data, xml=xml)

    def delete(self, dpt_id=None):
        xml = request.args.get('format')
        try:
            if dpt_id is None:
                data = response_code.HTTP_404_NOT_FOUND
                return response_result_process(data, xml=xml)
            request_data = req.request_process(request, xml, modelEnum.department.value)
            if isinstance(request_data, bool):
                request_data = response_code.REQUEST_PARAM_FORMAT_ERROR
                return response_result_process(request_data, xml=xml)
            if not request_data:
                data = response_code.REQUEST_PARAM_MISSED
                return response_result_process(data, xml=xml)
            fields = ['user_ids']
            must = req.verify_all_param_must(request_data, fields)
            if must:
                return response_result_process(must, xml=xml)
            par_type = {'user_ids': list}
            param_type = req.verify_all_param_type(request_data, par_type)
            if param_type:
                return response_result_process(param_type, xml=xml)
            user_ids = str(request_data.get('user_ids'))

            data = department_singleton.delete_department_staff(dpt_id, user_ids)
            return response_result_process(data, xml=xml)

        except Exception as e:
            logger.error(e)
            error_data = response_code.DELETE_DATA_FAIL
            return response_result_process(error_data, xml=xml)
