# module : to interact with the operating system
import os

# module :  for high level operations on files and collection of files
# helps in automating the copying and removal of files and directories
import shutil

# function: to delete contents of the given folder
def rm_dir_content(dir):
    for filename in os.listdir(dir):
        file_path = os.path.join(dir, filename)
        try:
            # if it is a file or a symbolic link, delete or unlink the file
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                
            # if it is a directory, remove directory tree
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


# making the setup
def encoding_setup():
    # directory to store intermediate frames to make video file 
    inframes = './inframes'

    # if inframes does not exist, create it
    if not os.path.exists(inframes):
        os.makedirs(inframes)
    
    # delete anything present in inframes directory
    rm_dir_content(inframes)