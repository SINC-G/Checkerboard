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


def create_app(test_config=None):
    """ flask工厂 """

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )  # 默认配置

    # 读取实例文件夹内的配置或测试配置
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # 创建实例文件夹
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 注册蓝图
    from . import checkerboard
    checkerboard.register_bp(app)

    @app.route('/')
    def index():
        return "404"

    logging.info('实例化成功！')
    return app
