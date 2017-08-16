
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