#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
登录路由（api）

@File    :   route.py
@Time    :   2020/08/24 16:23:11
@Author  :   snc 
"""

from flask import Blueprint, request, g, jsonify, render_template

from flaskapp.db import get_db

login = Blueprint('login', __name__, url_prefix='/login')


@login.route('', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        get_db()
        form = request.form
        res = g.db.execute(
            "select * from user where username=:username and password=:password", form)
        if res:
            session['username'] = form.get('username')
            session['password'] = form.get('password')
            # 登录成功，则跳转到index页面
            return jsonify({'code': 200})
    # 登录失败，跳转到当前登录页面
    return render_template('login.html')
