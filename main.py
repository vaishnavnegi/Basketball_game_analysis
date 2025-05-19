from utils import read_video, save_video

def main():

    # Read Video
    video_frames = read_video("input_videos/video_1.mp4")

    # Save video
    save_video(video_frames, "output_videos/video_1.mp4")

if __name__ == '__main__':
    main()