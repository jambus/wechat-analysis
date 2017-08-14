#!/usr/bin/env python3

import sys

from classes.wechatSqliteUtil import WechatSqliteUtil
from classes.wechatMessageAnalysis import WechatMessageAnalysis

from classes.wechatAnalysisCounter import WechatAnalysisCounter

#Sample run command:
#python3 main.py "Bb SHA"
def main():
	args = sys.argv
	print('Paramters:')
	print(args)
	argslength = len(args)

	if argslength < 2:
		print('Missing arguments!')
		exit(0)
	elif argslength == 2:
		wechatSqliteUtil = WechatSqliteUtil(None,None)
	elif argslength == 3:
		wechatSqliteUtil = WechatSqliteUtil(args[2],None)
	elif argslength == 4:
		wechatSqliteUtil = WechatSqliteUtil(args[2],args[3])
	else:
		print('Too many arguments!')
		exit(0)

	targetRoomName = args[1]

	wechatSqliteUtil.loadWechatDB()
	roomId = wechatSqliteUtil.findChatRoomIdByRoomName(targetRoomName)
	if(roomId == None):
		return None

	targetChatTable =  wechatSqliteUtil.findChatRoomTableByRoomId(roomId)
	if(targetChatTable == None):
		return None
	chatHistory = wechatSqliteUtil.getChatHistoryByChatRoomTable(targetChatTable)

	wechatMessageAnalysis =  WechatMessageAnalysis()
	wechatMessageList = wechatMessageAnalysis.handleChatHistoryData(chatHistory)
	#wechatMessageAnalysis.printChatHistoryData(wechatMessageList)

	wechatMessageAnalysis.registerAnalysiser(WechatAnalysisCounter())
	wechatMessageAnalysis.executeAnalysis(wechatMessageList)

	wechatSqliteUtil.closeWechatDB()
	print('Done')

main()