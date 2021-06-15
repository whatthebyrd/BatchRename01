#!/usr/bin/env python3

# batchRename01
# Invoke by: batchRename01 <NewName> <ExcludeFileThatStartWithThis(OPTIONAL)>
# Takes all files in local path and renames with first arg value and numeric counter excluding files that start with second arg value
# Original Creation: 15JUN20
# Released under Apache 2.0 License

import os # For checking file path and replacing file extension
import sys # For parsing input arguments

files = [f for f in os.listdir() if os.path.isfile(f)] # PREDEP: Remove arg and switch to local dir work only
filesSkippedCt = 0

if len(sys.argv) == 3:
    for i in range(len(files)):
        oldext = os.path.splitext(files[i])[1]
        if files[i].startswith(sys.argv[2]):
            filesSkippedCt += 1
            continue
        os.rename(files[i], sys.argv[1] + str(i - filesSkippedCt) + oldext)
    print(str(len(files) - filesSkippedCt) + " files in " + os.getcwd() + " renamed to " + sys.argv[1] + " successfully.")
elif len(sys.argv) == 2:
    for i in range(len(files)):
        oldext = os.path.splitext(files[i])[1]
        os.rename(files[i], sys.argv[1] + i + oldext)
    print(str(len(files)) + " files in " + os.getcwd() + " renamed to " + sys.argv[1] + " successfully.")

else:
    print("Error: New filename required. Exiting.")
