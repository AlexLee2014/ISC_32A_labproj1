import re

command = ""
while( not re.match("^[DR] .+", command) ):
    command = input()
    if re.match("^[DR] .+", command):
        break
    print("ERROR")
'''
filereader = File_reader_class()
'''