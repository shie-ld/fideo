# module : python imaging library : support for image processing
from PIL import Image

# module : numerical python : fast and efficient processing for arrays
import numpy as np

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