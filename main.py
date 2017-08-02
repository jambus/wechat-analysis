#!/usr/bin/env python3

import sys
import sqlite3
import re

# main function to do anylsis of wechat chatting history
__default__MM__path = './data/MM.sqlite'
__default__Contact__path = './data/WCDB_Contact.sqlite'

tableNameList = []
contactList = []

def loadWechatSQLLib(mmPath, contactPath):
	
	#test purpose
	mmPath = __default__MM__path
	contactPath = __default__Contact__path
	
	conn = sqlite3.connect(mmPath)
	cursor = conn.cursor()

	tableNameList = listTableNames(cursor)
	#print(tableNameList)

	chatTableNameList = filter(isChatTable,tableNameList)
	print(chatTableNameList)

	cursor.close()
	#conn.commit()
	conn.close()
	return

def listTableNames(cursor):
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
	return cursor.fetchall()


isChatTablePattern = re.compile(r'^Chat_([0-9a-z]+)$')
def isChatTable(tuple):
	return isChatTablePattern.match(tuple[0])

def main():
	args = sys.argv
	print (args)
	argslength = len(args)
	if argslength < 3:
		print('Missing wechat sqlite file path!')
		exit(0);
	elif argslength == 3:
		loadWechatSQLLib(args[1],args[2])
		print 'Done';
	else:
		print('Too many arguments!')
		exit(0);

main()