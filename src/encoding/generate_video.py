# module : video processing support for python
import ffmpeg

import shutil

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