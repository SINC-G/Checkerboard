#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
flask应用

@File    :   __init__.py
@Time    :   2020/08/24 10:30:54
@Author  :   snc 
"""

import os
import logging

from flask import Flask, render_template, jsonify, g, session, redirect, url_for
from flaskapp.db import init_db


def create_app(test_config=None):
    """ flask工厂 """

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='user.sqlite'
    )  # 默认配置

    # init_db(app)

    # 注册蓝图
    from . import checkerboard
    from . import login
    checkerboard.register_bp(app)  # 如果这个内容不大的换成文件模块
    app.register_blueprint(login.login)

    @app.route('/')
    def index():
        # 如果用户名和密码都存在，则跳转到index页面，登录成功
        if 'username' in session and 'password' in session:
            # 发送棋盘（前端来获取），类似
            return render_template('index.html')
        # 否则，跳转到login页面
        return redirect(url_for('login.main'))

    logging.info('实例化成功！')
    return app
