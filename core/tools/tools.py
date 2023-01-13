#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#ttweb - by jero98772
def enPassowrdStrHex(password):
	password = str(password)
	hashPassowrd = str(sha256(password.encode('utf-8')).hexdigest())
	return hashPassowrd
def enPassowrdHash(password):
	password = str(password)
	hashPassowrd = sha256(password.encode("utf-8")).digest()
	return hashPassowrd
def createLedgerFile(name):
	"""
	writetxt(name,content) , write in txt file something  
	"""
	with open(name, 'w') as file:
		file.write("")
		file.close()