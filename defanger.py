print("This is the initial commit to get the repo started")

# Pseudocode Outline

# import packages
import argparse

# Initialize parser and arguments
parser = argparse.ArgumentParser(description="defanger parse")
parser.add_argument("-i", "--input", help = "Designate Input File", required=True)
parser.add_argument("-o", "--output", help = "Designate Output File", required=True)

# Get user input .txt file
arg_in = parser.parse_args(0)
# get output .txt file from command line arguments
arg_out = parser.parse_args(1)
# error checking, ignore
print(arg_in)
print(arg_out)

# read lines of file into list

# defang urls in list
    # replace . with [.]
    # replace https:// with hxxps ://

# write list into lines of new file

# close file

# exit gracefully