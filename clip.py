#! /usr/bin/env python3
""" Usage: copies content of a file to clipbboard. $clip filename"""
import os, sys, pyperclip
if len(sys.argv) == 1:
	print('Usage clip file_name //to copy content of file to clipboard')
file_name = ' '.join(sys.argv[1:])
content = ''
with open(file_name) as f:
	for line in f.readlines():
		content+=line
print(content)
pyperclip.copy(content)
