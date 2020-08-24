#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
登录路由（api）

@File    :   route.py
@Time    :   2020/08/24 16:23:11
@Author  :   snc 
"""

from flask import Blueprint, request, g

from flaskapp.db import get_db

login = Blueprint('login', __name__, url_prefix='/login')


@login.route('', methods=['POST', 'GET'])
def index():
    get_db()

    if request.method == "GET":
        pass

    if request.method == "POST":
        # 用户名，密码
        form = request.form
        res = g.db.execute(
            "select * from user where username=:username and password=:password", form)
        if res:
            return "200"
        else:
            return "密码或用户名错误"
        # 信息暂定
