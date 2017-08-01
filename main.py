#!/usr/bin/env python3

import sys

# main function to do anylsis of wechat chatting history
def loadWechatSQLLib(path):
	#TODO
	return

def main():
	args = sys.argv
	if len(args) != 1:
		print('Too many arguments!')
		exit(0);
	else:
		loadWechatSQLLib(args[0])
		print 'Done';

main()