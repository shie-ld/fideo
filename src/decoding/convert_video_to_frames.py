import ffmpeg

def convert_video_to_frames(videopath):
    print("Converting video file to respective frames...")
    
    (
        ffmpeg
        .input('output.mp4')
        .filter('fps', fps=25, round='down')
        .output('./outframes/frame_%d.png')
        .run()
    )
#     os.system('ffmpeg -i ' + videopath + ' -r 24 ./outframes/frame_%d.png')
    
    print("Successfully generated all frames")