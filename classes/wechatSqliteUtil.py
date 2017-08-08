#!/usr/bin/env python3

import sqlite3
import re

class WechatSqliteUtil(object):

	# default wechat sqlite path
	#_mm_path = './data/MM.sqlite'
	#_contact__path = './data/WCDB_Contact.sqlite'
	#_BbChatRoomNameHash = 'a562c223491ef22e6bb398e66a7ec84b'

	def __init__(self, mmPath, contactPath):
		if(mmPath == None):
			self._mm_path = './data/MM.sqlite'
		else:
			self._mm_path = mmPath

		if(contactPath == None):
			self._contact__path = './data/WCDB_Contact.sqlite'
		else:
			self._contact__path = contactPath
		self._bbChatRoomNameHash = 'a562c223491ef22e6bb398e66a7ec84b'

	def loadWechatDB(self):
		self._connMM = sqlite3.connect(self._mm_path)
		self._cursorMM = self._connMM.cursor()

		self._connContact = sqlite3.connect(self._contact__path)
		self._cursorContact = self._connContact.cursor()
		return

	def closeWechatDB(self):
		try:
			self._cursorMM.close()
			#self.conn.commit()
			self._connMM.close()

			self._cursorContact.close()
			#self.conn.commit()
			self._connContact.close()
		finally:
			print('Close wechat DB')
		return

	def listTableNames(self):
		self._cursorMM.execute("SELECT name FROM sqlite_master WHERE type='table';")
		return self._cursorMM.fetchall()

	def listChatRooms(self):
		self._cursorContact.execute("SELECT userName, cast(dbContactRemark as TEXT) FROM Friend WHERE userName like '%@chatroom';")
		return self._cursorContact.fetchall()

	def _isChatTable(self,tuple):
		if(not hasattr(self,'_chatTablePattern')):
			self._chatTablePattern = re.compile(r'^Chat_([0-9a-z]{32})$')
		return self._chatTablePattern.match(tuple[0])

	def findChatRoomTableByRoomName(self,targetChatRoomName):
		tableNameList = self.listTableNames()

		chatTableNameList = filter(self._isChatTable,tableNameList)
		#print(chatTableNameList)

		chatRoomList = self.listChatRooms()
		print(chatRoomList)

		for table in chatRoomList:
			if targetChatRoomName in table[1]:
				print('Find room ' + targetChatRoomName + ' , Room id is:'+ table[0])
				return table[0]

		print('Room not found')
		return None

