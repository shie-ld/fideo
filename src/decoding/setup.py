# module : to interact with the operating system
import os

# module :  for high level operations on files and collection of files
# helps in automating the copying and removal of files and directories
import shutil

# making the setup
def setup():
    # directory to store intermediate frames to make video file 
    outframes = './outframes'

    # first removing the directory if it contains anything
    shutil.rmtree(outframes)
    
    os.makedirs(outframes)