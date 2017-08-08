#!/usr/bin/env python3

import sys

from classes.wechatSqliteUtil import WechatSqliteUtil

def main():
	args = sys.argv
	print (args)
	argslength = len(args)

	if argslength == 1:
		wechatSqliteUtil = WechatSqliteUtil(None,None)
	elif argslength == 2:
		wechatSqliteUtil = WechatSqliteUtil(args[1],None)
	elif argslength == 3:
		wechatSqliteUtil = WechatSqliteUtil(args[1],args[2])
	else:
		print('Too many arguments!')
		exit(0)
	wechatSqliteUtil.loadWechatDB()
	wechatSqliteUtil.findChatRoomTableByRoomName('Bb SHA')
	wechatSqliteUtil.closeWechatDB()
	print('Done')

main()