'''
Created on Oct 11, 2018

@author: Alex
'''
import os

class File_reader_class:
    def __init__(self):
        None
        
    def file_printer(self, directory : str) -> []:
        file_out = []
        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file)):
                file_out.append(os.path.join(directory, file))
        return file_out
    
    def file_recursive_printer(self, directory : str) -> []:
        file_out = []
        for path in os.listdir(directory):
            path = os.path.join(directory, path)
            if os.path.isfile(path):
                file_out.append(path)
            elif os.path.isdir(path):
                file_out.extend(self.file_recursive_printer(path))
        return file_out

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