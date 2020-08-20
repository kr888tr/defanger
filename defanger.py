#########################################################################################################
###                         DEFANGER. Defangs URLs and IP addresses.                                  ###             
#########################################################################################################

# import packages
import argparse
import os

# Initialize parser and arguments
parser = argparse.ArgumentParser(description="defanger parse")
parser.add_argument("-i", "--input", help = "Designate Input File", required=True)
parser.add_argument("-o", "--output", help = "Designate Output File", required=False)
args = parser.parse_args()

# Name Input / Output variables for ease of use
arg_in = args.input
arg_ou = args.output

# error checking, ignore
print('inputfile: ', arg_in)
print('outputfile: ', arg_ou)

# function checks if filename exists
def file_exists(filename):
    if os.path.isfile(filename):
        print("True!", filename)
        return True
    else:
        print("False!", filename)
        return False

# function takes a .txt file name, and creates a file by that name. 
def create_file(filename):
    print("Writing File: ", filename)
    with open(str(filename), "w+") as fi:
        fi.write("")
        fi.close()

# function determines if command line argument for output file was specified
def specific_output(argument):
    if argument == "None":
        print("Output File Not Specified, using Default")
        return False
    else:
        print('Output File: ', argument)
        return True

# function takes file name and iterates it until it finds one that doesn't exist
def filename_iterator(file):
    # while file exists, iterate its name
    while file_exists(file):
        i = int(file[-5])
        j = i + 1

        # Debugging Block
        print("File Name: ", file)
        print("i: ", i)
        print("J: ", j)

        # Actual Iteration Happens Here
        file.replace(i, j)

    return file

# function calls filename_iterator if file it's fed exists
# creates unique filename
def file_logic(filename):
    # if filename exists
    if file_exists(filename):
        # filename_iterator function call
        print("Specified Output Filename exists, Iterating")
        newfile = filename_iterator(filename)
            
        # when loop exits, create file
        print("Iterator Exiting, creating new output file")
        create_file(newfile)

    # else specified filename doesn't exist        
    else:
        # create new file
        print("Specified Output Filename doesn't Exist, Creating")
        create_file(filename)

# function uses create_file, specific_output, and file_logic to:
# - determine if output file command line argument was used
#   - if yes, determine if specified output filename  exists
#       - if yes, iterate the name
#       - if no, use the name 
def new_out_file(filename):
    
    output_determinant = specific_output(filename)
    print("Doing Logic")
    
    # if specified filename argument exists
    if output_determinant == True:
        
        # call file_logic with specified filename
        print("Specified Output File In Use")
        file_logic(filename)
        
    # else filename argument does not exist, use default filename
    else:

        # call file_logic with default filename
        print("No Output File Specified, using Default")
        file_logic("defanger_output.txt")

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
        print("Successfully Selected Input File")
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
