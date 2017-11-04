#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: views.py
@time: 2017/11/4 下午1:34
"""


from . import admin

@admin.route("/")
def index():
    return "<h1 style='color:red'>this is admin</h1>"