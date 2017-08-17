import xml.etree.ElementTree as ET
#import xml.etree.ElementTree.ParseError as ParseError

class WechatUtils(object):

	@staticmethod
	def handleContactRemarkUnexpectedChars(aliasName):
		#if(not hasattr(self,'_aliasPattern')):
		#	self._aliasPattern = re.compile(r'^\n.(.+?)(\x12.*|[^\x12]*)$')
		#result = self._aliasPattern.match(aliasName)

		#if result == None:
		#	return aliasName
		#else:
		#	return result.group(1)
		start = 2
		end = aliasName.find('\x12', start)
		return aliasName[start:end]

	@staticmethod
	def handleXMLContentFromMessage(content):

		rootNode = None
		if len(content) < 5:
			print ('It is not valid xml content:' + str(content))
			return rootNode
		else:
			if content[0:5] != '<msg>':
				content = '\n'.join(content.split('\n',2)[1:])

			try:	
				rootNode = ET.fromstring(content)
			except ET.ParseError as args:
				#print ('It is not valid xml content (' , args,'):\n',content)
				rootNode = None
			
			return rootNode