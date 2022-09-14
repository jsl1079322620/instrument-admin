# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: resource.py
@create date: 2022/8/19 21:06
@description:
"""
from flask_restful import Api

from api.department.interface_department import InterfaceDepartment
from api.department.interface_department_staff import interfaceDepartmentStaff
# from api.login.interface_login import interfaceLogin
# from api.role.interface_permission import interfacePermission
# from api.role.interface_role import interfaceRole
# from api.role.interface_role_permission import interfaceRolePermission
# from api.user.interface_basic import interfaceUserBasic
# from api.user.interface_password import interfacePassword
# from api.user.interface_user import interfaceUser
# from api.user_group.interface_user_group import interfaceUserGroup
# from api.user_group.interface_user_group_role import interfaceUserGroupRole
# from api.user_group.interface_user_group_staff import interfaceUserGroupStaff
from api.login.interface_login import InterfaceLogin
from api.user.interface_user import InterfaceUser
from api.vue_element_admin.interface_vue import InterfaceVue

api = Api()

# 部门管理
api.add_resource(
    InterfaceDepartment,
    '/department',
    '/department/<int:dpt_id>'
)


api.add_resource(
    interfaceDepartmentStaff,
    '/department/staff/<int:dpt_id>'
)

# api.add_resource(
#     InterfaceUser,
#     '/user/info'
# )

api.add_resource(
    InterfaceLogin,
    '/login'
)

# # 用户
# api.add_resource(
#     interfaceUser,
#     '/user',
#     '/user/<int:user_id>',
#
# )
#
# # 密码
# api.add_resource(
#     interfacePassword,
#     '/user/<int:user_id>/password'
# )
#
# # 基本信息修改
# api.add_resource(
#     interfaceUserBasic,
#     '/user/<int:user_id>/base/info'
# )
#
# # 角色
# api.add_resource(
#     interfaceRole,
#     '/role',
#     '/role/<int:role_id>'
# )
# #  角色权限
# api.add_resource(
#     interfaceRolePermission,
#     '/role/<role_id>/permission'
# )
# # 权限
# api.add_resource(
#     interfacePermission,
#     '/permission'
# )
#
# # 用户组
# api.add_resource(
#     interfaceUserGroup,
#     '/user/group',
#     '/user/group/<int:group_id>'
# )
#
#
# api.add_resource(
#     interfaceUserGroupStaff,
#     '/user/group/<int:group_id>/staff'
# )
#
# # 获取用户组的角色信息
# api.add_resource(
#     interfaceUserGroupRole,
#     '/user/group/<int:group_id>/role'
# )
#
# api.add_resource(
#     interfaceLogin,
#     '/login'
# )
