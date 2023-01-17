#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#ttweb - by jero98772
from flask import Flask, render_template, request, flash, redirect ,session
from core.tools.dbInteracion import dbInteracion
from core.tools.tools import *
app = Flask(__name__)
app.secret_key = str(enPassowrdHash(generatePassword()))
DBPATH = "data/"
DATAUSER="data/datauser/"
DBNAMEGAS = DBPATH + "db"
class webpage():
  @app.route("/",methods = ['GET','POST'])
  def index():
    data=""
    if request.method == 'POST':
      if session['status']:
        if request.form["category"]:
          session['status']=False
          writef(session['file'] ,formatin(data))
      else:
        writef(session['file'] ,formatout())
        session['status']=True
    return render_template("index.html",data=data)
  @app.route("/login.html",methods = ['GET','POST'])
  def login():
    if request.method == 'POST':
      db = dbInteracion(DBNAMEGAS)
      db.connect("login")
      usr = request.form["username"]
      if db.findUser(usr) and db.findPassword(enPassowrdStrHex(request.form["password"])):
        session['loged'] = True
        session['user'] = usr
        file=DATAUSER+usr+".ldg"
        session['file'] = file
        session['status']=True
        return redirect("/")
    return render_template("login.html")
  @app.route("/register",methods = ['GET','POST'])
  def register():
    msg=""
    if request.method == 'POST':
      pwd = request.form["pwd"]
      pwd2 = request.form["pwd2"]
      if pwd == pwd2 :
        usr = request.form["usr"]
        db = dbInteracion(DBNAMEGAS)
        db.connect("login")
        if db.findUser(usr):
          msg="User alredy register"
        else:
          if db.userAvailable(usr,"usr") :
            db.saveUser(usr,enPassowrdStrHex(pwd))
            try:
              file=DATAUSER+usr+".ldg"
              createLedgerFile(file)
              session['status']=True
              session['loged'] = True
              session['user'] = usr
              session['file'] = file
            except db.userError():
              return "invalid user , please try with other username and password"		
      else:
        msg="Passwords must be same"
    return render_template("register.html",msg=msg)
  @app.route("/unlog")
  def unlog():
    session['loged']=False
    return redirect("/")
  @app.route("/data.html")
  def data():
    data=""
    try:
      if session['loged']:
        data=getbal(session['file'])
    except:
        data="you need login"
    return render_template("data.html",data=data)