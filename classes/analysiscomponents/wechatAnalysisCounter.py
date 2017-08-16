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
		userReducedCounter = reduce(userReduceSum, userMappedList) 

		topMessageUserList = userReducedCounter.most_common(3)
		print('群里话最多的前',len(topMessageUserList),'名:')
		for user in topMessageUserList:
			print(user[0],'(',user[1],')\t',end='')
		print()

		pass