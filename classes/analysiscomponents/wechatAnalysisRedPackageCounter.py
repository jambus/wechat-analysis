import xml.etree.ElementTree as ET

from classes.wechatMessageType import WechatMessageType
from classes.analysiscomponents.wechatCommonAnalysiser import WechatCommonAnalysiser
from classes.wechatUtils import WechatUtils

class WechatAnalysisRedPackageCounter(WechatCommonAnalysiser):

	def execute(self,dataList):

		#filter
		validDataList = filter(self._isRedPackageMessage,dataList)
		
		userReducedCounter = self.mapReduceCountsByList(validDataList)

		topMessageUserList = userReducedCounter.most_common(3)

		self.printCountResultList(topMessageUserList,'发红包')

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