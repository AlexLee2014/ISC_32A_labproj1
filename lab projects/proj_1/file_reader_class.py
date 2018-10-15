'''
Created on Oct 11, 2018

@author: Alex
'''
import os
import time
from gi.types import nothing

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
    
    def search_by_name(self, filename : str, files) -> []:
        outfiles = []
        for file in files:
            if file is filename:
                outfiles.append(file)
        return outfiles
    
    def search_by_extension(self, extension : str, files) -> []:
        outfile = []
        for file in files:
            space_index = file.find(" ")
            if file[space_index:] is extension:
                outfile.append(file)
    
    def search_by_text(self, text : str, files) -> []:
        outfile = []
        for file in files:
            infile = open(file, 'r')
            if text in infile.read():
                outfile.append(file)
        return outfile
    
    def search_by_max_size(self, size : int, files) -> []:
        outfile = []
        for file in files:
            statinfo = os.stat(file)
            if statinfo.st_size < size:
                outfile.append(file)
        return outfile
    
    def search_by_min_size(self, size : int, files) -> []:
        outfile = []
        for file in files:
            statinfo = os.stat(file)
            if statinfo.st_size > size:
                outfile.append(file)
        return outfile
    
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
    If this line of input is the letter A alone on a line,
    all of the files found in the previous step are considered interesting.
    
    def return_all_files(self, files):
        return files
    
    
    If this line of input begins with the letter N,
    the search will be for files whose names exactly match a particular name.
    The N will be followed by a space;
    after the space, the rest of the line will indicate the name of the files to be searched for.
    Note that filenames include extensions, so a search for boo would not find a file named boo.doc.
    
    
    def return_file_by_name(self, files, name):
        outfiles = []
        for i in files:
            if i is name:
                outfiles.append(i)
        return outfiles
    
    
    If this line of input begins with the letter E,
    the search will be for files whose names have a particular extension.
    The E will be followed by a space; after the space,
    the rest of the line will indicate the desired extension.
    For example, if the desired extension is py,
    all files whose names end in .py will be considered interesting.
    
    The desired extension may be specified with or without a dot preceding it
    (e.g., E .py or E py would mean the same thing in the input),
    and your search should behave the same either way.
    
    Note, also, that there is a difference between what you might call a name ending and an extension.
    In our program, if the search is looking for files with the extension oc,
    a file named iliveinthe.oc would be found, but a file named invoice.doc would not.
    
    def return_file_by_extension(self, files, extension):
        outfile = []
        for file in files:
            space_index = file.find(" ")
            if file[space_index:] is extension:
                outfile.append(file)
    
    
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
    
    def duplicate_file(self, filename):
        infile = open(filename, 'r')
        lines = infile.read()
        outfile = open(filename + ".dup", 'w+')
        outfile.write(lines)
        
        
    '''
    If the third line of the input contains the letter T by itself,
    "touch" the file, which means to modify its last modified timestamp to be the current date/time.
    '''
    def touch_file(self, file):
        infile = open(file, 'r')
        infile.read()
        outfile = open(file, 'w')
        outfile.write("")
        
    '''
    def touch_file(selfs, file : str):
        # touch file
        return
    '''


    
'''
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
'''
    
print("")
print("")
new_reader = File_reader_class()
#new_reader.duplicate_file("/home/me/Documents/test")
new_reader.touch_file("/home/me/Documents/testhere")

