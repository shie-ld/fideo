# module : video processing support for python
import ffmpeg

# function : generate video file from frames
def generate_video():
#     FRAMERATE = 24
    print("Generating video file...")
    
    (
        ffmpeg
        .input('./inframes/frame_%d.png')
        .filter('fps', fps=25, round='up')
        .output('output.mp4')
        .run()
    )
#     os.system('ffmpeg -framerate 24 -i ./inframes/frame_%d.png output.mp4')
    
    print("Successfully generated video file")