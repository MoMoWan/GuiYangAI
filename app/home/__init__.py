#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: __init__.py.py
@time: 2017/11/4 下午1:32
"""

from flask import Blueprint

home  = Blueprint('home',__name__)

import app.home.views
