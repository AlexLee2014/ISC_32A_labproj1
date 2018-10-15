'''
Created on Oct 14, 2018

@author: me
'''
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