#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
棋盘验证

@File    :   __init__.py
@Time    :   2020/08/24 10:35:50
@Author  :   snc 
"""

from . import route


def register_bp(app):
    """ 注册蓝图到应用中. """
    app.register_blueprint(route.cb)
