#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
棋盘验证路由

@File    :   route.py
@Time    :   2020/08/24 10:38:13
@Author  :   snc 
"""

from flask import Blueprint, request, session, jsonify

from .models import Checkerboard

cb = Blueprint('cb', __name__, url_prefix='/checkerboard')

flag = {"flag": ""}


@cb.route('/', methods=["POST", "GET"])
def index():
    if 'username' in session and 'password' in session:
        if request.method == "POST":
            form = request.get_json(force=True)
            if form['key'] == session['key']:
                return jsonify(flag)
            else:
                # 刷新
                return jsonify("400")
        else:
            checkerboard = Checkerboard()
            session['key'] = checkerboard.random_key()
            # 翻转硬币后发送
            checkerboard.flip_coin()
            return jsonify(checkerboard.cb)
