#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: views.py
@time: 2017/11/4 下午1:34
"""


from . import home
from flask import render_template

@home.route("/")
def index():
    return render_template("home/index.html")

