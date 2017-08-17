from collections import Counter
from functools import reduce

from classes.wechatAnalysisInterface import WechatAnalysisInterface
from classes.wechatMessageType import WechatMessageType

class WechatCommonAnalysiser(WechatAnalysisInterface):

	def __init__(self):
		pass
	
	def execute(self,dataList):
		raise NotImplementedError("Should implement this")

	def getWechatUserMessageTypeList(self):
		if(not hasattr(self,'_userMessageTypeList')):
			self._userMessageTypeList = [WechatMessageType.TEXT,WechatMessageType.VOICE,WechatMessageType.VIDEO1,WechatMessageType.EMOTION,WechatMessageType.VIDEO2,WechatMessageType.CALL,WechatMessageType.PICTURE,WechatMessageType.POSITION,WechatMessageType.CARD,WechatMessageType.LINK]
		return self._userMessageTypeList

	def getWechatVideoMessageTypeList(self):
		if(not hasattr(self,'_videoMessageTypeList')):
			self._videoMessageTypeList = [WechatMessageType.VIDEO1,WechatMessageType.VIDEO2]
		return self._videoMessageTypeList

	def mapReduceCountsByList(self, list):
		#map
		userMapFun = lambda x:{x.sender:1}
		userMappedList = map(userMapFun, list) 

		#reduce
		userReduceSum = lambda x,y:Counter(x) + Counter(y)
		userReducedCounter = reduce(userReduceSum, userMappedList,Counter({})) 

		return userReducedCounter
