from utils import read_video, save_video
from trackers.player_tracking import PlayerTracker

def main():

    # Read Video
    video_frames = read_video("input_videos/video_1.mp4")

    # Initialize Player Tracker
    player_tracker = PlayerTracker("models/Player_Detector.pt")

    # Run Player Tracker
    player_tracks = player_tracker.get_object_tracks(video_frames,
                                                     read_from_stub=True,
                                                     stub_path="stubs/player_tracks.pkl"
                                                     )

    print(player_tracks)

    # Save video
    # save_video(video_frames, "output_videos/video_1.avi")

if __name__ == '__main__':
    main()