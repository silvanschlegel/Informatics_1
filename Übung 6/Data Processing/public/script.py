#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        # what to do if the input file does not exist?
        return False

    with open(path_reading, 'r') as f:

        with open(path_writing, 'w') as g:
            content = f.readlines()
            # if input file is empty, return empty output file
            if os.stat(path_reading).st_size == 0:
                return path_writing
            g.write("Firstname,Lastname")
            if len(content) > 1:
                g.write("\n")
            # if inpout file only contains header, only write header Firstname,Lastname in the new file
            if content == "Name":
                return path_writing
            for i,line in enumerate(content[1:]):
                if line == "\n":
                    g.write(",\n")
                else:
                    if line.__contains__(";"):
                        line_1 = line.split("; ")
                        g.write(str(line_1[1].strip("\n") + "," + line_1[0].strip("\n")))
                    else:
                        line_1 = line.split()
                        g.write(str(line_1[0].strip("\n") + "," + line_1[1].strip("\n")))


                    if i < len(content)-2:
                        g.write("\n")
    return path_writing







# The following line calls your solution function with the provided input file
# and then attempts to read and print the contents of the resulting output file.
# You do not need to modify these lines.
INPUT_PATH = "my_data.txt"
OUTPUT_PATH = "my_data_processed.txt"
process_data(INPUT_PATH, OUTPUT_PATH)
if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH) as resultfile:
        print(resultfile.read())
else:
    print("No output file exists")

