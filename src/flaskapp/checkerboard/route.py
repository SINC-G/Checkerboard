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


@cb.route('/', method=["POST", "GET"])
def index():
    if request.method == "POST":
        if 'username' in session and 'password' in session:
            form = request.get_json(force=True)
            if form['key'] == session['key']:
                return jsonify(flag)
    checkerboard = Checkerboard()
    session['key'] = checkerboard.random_key()
    # 翻转硬币后发送
    checkerboard.flip_coin()
    return jsonify(checkerboard.cb)
