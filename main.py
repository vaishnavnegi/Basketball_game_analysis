from utils import read_video, save_video
from trackers import PlayerTracker, BallTracker
from drawers import PlayerTracksDrawer, BallTracksDrawer

def main():

    # Read Video
    video_frames = read_video("input_videos/video_1.mp4")

    # Initialize Player Tracker
    player_tracker = PlayerTracker("models/Player_Detector.pt")
    
    # Initialize Ball Tracker
    ball_tracker = BallTracker("models/Ball_Detector.pt")

    # Run Player Tracker
    player_tracks = player_tracker.get_object_tracks(video_frames,
                                                     read_from_stub=True,
                                                     stub_path="stubs/player_tracks.pkl"
                                                     )
    # Run Ball Tracker
    ball_tracks = ball_tracker.get_object_tracks(video_frames,
                                                 read_from_stub=True,
                                                 stub_path="stubs/ball_tracks.pkl"
                                                 )    
    #Drawing Player Tracks
    #Initialize drawers
    player_tracks_drawer = PlayerTracksDrawer()
    ball_tracks_drawer = BallTracksDrawer()
    
    # Drawing Player Tracks
    output_video_frames = player_tracks_drawer.draw(video_frames, player_tracks)
    
    # Drawing Ball Tracks
    output_video_frames = ball_tracks_drawer.draw(output_video_frames, ball_tracks)

    # Save video
    save_video(output_video_frames, "output_videos/video_1.avi")

if __name__ == '__main__':
    main()