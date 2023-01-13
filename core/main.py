#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#ttweb - by jero98772
from flask import Flask, render_template, request, flash, redirect ,session
from tools.dbInteracion import dbInteracion
from tools.tools import *
app.secret_key = str(enPassowrdHash(generatePassword()))
DBPATH = "data/"
DBNAMEGAS = DBPATH + "db"
app = Flask(__name__)
class webpage():
  @app.route("/")
  def index():
    return render_template("index.html")
  @app.route("/register")
  def register():
    if request.method == 'POST':
      pwd = request.form["pwd"]
      pwd2 = request.form["pwd2"]
      if pwd == pwd2 :
        usr = request.form["usr"]
        db = dbInteracion(DBNAMEGAS)
        db.connect("login")
        if db.userAvailable(usr,"usr") :
          encpwd = enPassowrdStrHex(pwd+usr) 
          db.saveUser(usr,enPassowrdStrHex(pwd))
          try:
            createLedgerFile(encpwd)
            session['loged'] = True
            session['user'] = usr
            session['file'] = encpwd
          except db.userError():
            return "invalid user , please try with other username and password"		
    return render_template("register.html")
  @app.route("/unlog")
  def register():
  	session['loged']=False
    return redirect("/")