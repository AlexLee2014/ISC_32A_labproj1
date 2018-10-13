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
    
    def file_recursive_printer(self, directory):
        file_out = []
        for root, dirs, files in os.walk(directory):  
            for directories in dirs:
                file_out.append(os.path.join(root, directories))
        return(file_out)
    
    def search_by_name(self, filename : str) -> []:
        return []
    
    def search_by_extension(self, extension : str) -> []:
        return []
    
    def search_by_text(self, text : str) -> []:
        return[]
    
    def search_by_max_size(self, size : int) -> []:
        return[]
    
    def search_by_min_size(self, size : int) -> []:
        return []
    
    """
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
    """

    '''
    If this line of input contains the letter F by itself, 
    print the first line of text from the file if it's a text file; print NOT TEXT if it is not.
    '''
    def get_first_line(self, file):
        infile = open(file, 'r')
        return infile.readline()
    
    '''
    If this line of input contains the letter D by itself, 
    make a duplicate copy of the file and store it in the same directory where the original resides,
    but the copy should have .dup(short for "duplicate") appended to its filename.
    For example, if the interesting file is C:\pictures\boo.jpg,
    you would copy it to C:\pictures\boo.jpg.dup.
    '''
    def duplicate_file(self, filename : str):
        outfile = open(filename, 'w')
    
    '''
    If the third line of the input contains the letter T by itself,
    "touch" the file, which means to modify its last modified timestamp to be the current date/time.
    '''
    
    def touch_file(selfs, file : str):
        # touch file
        return

    

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



