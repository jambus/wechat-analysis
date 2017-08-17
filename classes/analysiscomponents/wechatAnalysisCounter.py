from classes.wechatAnalysisInterface import WechatAnalysisInterface
from classes.analysiscomponents.wechatCommonAnalysiser import WechatCommonAnalysiser
from classes.wechatMessageType import WechatMessageType

class WechatAnalysisCounter(WechatCommonAnalysiser):
	
	def execute(self,dataList):
		self.userMessageCounts(dataList)
		self.userWelcomeMessageCounts(dataList)
		self.userHappyBirthdayMessageCounts(dataList)
		pass

	def userMessageCounts(self,dataList):

		#filter
		userMessageFilter = lambda x: x.type in self.getWechatUserMessageTypeList()
		validDataList = filter(userMessageFilter,dataList)

		userReducedCounter = self.mapReduceCountsByList(validDataList)

		topMessageUserList = userReducedCounter.most_common(3)

		if len(list(topMessageUserList)) == 0:
			print('群里没有人说话')
		else:
			print('群里话最多的前',len(topMessageUserList),'名:')
			for user in topMessageUserList:
				print(user[0],'(',user[1],')\t',end='')
			print()

	def userWelcomeMessageCounts(self,dataList):

		#filter
		validDataList = filter(self._isWelcomeMessage,dataList)

		userReducedCounter = self.mapReduceCountsByList(validDataList)

		topMessageUserList = userReducedCounter.most_common(3)

		if len(list(topMessageUserList)) == 0:
			print('群里没有人说欢迎')
		else:
			print('群里欢迎最积极的前',len(topMessageUserList),'名:')
			for user in topMessageUserList:
				print(user[0],'(',user[1],')\t',end='')
			print()



	def _isWelcomeMessage(self, record):
		if record.type == WechatMessageType.TEXT:
			if('welcome' in record.message.lower() or '欢迎' in record.message or '[Clap]' in record.message or '🎉' in record.message):
				return True
		return False

	def userHappyBirthdayMessageCounts(self,dataList):

		#filter
		validDataList = filter(self._isHappyBirthdayMessage,dataList)

		userReducedCounter = self.mapReduceCountsByList(validDataList)

		topMessageUserList = userReducedCounter.most_common(3)

		if len(list(topMessageUserList)) == 0:
			print('群里没有人说生日快乐')
		else:
			print('群里生日快乐最积极的前',len(topMessageUserList),'名:')
			for user in topMessageUserList:
				print(user[0],'(',user[1],')\t',end='')
			print()

	def _isHappyBirthdayMessage(self, record):
		if record.type == WechatMessageType.TEXT:
			if('happy birthday' in record.message.lower() or '生日快乐' in record.message or '[蛋糕]' in record.message or '[Cake]' in record.message or '🎂' in record.message):
				return True
		return False