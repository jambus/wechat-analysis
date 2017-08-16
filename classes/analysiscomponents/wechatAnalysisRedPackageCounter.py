import xml.etree.ElementTree as ET

from functools import reduce
from collections import Counter

from classes.wechatMessageType import WechatMessageType
from classes.analysiscomponents.wechatCommonAnalysiser import WechatCommonAnalysiser
from classes.wechatUtils import WechatUtils

class WechatAnalysisRedPackageCounter(WechatCommonAnalysiser):

	def execute(self,dataList):

		#filter
		validDataList = filter(self._isRedPackageMessage,dataList)

		#map
		userMapFun = lambda x:{x.sender:1}
		userMappedList = map(userMapFun, validDataList) 

		#reduce
		userReduceSum = lambda x,y:Counter(x) + Counter(y)
		userReducedCounter = reduce(userReduceSum, userMappedList) 

		topMessageUserList = userReducedCounter.most_common(3)
		print('群里红包数量发的最多的',len(topMessageUserList),'名:')
		for user in topMessageUserList:
			print(user[0],'(',user[1],')\t',end='')
		print()

		pass

	def _isRedPackageMessage(self, record):
		if record.type != WechatMessageType.LINK:
			return False
		else:
			root = WechatUtils.handleXMLContentFromMessage(record.message)
			if(root != None):
				typeNode = root.find('./appmsg/type')
				if typeNode != None and typeNode.text == '2001':
					return True
			return False