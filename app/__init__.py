#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: __init__.py.py
@time: 2017/11/4 下午1:32
"""

from flask import  Flask

app = Flask(__name__)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint,url_prefix='/admin')

