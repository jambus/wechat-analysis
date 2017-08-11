from enum import Enum

class WechatMessageType(Enum):
	TEXT = 1
	SYSTEM_MESSAGE = 10000
	VOICE = 34
	EMOTION = 47
	VIDEO = 62
	CALL = 50
	PICTURE = 3
	POSITION = 48
	CARD = 42
	LINK = 49

	UNHANDLED = -999