import re
import os

# Define file functions
def file_printer(directory : str) -> []:
    outfiles = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            outfiles.append(os.path.join(directory, file))
    return outfiles

def file_recursive_printer(directory : str) -> []:
    outfiles = []
    for path in os.listdir(directory):
        path = os.path.join(directory, path)
        if os.path.isfile(path):
            outfiles.append(path)
        elif os.path.isdir(path):
            outfiles.extend(file_recursive_printer(path))
    return outfiles

def search_by_name(filename : str, files : [], slashtype : str) -> []:
    outfiles = []
    for file in files:
        if file.endswith(slashtype + filename):
            outfiles.append(file)
    return outfiles

def search_by_extension(extension : str, files : []) -> []:
    outfiles = []
    for file in files:
        if file.endswith("." + extension):
            outfiles.append(file)
    return outfiles

def search_by_text(text : str, files : []) -> []:
    outfiles = []
    for file in files:
        infile = open(file, 'r')
        if text in infile.read():
            outfiles.append(file)
    return outfiles

def search_by_max_size(size : int, files : []) -> []:
    outfiles = []
    for file in files:
        if os.stat(file).st_size < size:
            outfiles.append(file)
    return outfiles

def search_by_min_size(size : int, files : []) -> []:
    outfile = []
    for file in files:
        if os.stat(file).st_size > size:
            outfile.append(file)
    return outfile

def get_first_line(filepath : str) -> str:
    infile = open(filepath, 'r')
    line = infile.readline()
    infile.close()
    return line

def duplicate_file(filepath : str):
    infile = open(filepath, 'r')
    lines = infile.read()
    outfile = open(filepath + ".dup", 'w+')
    outfile.write(lines)
    infile.close()
    outfile.close()
    
def touch_file(filepath : str):
    infile = open(filepath, 'r')
    infile.read()
    outfile = open(filepath, 'w')
    outfile.write("")
    infile.close()
    outfile.close()

# Define utility functions
def get_correct_input(pattern : str) -> str:
    line = ""
    while( not re.match(pattern, line) ):
        line = input()
        if re.match(pattern, line):
            argument = "" if line.__len__() < 3 else line[2:]
            return (line[0], argument)
        print("ERROR")

def persist(funct, ex : Exception, error : str):
    while(True):
        try:
            return funct()
        except ex:
            print(error)

def lexicographical_sort(directory : str, inputfiles : [], slashtype : str) -> []:
    outputfiles = []
    directfiles = []
    subfiles = []
    for file in inputfiles:
        if slashtype in file[directory.__len__()+1:]:
            subfiles.append(file)
        else:
            directfiles.append(file)
    outputfiles.extend(sorted(directfiles, key=lambda str:str.lower()))
    outputfiles.extend(sorted(subfiles, key=lambda str:str.lower()))
    return outputfiles

# Define organizational functions

def get_files() -> []:
    function, argument = get_correct_input("^[DR] .+")
    return argument, file_printer(argument) if function == ("D") else file_recursive_printer(argument)

def select(function : str, sortedfiles : []) -> []:
    interestingfiles = []
    if function == "A":
        interestingfiles = sortedfiles
    elif function == "N":
        interestingfiles = search_by_name(argument, sortedfiles, slashtype)
    elif function == "E":
        interestingfiles = search_by_extension(argument, sortedfiles)
    elif function == "T":
        interestingfiles = search_by_text(argument, sortedfiles)
    elif function == "<":
        interestingfiles = search_by_max_size(int(argument), sortedfiles)
    elif function == ">":
        interestingfiles = search_by_min_size(int(argument), sortedfiles)
    return interestingfiles

def operate(function : str, sortedfiles : []):
    if function == "F":
        for file in sortedfiles:
            try:
                line = get_first_line(file)
                if line.endswith("\n"):
                    print(line[:-1])
                else:
                    print(line)
            except:
                print("NOT TEXT")
    elif function == "D":
        for file in sortedfiles:
            duplicate_file(file)
    elif function == "T":
        for file in sortedfiles:
            touch_file(file)

# Run program
if __name__ == '__main__':
    slashtype = os.path.join(os.getcwd(),"")[-1]
    
    directory, files = persist(get_files, FileNotFoundError, "ERROR")
    sortedfiles = lexicographical_sort(directory, files, slashtype)
    for file in sortedfiles:
        print(file)

    function, argument = get_correct_input("^A$|^[NET] .+|^[<>] \d+$")
    interestingfiles = select(function, sortedfiles)
    sortedfiles = lexicographical_sort(directory, interestingfiles, slashtype)
    for file in sortedfiles:
        print(file)
    
    function, argument = get_correct_input("^[FDT]$")
    operate(function, sortedfiles)