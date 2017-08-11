from classes.wechatMessageType import WechatMessageType

class WechatMessage(object):

	def __init__(self):
		self._createTime = None
		self._sender = None
		self._message = None
		self._status = None
		self._type = WechatMessageType.UNHANDLED
		self._isMyMessage = False
		pass

	@property
	def createTime(self):
		return self._createTime

	@createTime.setter
	def createTime(self, value):
		self._createTime = value

	@property
	def sender(self):
		return self._sender

	@sender.setter
	def sender(self, value):
		self._sender = value

	@property
	def message(self):
		return self._message

	@message.setter
	def message(self, value):
		self._message = value

	@property
	def status(self):
		return self._status

	@status.setter
	def status(self, value):
		self._status = value

	@property
	def type(self):
		return self._type

	@type.setter
	def type(self, value):
		self._type = value

	@property
	def isMyMessage(self):
		return self._isMyMessage

	@isMyMessage.setter
	def isMyMessage(self, value):
		self._isMyMessage = value

