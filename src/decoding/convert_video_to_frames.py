import ffmpeg

def convert_video_to_frames(INPUT, FRAMERATE):
    print("Converting video file to respective frames...")
    
    (
        ffmpeg
        .input(INPUT)
        .filter('fps', fps=FRAMERATE, round='down')
        .output('./outframes/frame_%d.png')
        .run()
    )
#     os.system('ffmpeg -i ' + videopath + ' -r 24 ./outframes/frame_%d.png')
    
    print("Successfully generated all frames")