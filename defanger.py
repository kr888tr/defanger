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

# Name Variables for ease of use
arg_in = args.input
arg_ou = args.output

# error checking, ignore
print('inputfile: ', arg_in)
print('outputfile: ', arg_ou)

# function checks if filename exists
def file_exists(filename):
    if os.path.isfile(filename):
        return True
    else:
        return False

# function takes a .txt file name, and creates a file by that name. 
def create_file(filename):
    print("Writing File: ", filename)
    with open(str(filename), "w+") as fi:
        fi.write("")
        fi.close()

# function determines if command line argument for output file was specified
def specific_output():
    if arg_ou == "None":
        print("Output File Not Specified, using Default")
        return False
    else:
        print('Output File: ', arg_ou)
        return True

# function takes file name and iterates it until it finds one that doesn't exist
def filename_iterator(file):
    # while file exists, iterate its name
    while file_exists(file):
        i = int(file[-4])


# function uses create_file and specific_output to: 
def new_out_file(filename):
    output_determinant == specific_output()
    print("Doing Logic")
    # if specified filename argument exists
    if output_determinant == True:
        # if filename exists
        if file_exists(filename):
            print("Do Logic")
            # while loop: while filename exists, iterate until it doesn't
            # when loop exits, create file
        # else filename doesn't exist
            # create file
    

# read lines of file into list

# defang urls in list
    # replace . with [.]
    # replace https:// with hxxps ://

# write list into lines of new file

# close