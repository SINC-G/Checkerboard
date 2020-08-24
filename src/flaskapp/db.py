#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
数据库

@File    :   db.py
@Time    :   2020/07/21 13:58:33
@Author  :   snc 
"""

import sqlite3
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'])
        # g.db.row_factory = json_factory  # 行字典处理
    return g.db


def close_db(e):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db(app):
    db = sqlite3.connect(app.config['DATABASE'])
    with open('user.sql', 'r', encoding='utf-8') as f:
        db.executescript(f.read())
    db.commit()
    return db
