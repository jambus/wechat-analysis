from classes.wechatAnalysisInterface import WechatAnalysisInterface
from classes.analysiscomponents.wechatCommonAnalysiser import WechatCommonAnalysiser
from classes.wechatMessageType import WechatMessageType

class WechatAnalysisCounter(WechatCommonAnalysiser):
	
	def execute(self,dataList):
		self.userMessageCounts(dataList)
		self.userWelcomeMessageCounts(dataList)
		self.userHappyBirthdayMessageCounts(dataList)
		self.userBossMessageCounts(dataList)
		pass

	def userMessageCounts(self,dataList):

		#filter
		userMessageFilter = lambda x: x.type in self.getWechatUserMessageTypeList()
		validDataList = filter(userMessageFilter,dataList)

		userReducedCounter = self.mapReduceCountsByList(validDataList)

		topMessageUserList = userReducedCounter.most_common(3)

		self.printCountResultList(topMessageUserList,'说话')

	def userWelcomeMessageCounts(self,dataList):

		#filter
		validDataList = filter(self._isWelcomeMessage,dataList)

		userReducedCounter = self.mapReduceCountsByList(validDataList)

		topMessageUserList = userReducedCounter.most_common(3)

		self.printCountResultList(topMessageUserList,'说欢迎')

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

		self.printCountResultList(topMessageUserList,'说生日快乐')

	def _isHappyBirthdayMessage(self, record):
		if record.type == WechatMessageType.TEXT:
			if('happy birthday' in record.message.lower() or '生日快乐' in record.message or '[蛋糕]' in record.message or '[Cake]' in record.message or '🎂' in record.message):
				return True
		return False

	def userBossMessageCounts(self,dataList):

		#filter
		validDataList = filter(self._isThankBossMessage,dataList)

		userReducedCounter = self.mapReduceCountsByList(validDataList)

		topMessageUserList = userReducedCounter.most_common(3)

		self.printCountResultList(topMessageUserList,'感谢老板')

	def _isThankBossMessage(self, record):
		if record.type == WechatMessageType.TEXT:
			if('boss' in record.message.lower() or '老板' in record.message):
				return True
		return False