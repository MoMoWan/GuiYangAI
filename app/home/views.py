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
from flask import render_template,redirect,url_for

@home.route("/")
def index():
    return render_template("home/index.html")

@home.route("/login/")
def login():
    return render_template("home/login.html")

@home.route("/logout/")
def logout():
    return redirect(url_for("home.login"))

@home.route("/regist/")
def regist():
    return render_template("home/regist.html")