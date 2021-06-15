#!/usr/bin/env python3

# batchRename01
# Invoke by: batchRename01 <NewName> <ExcludeFileThatStartWithThis(OPTIONAL)>
# Takes all files in local path and renames with first arg value and numeric counter excluding files that start with second arg value
# Original Creation: 15JUN20
# Released under Apache 2.0 License

import os # For checking file path and replacing file extension
import sys # For parsing input arguments

files = [f for f in os.listdir() if os.path.isfile(f)]  # List files in directory
filesSkippedCt = 0  # Used to keep track of renamed file numbers when excluding files

if len(sys.argv) == 3:  # Arguments are 1: new name and 2: filenames that start with this to exclude
    for i in range(len(files)):
        oldext = os.path.splitext(files[i])[1]  # Split out file names (old) and extensions to preserve extensions
        if files[i].startswith(sys.argv[2]):  # Check to skip file is excluded
            filesSkippedCt += 1  # Keep count of number of files excluded
            continue
        os.rename(files[i], sys.argv[1] + str(i - filesSkippedCt) + oldext)  # Rename files with new names plus numeric count and extension
    print(str(len(files) - filesSkippedCt) + " files in " + os.getcwd() + " renamed to " + sys.argv[1] + " successfully.")
elif len(sys.argv) == 2:  # Argument is 1: new name
    for i in range(len(files)):
        oldext = os.path.splitext(files[i])[1]  # Split out file names (old) and extensions to preserve extensions
        os.rename(files[i], sys.argv[1] + str(i) + oldext)  # Rename files with new names plus numeric count and extension
    print(str(len(files)) + " files in " + os.getcwd() + " renamed to " + sys.argv[1] + " successfully.")
else:
    print("Error: New filename required. Exiting.")  # FUTURE WORK: Errors for invalid filenames, improper permissions. warning before execution if no excluded files detected
