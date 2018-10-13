'''
Created on Oct 11, 2018

@author: Alex
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

print("all file names in surface level")
new_reader = File_reader_class()
for i in new_reader.file_printer("/home/me/ICS 32A/10_12 lab files"):
    print(i)
print()

print("all directory names, sorted")
directories_ordered = new_reader.file_recursive_printer("/home/me/ICS 32A/10_12 lab files")
directories_ordered.sort()
for i in directories_ordered:
    print(i)
print()

print("all file names, ordered")    
files_ordered = []
for i in directories_ordered:
    for j in new_reader.file_printer(i):
        print(j)
        files_ordered.append(j)
print()

print("intereting search, All")
print(new_reader.interesting_search('A', files_ordered))
print()

print("interesting search, Name")
print(new_reader.interesting_search('N C1_B3_A1_f', files_ordered))



