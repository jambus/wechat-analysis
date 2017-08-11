#!/usr/bin/env python3

import datetime as dt

from classes.wechatMessage import WechatMessage

class WechatMessageAnalysis(object):

	def __init__(self):
		pass

	def handleChatHistoryData(self,data):
		if len(data) == 0:
			pass

		historyList = []
		for record in data:
			message = WechatMessage()
			message.createTime = record[0]
			message.sender = self._getMessageSender(record)
			message.message = self._getMessageBody(record)
			message.status = record[2]
			message.type = record[3]
			message.isMyMessage = (record[4] == 0)

			historyList.append(message)

		return historyList

	def _getMessageSender(sef, record):
		if record[4] == 0:
			return 'me'
		else:
			return record[1].split(':', 1)[0]

	def _getMessageBody(sef, record):
		if record[4] == 0:
			return record[1]
		else:
			recordSplitList = record[1].split(':', 1)
			return recordSplitList[1] if len(recordSplitList)==2 else record[1]

	def printChatHistoryData(self,wechatMessageList):
		if len(wechatMessageList) == 0:
			pass
		
		formatRecordStr = ''
		for message in wechatMessageList:
			formatRecordStr += dt.datetime.fromtimestamp(message.createTime).strftime('%Y-%m-%d %H:%M:%S')
			formatRecordStr += ' ' + message.sender + ':' + '\n'
			formatRecordStr += message.message + '\n'
			formatRecordStr += '\n'

		print(formatRecordStr)
		pass
