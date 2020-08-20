# defanger

This script will take a .txt file of url's or IP addresses and defang them. 
Uses https://pypi.org/project/defang/ for the actual defang-ing, this is more of a convenient framework for defanging a large batch of links for use in reporting. 

Usage: 

python defanger.py -i inputfile.txt -o outputfile.txt

Notes:

Options:

-i option is mandatory. Designates target for input file.

-o option is optional.  Designates target for ouput file. If not used, script will generate a default .txt file. 

Behavior: 

- If specific output filename is requested, and it already exists, the script will automatically iterate the filename. 

- If the user does not designate a file extension, the script will append a ".txt" extension. 

