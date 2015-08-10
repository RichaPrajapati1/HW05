#!/usr/bin/env python
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the 
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports
import os

# Body
def read_file():
	try:
		fout = open('words.txt','r')
	except:
		print ("File does not exist")
	else:
		for line in fout:
			if len(line) > 20:
				print line
		fout.close()


##############################################################################
def main():
    read_file()

if __name__ == '__main__':
    main()
