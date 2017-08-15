import datetime as dt
import re

from classes.wechatMessage import WechatMessage
from classes.wechatMessageType import WechatMessageType
from classes.wechatAnalysisInterface import WechatAnalysisInterface

class WechatMessageAnalysisProcessor(object):

	def __init__(self):
		self._analysiserList = []
		self._aliasNameDict = {}
		pass

	def loadAliasNameList(self,data):
		if len(data) == 0:
			pass

		for record in data:
			self._aliasNameDict[record[0]] = self._handleAliasToClearUnexpectedChars(record[1])

		return self._aliasNameDict

	def _handleAliasToClearUnexpectedChars(self, aliasName):
		if(not hasattr(self,'_aliasPattern')):
			self._aliasPattern = re.compile(r'^\n\W(.+?)\x12.*')
		result = self._aliasPattern.match(aliasName)

		if result == None:
			return aliasName
		else:
			return result.group(1)

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

			try:
				message.type = WechatMessageType(record[3])
			except ValueError:
				print('Unhandled message type' + str(record[3]))
				message.type = WechatMessageType.UNHANDLED
			
			message.isMyMessage = (record[4] == 0)
			historyList.append(message)

		return historyList

	def _getMessageSender(self, record):
		if record[4] == 0:
			return 'me'
		else:
			if record[3] in [WechatMessageType.VIDEO1.value,WechatMessageType.VIDEO2.value]:
				return 'Unhandled sender for type VIDEO'
			else:
				return self._linkAliasName(record[1].split(':', 1)[0])

	def _linkAliasName(self,wechatId):
		if len(self._aliasNameDict) == 0:
			return wechatId
		else:
			if(wechatId in self._aliasNameDict):
				return self._aliasNameDict[wechatId]
			else:
				return wechatId

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

	def registerAnalysiser(self, wechatAnalysisers):
		if isinstance(wechatAnalysisers, WechatAnalysisInterface):
			self._analysiserList.append(wechatAnalysisers)
		else:
			print('Fail to load wechatAnalysiser' + str(wechatAnalysisers))

	def executeAnalysis(self,dataList):
		if len(self._analysiserList) == 0:
			pass

		for anaylsiser in self._analysiserList:
			anaylsiser.execute(dataList)

		print('Anaylsis done')

