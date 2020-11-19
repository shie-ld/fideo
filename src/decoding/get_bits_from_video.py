# module : unix style pathname pattern expansion
import glob
import shutil

from convert_video_to_frames import convert_video_to_frames
from convert_image_to_bits import convert_image_to_bits

def get_bits_from_video(videopath):
    print("Getting bits from video file...")
    
    bits = ""
    convert_video_to_frames(videopath)
    
    for image in sorted(glob.glob("./outframes/*.png")):
        bits += convert_image_to_bits(image)
    
    shutil.rmtree('./outframes')
    print("Successfully retrieved bits from video file")
    
    return bits