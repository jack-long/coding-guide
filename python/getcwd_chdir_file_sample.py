#!/usr/bin/env python
'''A demo for os.getcwd, os.chdir && file write.

The user can set a path and save something to a file.
'''
import os

print "Current directory:", os.getcwd()

message = '''Enter the path, examples:
------------
Current folder: .
Relative path: ../parentfolder/
Absolute path: D://Document/
------------
'''
path = raw_input(message)
os.chdir(path)

print "Current directory:", os.getcwd()

file_name = raw_input("Your file name: ")

with open(file_name, 'w') as f:
    print "File content:"
    while(True):
        content = raw_input("")
        if content != '':
            f.write(content)
        else:
            break
    
print "File saved!"
print "Bye!"
raw_input("Press 'Enter' to exist")