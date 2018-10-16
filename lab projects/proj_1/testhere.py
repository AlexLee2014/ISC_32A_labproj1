'''
Created on Oct 14, 2018

@author: me
'''
import os
outfile = open("/home/me/Documents/testhere", 'w')
outfile.write("hello")
outfile.write("more stuff")

outfile = []
files = ["bob py", "joepy", "alan pyy", "alex p", "dan id", "newton py"]
for file in files:
    space_index = file.find(" ")
    if file[space_index+1:] == "py":
        outfile.append(file)
print(outfile)
files = ["/home/me/Documents/1", "/home/me/Documents/2","/home/me/Documents/3"]
outfile = []
for file in files:
    statinfo = os.stat(file)
    if statinfo.st_size < 6:
        outfile.append(file)
print(outfile)
outfile = []
text = "hi t"
for file in files:
    infile = open(file, 'r')
    if text in infile.read():
        outfile.append(file)
print(outfile)




