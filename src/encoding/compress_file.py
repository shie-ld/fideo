# module : gzip support for files 
import gzip

# module :  for high level operations on files and collection of files
# helps in automating the copying and removal of files and directories
import shutil

# contextlib module :  provides utilities for common tasks involving the 'with' statement
from contextlib import ExitStack

# module : to interact with the operating system
import os

# function : compress a file using gzip compression 
def compress_file(INPUT):
#   os.path.basename() : removes the leading path information of the file and leaves only 
#   with the actual filename from the complete path
#   /home/user/file.txt -> file.txt
    print("Compressing " + os.path.basename(INPUT) + "...")
    
#   creates a stack of files so that we can define operations one after the other
#   helpful in removing nested 'with' statements
    with ExitStack() as stack:
        f_in = stack.enter_context(open(INPUT, 'rb'))
        f_out = stack.enter_context(gzip.open(INPUT + ".gz", 'wb'))
        shutil.copyfileobj(f_in, f_out)
        
#       deleting unused objects
        del f_in
        del f_out
        
    print("Successfully compressed " + os.path.basename(INPUT))