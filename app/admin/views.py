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
from flask import render_template,redirect,url_for


@admin.route("/")
def index():
    return render_template("admin/index.html")

@admin.route("/login/")
def login():
    return render_template("admin/login.html")

@admin.route("/logout/")
def logout():
    return redirect(url_for("admin.login"))

@admin.route("/pwd/")
def pwd():
    return render_template("admin/pwd.html")

@admin.route("/tag/add/")
def tag_add():
    return render_template("admin/tag_add.html")

@admin.route("/tag/list/")
def tag_list():
    return render_template("admin/tag_list.html")

@admin.route("/movie/add/")
def movie_add():
    return render_template("admin/movie_add.html")

@admin.route("/movie/list/")
def movie_list():
    return render_template("admin/movie_list.html")

@admin.route("/preview/add/")
def preview_add():
    return render_template("admin/preview_add.html")

@admin.route("/preview/list/")
def preview_list():
    return render_template("admin/preview_list.html")