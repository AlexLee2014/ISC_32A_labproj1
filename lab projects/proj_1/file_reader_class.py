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
        
    def file_printer(self, directory : str) -> []:
        file_out = []
        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file)):
                file_out.append(file)
        return file_out
    
    def file_recursive_printer(self, directory : str) -> []:
        file_out = []
        for root, dirs, files in os.walk(directory):  
            for directories in dirs:
                file_out.append(os.path.join(root, directories))
        return(file_out)
    
    def search_by_name(self, filename : str, files : []) -> []:
        outfiles = []
        for file in files:
            if file is filename:
                outfiles.append(file)
        return outfiles
    
    def search_by_extension(self, extension : str, files : []) -> []:
        outfile = []
        for file in files:
            space_index = file.find(" ")
            if file[space_index:] is extension:
                outfile.append(file)
    
    def search_by_text(self, text : str, files : []) -> []:
        outfile = []
        for file in files:
            infile = open(file, 'r')
            if text in infile.read():
                outfile.append(file)
        return outfile
    
    def search_by_max_size(self, size : int, files : []) -> []:
        outfile = []
        for file in files:
            statinfo = os.stat(file)
            if statinfo.st_size < size:
                outfile.append(file)
        return outfile
    
    def search_by_min_size(self, size : int, files : []) -> []:
        outfile = []
        for file in files:
            statinfo = os.stat(file)
            if statinfo.st_size > size:
                outfile.append(file)
        return outfile
    
    def get_first_line(self, filepath : str):
        infile = open(filepath, 'r')
        return infile.readline()
    
    def duplicate_file(self, filepath : str):
        infile = open(filepath, 'r')
        lines = infile.read()
        outfile = open(filepath + ".dup", 'w+')
        outfile.write(lines)
        
    def touch_file(self, filepath : str):
        infile = open(filepath, 'r')
        infile.read()
        outfile = open(filepath, 'w')
        outfile.write("")