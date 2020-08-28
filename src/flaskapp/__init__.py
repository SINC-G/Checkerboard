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
        SECRET_KEY='1jL\xed\x03U\x8eZ\xa0qp\xe6\xe1\xb5\xf8w\x06l?]\x02gBH',
        DATABASE='user.sqlite',
        template_folder="static"
    )  # 默认配置

    # init_db(app)

    # 注册蓝图
    from . import checkerboard
    from . import login
    checkerboard.register_bp(app)  # 如果这个内容不大的换成文件模块
    app.register_blueprint(login.login)

    @app.route('/')
    def index():
        if 'username' in session and 'password' in session:
            # 发送棋盘（前端来获取），类似

            # 这里应该返回200，未授权返回401
            return jsonify({"status": 200}), 200
        return jsonify({"code": "401", "info": "未授权"}), 401

    logging.info('实例化成功！')
    return app
