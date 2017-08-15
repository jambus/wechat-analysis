import datetime as dt

from classes.wechatMessage import WechatMessage
from classes.wechatMessageType import WechatMessageType
from classes.wechatAnalysisInterface import WechatAnalysisInterface

class WechatMessageAnalysisProcessor(object):

	def __init__(self):
		self._analysiserList = []
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

			try:
				message.type = WechatMessageType(record[3])
			except ValueError:
				print('Unhandled message type' + str(record[3]))
				message.type = WechatMessageType.UNHANDLED
			
			message.isMyMessage = (record[4] == 0)
			historyList.append(message)

		return historyList

	def _getMessageSender(sef, record):
		if record[4] == 0:
			return 'me'
		else:
			if record[3] in [WechatMessageType.VIDEO1.value,WechatMessageType.VIDEO2.value]:
				return 'Unhandled sender for type VIDEO'
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

