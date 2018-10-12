'''
Created on Oct 11, 2018

@author: me
'''
import os

class File_reader_class:
    def __init__(self):
        None
        
    def file_printer(self, directory):
        file_out = []
        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file)):
                file_out.append(file)
        return file_out
    
    def file_recursive_printer(self, filename):
        file_out = []
        for root, dirs, files in os.walk(filename):  
            for directories in dirs:
                file_out.append(os.path.join(root, directories))
        return(file_out)
    
    def interesting_search(self, command, filelist):
        out_list = []
        if command is 'A':
            return filelist
        if len(command)>1:
            if command[0] is 'N':
                search_for = command[2:]
                for file in filelist:
                    if file == search_for:
                        out_list.append(file)
        return out_list

new_reader = File_reader_class()
for i in new_reader.file_printer("/home/me/ICS 32A/lab projects/proj_1/"):
    print(i)

directories_ordered = new_reader.file_recursive_printer("/home/me/ICS 32A/lab projects/proj_1/")
directories_ordered.sort()
for i in directories_ordered:
    print(i)
    
files_ordered = []
for i in directories_ordered:
    for j in new_reader.file_printer(i):
        print(j)
        files_ordered.append(j)

print(new_reader.interesting_search('A', files_ordered))
print(new_reader.interesting_search('N apple', files_ordered))



