#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
棋盘验证路由

@File    :   route.py
@Time    :   2020/08/24 10:38:13
@Author  :   snc
"""

import os
from flask import Blueprint, request, session, jsonify

from .models import Checkerboard

cb = Blueprint('cb', __name__, url_prefix='/checkerboard')

flag_path = "/flag.txt"

with open(flag_path, "r") as f:
    text = f.read()
flag = {"flag": text}


@cb.route('', methods=["POST", "GET"])
def index():
    if 'username' in session and 'password' in session:
        if request.method == "POST":
            form = request.get_json(force=True)
            if form['key'] == session['key']:
                return jsonify(flag)
            else:
                checkerboard = Checkerboard()
                session['key'] = checkerboard.get()
                return jsonify({"cb": checkerboard.cb, "flip": checkerboard.flip})
        else:
            checkerboard = Checkerboard()
            session['key'] = checkerboard.get()
            print(checkerboard.solve())
            return jsonify({"cb": checkerboard.cb, "flip": checkerboard.flip})
