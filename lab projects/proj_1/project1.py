import re
import os

# Define file functions
def file_printer(directory : str) -> []:
    """Return the paths to files in a directory.

    Keyword arguments:
    directory -- the path of the directory to search
    """
    outfiles = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            outfiles.append(os.path.join(directory, file))
    return outfiles

def file_recursive_printer(directory : str) -> []:
    """Return the paths to files in a directory and all of its sub-directories.

    Keyword arguments:
    directory -- the path of the directory to search
    """
    outfiles = []
    for path in os.listdir(directory):
        path = os.path.join(directory, path)
        if os.path.isfile(path):
            outfiles.append(path)
        elif os.path.isdir(path):
            outfiles.extend(file_recursive_printer(path))
    return outfiles

def search_by_name(filename : str, files : [], slashtype : str) -> []:
    """Return the paths with a given filename from a given list of files.

    Keyword arguments:
    filename -- the filename to filter by
    files -- the list of files to filter
    slashtype -- the type of slash that is used to separate directories
    """
    outfiles = []
    for file in files:
        if file.endswith(slashtype + filename):
            outfiles.append(file)
    return outfiles

def search_by_extension(extension : str, files : []) -> []:
    """Return the paths with a given extension from a given list of files.

    Keyword arguments:
    extension -- the extension type to filter by
    files -- the list of files to filter
    """
    outfiles = []
    for file in files:
        if file.endswith("." + extension):
            outfiles.append(file)
    return outfiles

def search_by_text(text : str, files : []) -> []:
    """Return the paths to files containing the given text from a given list of files.

    Keyword arguments:
    text -- the text to search for
    files -- the list of files to filter
    """
    outfiles = []
    for file in files:
        try:
            infile = open(file, 'r')
            if text in infile.read():
                outfiles.append(file)
        except UnicodeDecodeError:
            continue
    return outfiles

def search_by_max_size(size : int, files : []) -> []:
    """Return the paths to files smaller than a given limit from a given list of files.

    Keyword arguments:
    size -- the maximum size to filter by
    files -- the list of files to filter
    """
    outfiles = []
    for file in files:
        if os.stat(file).st_size <= size:
            outfiles.append(file)
    return outfiles

def search_by_min_size(size : int, files : []) -> []:
    """Return the paths to files larger than a given limit from a given list of files.

    Keyword arguments:
    size -- the minimum size to filter by
    files -- the list of files to filter
    """
    outfile = []
    for file in files:
        if os.stat(file).st_size >= size:
            outfile.append(file)
    return outfile

def get_first_line(filepath : str) -> str:
    
    """Return the first line in a given file.

    Keyword arguments:
    filepath -- the path to the file to read from
    """
    infile = open(filepath, 'r')
    line = infile.readline()
    infile.close()
    return line

def duplicate_file(filepath : str):
    """Duplicate a given file.

    Keyword arguments:
    filepath -- the path to the file to duplicate
    """
    infile = open(filepath, 'r')
    lines = infile.read()
    outfile = open(filepath + ".dup", 'w+')
    outfile.write(lines)
    infile.close()
    outfile.close()
    
def touch_file(filepath : str):
    """Set a file's last modified date to the current time.

    Keyword arguments:
    filepath -- the path to the file to touch
    """
    infile = open(filepath, 'r')
    infile.read()
    outfile = open(filepath, 'w')
    outfile.write("")
    infile.close()
    outfile.close()

# Define utility functions
def get_formatted_input(pattern : str) -> str:
    """Continuously read input until it matches a given format, and return the input's function and argument as a tuple.

    Keyword arguments:
    pattern -- the regex pattern the input must match
    """
    line = ""
    while( not re.match(pattern, line) ):
        line = input()
        if re.match(pattern, line):
            argument = "" if line.__len__() < 3 else line[2:]
            return (line[0], argument)
        print("ERROR")

def persist(funct, ex : Exception, error : str):
    """Repeat a given function until a given Exception stops occurring, and print an error each time it does.

    Keyword arguments:
    funct -- the function to execute
    ex -- the exception to catch and print an error for
    error -- the error message to print
    """
    while(True):
        try:
            return funct()
        except ex:
            print(error)

def lexicographical_sort(directory : str, inputfiles : [], slashtype : str) -> []:
    """Return a list of files sorted lexicographically, with files in the base directory in the beginning.

    Keyword arguments:
    directory -- the base directory
    inputfiles -- the files to sort
    slashtype -- the type of slash that is used to separate directories
    """
    outputfiles = []
    directfiles = []
    subfiles = []
    for file in inputfiles:
        if slashtype in file[directory.__len__()+1:]:
            subfiles.append(file)
        else:
            directfiles.append(file)
    outputfiles.extend(sorted(directfiles))
    outputfiles.extend(sorted(subfiles))
    return outputfiles

# Define organizational functions

def get_files() -> []:
    """Read input until correctly formatted, then return the files requested by the input"""
    function, argument = get_formatted_input("^[DR] .+")
    return argument, file_printer(argument) if function == ("D") else file_recursive_printer(argument)

def select(function : str, argument : str, sortedfiles : []) -> []:
    """Return a list of files sorted by a given command.

    Keyword arguments:
    function -- the indicator for an aspect to filter by
    argument -- the optional argument to filter against
    sortedfiles -- the files to filter through
    """
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
    """Perform a specified operation on a given list of files.

    Keyword arguments:
    function -- the indicator for the operation to execute
    sortedfiles -- the files to operate on
    """
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
    # Determine which type of slashes are used in this directory system
    slashtype = os.path.join(os.getcwd(),"")[-1]
    
    # Continuously attempt to retrieve files until the user input is valid.
    directory, files = persist(get_files, FileNotFoundError, "ERROR")
    
    # Display the files in lexicographical order
    sortedfiles = lexicographical_sort(directory, files, slashtype)
    for file in sortedfiles:
        print(file)

    # Continuously read input until valid, then filter files based on user criteria
    function, argument = get_formatted_input("^A$|^[NET] .+|^[<>] \d+$")
    interestingfiles = select(function, argument, sortedfiles)
    
    # Display the files in lexicographical order
    sortedfiles = lexicographical_sort(directory, interestingfiles, slashtype)
    for file in sortedfiles:
        print(file)
    
    # Continuously read input until valid, then operate on files based on user criteria
    function, argument = get_formatted_input("^[FDT]$")
    operate(function, sortedfiles)