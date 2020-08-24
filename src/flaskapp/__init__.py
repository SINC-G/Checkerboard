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

from flask import Flask, render_template, jsonify, g
from flaskapp.db import init_db


def create_app(test_config=None):
    """ flask工厂 """

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='user.sqlite'
    )  # 默认配置

    init_db(app)

    # 注册蓝图
    from . import checkerboard
    from .login import login
    checkerboard.register_bp(app)  # 如果这个内容不大的换成文件模块
    app.register_blueprint(login)

    @app.route('/')
    def index():
        return "404"

    logging.info('实例化成功！')
    return app
