import re
from file_reader_class import File_reader_class

# Define functions

def get_correct_input(pattern : str) -> str:
    line = ""
    while( not re.match(pattern, line) ):
        line = input()
        if re.match(pattern, line):
            argument = "" if line.__len__() < 3 else line[2:]
            return line[0], argument
        print("ERROR")

def persist(funct, ex : Exception, error : str):
    while(True):
        try:
            return funct()
        except ex:
            print(error)

def lexicographical_sort(directory : str, inputfiles : []) -> []:
    outputfiles = []
    directfiles = []
    subfiles = []
    for file in inputfiles:
        if "\\" in file[directory.__len__()+1:]:
            subfiles.append(file)
        else:
            directfiles.append(file)
    outputfiles.extend(sorted(directfiles, key=lambda str:str.lower()))
    outputfiles.extend(sorted(subfiles, key=lambda str:str.lower()))
    return outputfiles

# Run program
filereader = File_reader_class()

def get_files() -> []:
    function, argument = get_correct_input("^[DR] .+")
    return argument, filereader.file_printer(argument) if function == ("D") else filereader.file_recursive_printer(argument)

directory, files = persist(get_files, FileNotFoundError, "ERROR")
sortedfiles = lexicographical_sort(directory, files)
for file in sortedfiles:
    print(file)

interestingfiles = []
function, argument = get_correct_input("^A$|^[NET] .+|^[<>] \d+$")
if function == "A":
    interestingfiles = sortedfiles
elif function == "N":
    interestingfiles = filereader.search_by_name(argument)
elif function == "E":
    interestingfiles = filereader.search_by_extension(argument)
elif function == "T":
    interestingfiles = filereader.search_by_text(argument)
elif function == "<":
    interestingfiles = filereader.search_by_max_size(int(argument))
elif function == ">":
    interestingfiles = filereader.search_by_min_size(int(argument))

sortedfiles = lexicographical_sort(directory, interestingfiles)
for file in sortedfiles:
    print(file)

function, argument = get_correct_input("^[FDT]$")

if function == "F":
    for file in sortedfiles:
        print(filereader.get_first_line(file))
elif function == "D":
    for file in sortedfiles:
        filereader.duplicate_file(file)
elif function == "T":
    for file in sortedfiles:
        filereader.touch_file(file)