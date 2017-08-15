from functools import reduce
from collections import Counter

from classes.wechatAnalysisInterface import WechatAnalysisInterface
from classes.analysiscomponents.wechatCommonAnalysiser import WechatCommonAnalysiser
from classes.wechatMessageType import WechatMessageType

class WechatAnalysisCounter(WechatCommonAnalysiser):
	
	def execute(self,dataList):
		self.userMessageCounts(dataList)
		pass

	def userMessageCounts(self,dataList):

		#filter
		userMessageFilter = lambda x: x.type in self.getWechatUserMessageTypeList()
		validDataList = filter(userMessageFilter,dataList)

		#map
		userMapFun = lambda x:{x.sender:1}
		userMappedList = map(userMapFun, validDataList) 

		#reduce
		userReduceSum = lambda x,y:Counter(x) + Counter(y)
		userReducedDict = reduce(userReduceSum, userMappedList) 

		print(userReducedDict)
		pass