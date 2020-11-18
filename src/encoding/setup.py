# module : to interact with the operating system
import os

# module :  for high level operations on files and collection of files
# helps in automating the copying and removal of files and directories
import shutil

# function to remove contents of a directory
from rm_dir_content import rm_dir_content

# making the setup
def setup():
    # directory to store intermediate frames to make video file 
    inframes = './inframes'

    # if inframes does not exist, create it
    if not os.path.exists(inframes):
        os.makedirs(inframes)
    
    # delete anything present in inframes directory
    rm_dir_content(inframes)