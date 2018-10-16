'''
Created on Oct 11, 2018

@author: Alex
'''
import os
import re

class File_reader_class:
    def __init__(self):
        None
        
    def file_printer(self, directory : str) -> []:
        outfiles = []
        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file)):
                outfiles.append(os.path.join(directory, file))
        return outfiles
    
    def file_recursive_printer(self, directory : str) -> []:
        outfiles = []
        for path in os.listdir(directory):
            path = os.path.join(directory, path)
            if os.path.isfile(path):
                outfiles.append(path)
            elif os.path.isdir(path):
                outfiles.extend(self.file_recursive_printer(path))
        return outfiles

    def search_by_name(self, filename : str, files : []) -> []:
        outfiles = []
        for file in files:
            if file.endswith("\\" + filename):
                outfiles.append(file)
        return outfiles
    
    def search_by_extension(self, extension : str, files : []) -> []:
        outfiles = []
        for file in files:
            if file.endswith("." + extension):
                outfiles.append(file)
        return outfiles
    
    def search_by_text(self, text : str, files : []) -> []:
        outfiles = []
        for file in files:
            infile = open(file, 'r')
            if text in infile.read():
                outfiles.append(file)
        return outfiles
    
    def search_by_max_size(self, size : int, files : []) -> []:
        outfiles = []
        for file in files:
            if os.stat(file).st_size < size:
                outfiles.append(file)
        return outfiles
    
    def search_by_min_size(self, size : int, files : []) -> []:
        outfile = []
        for file in files:
            if os.stat(file).st_size > size:
                outfile.append(file)
        return outfile
    
    def get_first_line(self, filepath : str) -> str:
        infile = open(filepath, 'r')
        line = infile.readline()
        close(infile)
        return line
    
    def duplicate_file(self, filepath : str):
        infile = open(filepath, 'r')
        lines = infile.read()
        outfile = open(filepath + ".dup", 'w+')
        outfile.write(lines)
        close(infile)
        close(outfile)
        
    def touch_file(self, filepath : str):
        infile = open(filepath, 'r')
        infile.read()
        outfile = open(filepath, 'w')
        outfile.write("")
        close(infile)
        close(outfile)