#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#kawan kelam copyright ga isin buncid

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("bd.txt","r");
	link = raw_input(" www.example.com ): ")
	print "\n\nUrl  : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "wrong => ",req_link

def Credit():
	Space(9); print "\033[1;32;40m
╭╮╱╭┳━━━╮╱╱╱╱╭━━━╮╭╮╱╭━━━╮╱╱╱╭╮╱╱╭┳━━━╮
┃┃╱┃┃╭━╮┃╱╱╱╱┃╭━╮┣╯╰╮┃╭━╮┃╱╱╭╯┃╱╱┃┃╭━╮┃
┃╰━╯┃┃┃┃┣━┳━╮╰╯╭╯┣╮╭╯┃╰━━┳━━╋╮┃╭━╯┣╯╭╯┣━┳━━╮
┃╭━╮┃┃┃┃┃╭┫╭╮┳╮╰╮┃┃┃╱╰━━╮┃╭╮┃┃┃┃╭╮┣╮╰╮┃╭┫━━┫
┃┃╱┃┃╰━╯┃┃┃┃┃┃╰━╯┃┃╰╮┃╰━╯┃╰╯┣╯╰┫╰╯┃╰━╯┃┃┣━━┃
╰╯╱╰┻━━━┻╯╰╯╰┻━━━╯╰━╯╰━━━┫╭━┻━━┻━━┻━━━┻╯╰━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯"
	
Credit()
findAdmin()
