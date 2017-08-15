#!/usr/bin/env python3

import sys

import argparse

from classes.wechatSqliteUtil import WechatSqliteUtil
from classes.wechatMessageAnalysis import WechatMessageAnalysis
from classes.wechatAnalysisCounter import WechatAnalysisCounter

def parseArgs(sysArgs):
	print('Input Paramters: ' + '\t'.join(sysArgs))

	parser = argparse.ArgumentParser()
	parser.add_argument('program', help='Program name', nargs='?')
	parser.add_argument('group', help='Specific wechat group to anaylsis', nargs='?', default= None)
	parser.add_argument('-o', '--output',dest='output', help='Setup the output file path',nargs='?', default= None)
	parser.add_argument('-m', '--mm',dest='mm', help='Specific wechat main sqlite lib', nargs='?', default= './data/MM.sqlite')
	parser.add_argument('-c', '--contact',dest='contact', help='Specific wechat contact sqlite lib', nargs='?', default= './data/WCDB_Contact.sqlite')
	
	return parser.parse_args(sysArgs)

def setupOutputToFile(filePath):
	if(filePath == None):
		return None
	else:
		outputFile = open(filePath, 'w')
		sys.stdout = outputFile
		return outputFile

def closeOutput(outputFile):
	if(outputFile != None):
		outputFile.close()
	return

#Sample run command:
#python3 main.py "Bb SHA"
def main():
	args = parseArgs(sys.argv)

	targetRoomName = args.group
	if(targetRoomName == None):
		print('Missing argument wechat room name')
		exit(0)

	wechatSqliteUtil = WechatSqliteUtil(args.mm,args.contact)

	outputFile = setupOutputToFile(args.output)

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
	wechatMessageAnalysis.printChatHistoryData(wechatMessageList)

	wechatMessageAnalysis.registerAnalysiser(WechatAnalysisCounter())
	wechatMessageAnalysis.executeAnalysis(wechatMessageList)

	wechatSqliteUtil.closeWechatDB()
	print('Done')

	closeOutput(outputFile)

main()