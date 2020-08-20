#########################################################################################################
###                         DEFANGER. Defangs URLs and IP addresses.                                  ###             
#########################################################################################################

# import packages
import argparse
import os
from defang import defang

# Initialize parser and arguments
parser = argparse.ArgumentParser(description="defanger parse")
parser.add_argument("-i", "--input", help = "Designate Input File", required=True)
parser.add_argument("-o", "--output", help = "Designate Output File", required=False)
args = parser.parse_args()

# Name Input / Output variables for ease of use
arg_in = args.input
arg_ou = args.output

# error checking, ignore
# print('inputfile: ', arg_in)
# print('outputfile: ', arg_ou)

# function checks if filename exists
def file_exists(filename):

    path = '/mnt/c/Users/LJ/scripts/defanger/' + str(filename)

    if os.path.isfile(path):
        # print("File Exists: True!", filename)
        return True
    else:
        # print("File Exists: False!", filename)
        return False

# function adds '.txt' to filename that doesn't have it
def extension_check(filename):
    if ".txt" in filename:
        return filename
    else:
        print("You forgot a file extension, adding '.txt'")
        newfilename = str(filename) + ".txt"
        return newfilename

# function adds "1" just before file extension if no number is present
def iterability_check(iterator, filename):
    if iterator.isdigit():
        return filename
    else:
        print("File has no iterable value - adding")
        newfilename = str(filename.replace(".txt", "1.txt"))
        return newfilename

# function takes a .txt file name, and creates a file by that name. 
def create_file(filename):
    print("Writing File: ", filename)
    # write file
    with open(str(filename), "w+") as fi:
        fi.write("")
        fi.close()

# function determines if command line argument for output file was specified
def specific_output(argument):
    if str(argument) == "None":
        print("Output File Not Specified, using Default")
        return False
    else:
        # print('Output File (specific_output): ', argument)
        return True

# function takes file name and iterates it until it finds one that doesn't exist
def filename_iterator(file):
    # while file exists, iterate its name
    if file_exists(file):
        file_iterate = str(file[-5])
        
        # ensure file_iterate is an int / valid iterator
        icheck = str(iterability_check(file_iterate, file))

        known_good_iterator = str(icheck[-5])

        i = int(known_good_iterator)
        j = i + 1

        # Debugging Block
        # print("known good iterator: ", known_good_iterator)
        # print("icheck: ", icheck)
        # print("file_iterate: ", file_iterate)
        # print("File Name: ", file)
        # print("i: ", i)
        # print("J: ", j)

        # Actual Iteration Happens Here
        newfileName = str(icheck.replace(str(i), str(j)))

        # Debug
        # print("New File Name (post-iteration): ", newfileName)
        # return 
        return newfileName
    
    # filename doesn't exist, return original file
    else:
        return file

# function calls filename_iterator if file it's fed exists
# creates unique filename
def file_logic(filename):
    
    # while filename exists, iterate it until it doesn't
    while file_exists(filename):
        # filename_iterator function call
        # print("Output Filename exists, Iterating")
        newfile = filename_iterator(str(filename))
        # print("New Output File: ", newfile)
        filename = newfile
            
    # when loop exits, create file
    #print("Iterator Exiting, creating new output file")
    create_file(filename)
    return filename

    # else specified filename doesn't exist        
   # else:
        # create new file
       # print("Specified Output Filename doesn't Exist, Creating")
       # create_file(filename)

# function uses create_file, specific_output, and file_logic to:
# - determine if output file command line argument was used
#   - if yes, determine if specified output filename  exists
#       - if yes, iterate the name
#       - if no, use the name 
def new_out_file(filename):
    # looks for the specific output option
    output_determinant = specific_output(filename)
    #print("Output File (new_out_file): ", filename)
    
    # if specified filename argument exists
    if output_determinant == True:
        # call file_logic with specified filename
        # print("Specified Output File In Use")
        file_name = file_logic(filename)
        return file_name
        
    # else filename argument does not exist, use default filename
    else:
        # call file_logic with default filename
        print("No Output File Specified, using Default")
        file_name = file_logic("defanger_output_1.txt")
        return file_name

# defanger function - reads input file line by line, defangs, and writes result to output file.
# This is where the magic happens
def defanger(in_file, out_file):
    # open input .txt file
    with open(str(in_file)) as fr:
        # open output .txt file
        with open(str(out_file), 'a+') as fw:
            # read
            for line in fr:
                # defang
                new_line = defang(line, all_dots=True, colon=True)
                # write
                fw.write(new_line)

# run function - calls functions
def run_boi(file_in, file_out):
    # check if input file exists. If it does, proceed.
    # if it doesn't, the program won't run - exit
    if file_exists(file_in) == True:
        # run output filename through new_out_file.
        # This will:
        # 1. Check if the specific output option was used
        # 2. Check if the specified output filename already exists
        # 3. If 2 is yes, it will automatically iterate the filename until it finds one that doesn't exist
        # print("Successfully Selected Input File")
        file_boi = extension_check(file_out)
        file_name = new_out_file(file_boi)
        defanger(file_in, file_name)

    else:
        print("Input File doesn't Exist - Choose one that Does")
        # Exit Program

# run the program
run_boi(arg_in, arg_ou)

# closel

# read lines of file into list

# defang urls in list
    # replace . with [.]
    # replace https:// with hxxps ://

# write list into lines of new file
