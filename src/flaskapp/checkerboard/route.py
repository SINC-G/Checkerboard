#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
棋盘验证路由

@File    :   route.py
@Time    :   2020/08/24 10:38:13
@Author  :   snc 
"""

from flask import Blueprint

cb = Blueprint('cb', __name__, url_prefix='/cb')


@cb.route('/')
def index():
    return '棋盘'
