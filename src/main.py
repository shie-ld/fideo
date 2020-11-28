# importing required modules

# module : to interact with the operating system
import os

# module :  for high level operations on files and collection of files
# helps in automating the copying and removal of files and directories
import shutil

# module : gzip support for files 
import gzip

# contextlib module :  provides utilities for common tasks involving the 'with' statement
from contextlib import ExitStack

# bitstring module :  for the creation and analysis of binary data
from bitstring import BitArray,Bits

# module : python imaging library : support for image processing
from PIL import Image

# module : numerical python : fast and efficient processing for arrays
import numpy as np

# module : video processing support for python
import ffmpeg

# module: unix like pathname expansion
import glob

# argument parser for python
import argparse

# encoding part

# outline
#  1. encoding_setup
#  2. compress_file
#  3. get_bitarray
#  4. generate_frames
#  5. generate_video

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
    
    # delete the previous video file by same default name - OUTFILE.mp4
    if(os.path.isfile('OUTFILE.mp4')):
        os.remove('OUTFILE.mp4')

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

# function : get binary representation of a file
def get_bitarray(INPUT):
    print("Converting " + os.path.basename(INPUT) + " to binary form...")
    
#   stores the hexdump of the file in a bitstring.BitArray object
    bitarray = BitArray(filename = INPUT)
#     print("Type: " ,type(bitarray))
#     print("Hexdump: ", bitarray)

    # removing the gzip file after deriving bitarray from it
    os.remove(INPUT + ".gz")
    
    print("Successfully converted " + os.path.basename(INPUT) + " to binary form")

#   returns the binary dump of file
#     print("Bindump: ", bitarray.bin)
    return bitarray.bin
    

# function : generate frames from binstring.BitArray object
def generate_frames(bitarray):
#   RESOLUTION = (HEIGHT, WIDTH) : resolution of the video
    RESOLUTION = (480, 854)
    
    print("Generating frames...")
    
    index = 0
    frame_num = 0
    while(index < len(bitarray)):
#       generating a numpy array with the bitarray[index : index + resolution] slice
#       with data type as int
        pixels = np.fromiter(bitarray[index : index + (RESOLUTION[0] * RESOLUTION[1])], dtype = np.int)
        
        if(pixels.size < (RESOLUTION[0] * RESOLUTION[1])):
            pixels = np.concatenate((pixels, np.zeros((RESOLUTION[0] * RESOLUTION[1]) - pixels.size ,dtype = int)))
        
#       creating a new instance of 1-bit pixel image with the specified resolution and
#       with 1 pixel per byte. tuple denotes (width, height)
        image = Image.new("1", (RESOLUTION[1], RESOLUTION[0]))
        
        image.putdata(pixels)
        image.save("./inframes/" + "frame_" + str(frame_num) + ".png")
#         print("Generated frame: " + str(frame_num))
        
        del pixels
        del image
        frame_num += 1
        index += (RESOLUTION[0] * RESOLUTION[1])
    
    print("Successfully generated all frames")

# function : generate video file from frames
def generate_video(OUTPUT, FRAMERATE):
#     FRAMERATE = 24
    print("Generating video file...")
    
    (
        ffmpeg
        .input('./inframes/frame_%d.png')
        .filter('fps', fps=FRAMERATE, round='up')
        .output(OUTPUT)
        .run()
    )
#     os.system('ffmpeg -framerate 24 -i ./inframes/frame_%d.png output.mp4')
    
    shutil.rmtree('./inframes')
    print("Successfully generated video file")







# decoding part

# outline
#  1. decoding_setup
#  2. get_bits_from_video
#     1. convert_video_to_frames
#     2. convet_image_to_bits
#  3. get_file_from_bits

# making the setup
def decoding_setup():
    # directory to store intermediate frames to make video file 
    outframes = './outframes'

    # first removing the directory if it contains anything
    if(os.path.isdir(outframes)):
        shutil.rmtree(outframes)
    
    os.makedirs(outframes)

def convert_video_to_frames(INPUT, FRAMERATE):
    print("Converting video file to respective frames...")
    
    (
        ffmpeg
        .input(INPUT)
        .filter('fps', fps=FRAMERATE, round='down')
        .output('./outframes/frame_%d.png')
        .run()
    )
    
    print("Successfully generated all frames")

def convert_image_to_bits(imagepath):
    image = Image.open(imagepath)
    width, height = image.size
    bits = ""
    pixels = image.load()
    del image
    
    for j in range(height):
        for i in range(width):
            pixel = pixels[i, j]
            pixel_bin_rep = "0"
            
#           if white difference is smaller then black difference, then 
#           pixel_bin_rep must be "1"
            if (abs(pixel[0] - 255) < abs(pixel[0] - 0)
            and abs(pixel[1] - 255) < abs(pixel[1] - 0)
            and abs(pixel[2] - 255) < abs(pixel[2] - 0)):
                pixel_bin_rep = "1"
                
            bits += str(pixel_bin_rep)
    del pixels
    return bits

def get_bits_from_video(videopath, FRAMERATE):
    print("Getting bits from video file...")
    
    convert_video_to_frames(videopath, FRAMERATE)
    
    bits = ""
    
    for image in sorted(glob.glob("./outframes/*.png")):
        bits += convert_image_to_bits(image)
    
    shutil.rmtree('./outframes')
    print("Successfully retrieved bits from video file")
    
    return bits

def get_file_from_bits(bits, OUTPUT):
    print("Generating file from bits...")
    
    bitstring = Bits(bin = bits)
    bitstring = BitArray(bitstring)
    
    
    with open(OUTPUT, 'wb') as outfile:
        bitstring.tofile(outfile)
        
    del bitstring
    
    print("Successfully retrieved the file")







# actual function to encode files
def encode_file(INPUT, OUTPUT):
    FRAMERATE = 24
    
    encoding_setup()
    compress_file(INPUT)
    bitarray = get_bitarray(INPUT)
    generate_frames(bitarray)
    generate_video(OUTPUT, FRAMERATE)
    return

#actual function to decode files
def decode_file(videopath, OUTPUT = 'OUTFILE.gz'):
    FRAMERATE = 24
    
    decoding_setup()
    bits = get_bits_from_video(videopath, FRAMERATE)
    get_file_from_bits(bits, OUTPUT)
    return



def main():
    FRAMERATE = 24

    parser = argparse.ArgumentParser(
        description="fideo: file to video convertor"
    )

    parser.add_argument(
        "-e", "--encode", help="encode file to video", action="store_true"
    )

    parser.add_argument(
    "-d", "--decode", help="decode video to file", action="store_true" 
    )

    parser.add_argument(
        "-i", "--input", help="input file", required=True
    )

    parser.add_argument(
        "-o", "--output", help="output file"
    )

    parser.add_argument(
        "-f", "--framerate", help="framerate of video", default=FRAMERATE
    )

    args = parser.parse_args()

    # setting the framerate
    if(args.framerate != FRAMERATE):
        FRAMERATE = args.framerate

    # checking for input arguments
    if not args.decode and not args.encode:
        raise MissingArgument("Either use -e|--encode or -d|--decode!!")

    INPUT = args.input

    if args.encode:
        OUTPUT = 'output.mp4'
        
        if(args.output):
            OUTPUT = args.output
            
        encode_file(INPUT, OUTPUT)
        
    if args.decode:
        OUTPUT = 'output'
        
        if args.output:
            OUTPUT = args.output
        
        decode_file(INPUT, OUTPUT)



if(__name__ == '__main__'):
	main()
	
	
	
	
	
