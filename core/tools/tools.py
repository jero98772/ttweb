#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#ttweb - by jero98772
from hashlib import  sha256
import base64
import datetime
from subprocess import run
def enPassowrdStrHex(password):
	password = str(password)
	hashPassowrd = str(sha256(password.encode('utf-8')).hexdigest())
	return hashPassowrd
def enPassowrdHash(password):
	password = str(password)
	hashPassowrd = sha256(password.encode("utf-8")).digest()
	return hashPassowrd
def generatePassword():
	"""generatePassword(),return srtring
	generate random string 
	"""
	genPassowrd = ""
	for i in range(0,16):
		if len(genPassowrd) >= 16 and len(genPassowrd)-len(hexStr) <= 16:
			num = rnd.randint(0,9999)
			if 32 > num >126:
				char = chr(num)
				genPassowrd += char
			else:
				hexStr = str(hex(hexStr))
				genPassowrd += hexStr
		else:
			break
	return genPassowrd
def createLedgerFile(name):
	"""
	writetxt(name,content) , write in txt file something  
	"""
	with open(name, 'w') as file:
		file.write("")
		file.close()
def readtxt(name):
	"""
	readtxt(name) , return txt content as array ,element by line 
	"""
	content = []
	with open(name, 'r') as file:
		for i in file.readlines():
			content.append(str(i).replace("\n",""))
	return reversed(content)
def formatin(category):
	now=datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
	return "i "+now+" "+category+"\n"
def formatout():
	now=datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
	return "o "+now+"\n"
def writef(fname,content):

	"""
	writetxt(name,content) , write in txt file something  
	"""
	with open(fname, 'a') as file:
		file.write(content)
		file.close()
#def outcategory():
def getbal(fname,txt="data/tmp.txt"):
	run(f"ledger -f {fname} bal > {txt}",shell=True)
	return readtxt(txt)
