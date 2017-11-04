#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: __init__.py.py
@time: 2017/11/4 下午1:33
"""


from flask import Blueprint

admin  = Blueprint('admin',__name__)

import app.admin.views