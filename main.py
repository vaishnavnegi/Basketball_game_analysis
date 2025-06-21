from utils import read_video, save_video
from trackers import PlayerTracker, BallTracker
from drawers import PlayerTracksDrawer, BallTracksDrawer
from team_assignment import TeamAssigner

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
    # Remove wrong detections
    ball_tracks = ball_tracker.remove_wrong_detections(ball_tracks)
    # Interpolate Ball Positions
    ball_tracks = ball_tracker.interpolate_ball_positions(ball_tracks)

    # Assign Teams to Players
    team_assigner = TeamAssigner()
    player_assignment = team_assigner.get_player_teams_across_frames(video_frames, 
                                                                player_tracks,                                                        
                                                                read_from_stub=True,
                                                                stub_path="stubs/player_teams.pkl"
                                                                )
    
    #Drawing Player Tracks
    #Initialize drawers
    player_tracks_drawer = PlayerTracksDrawer()
    ball_tracks_drawer = BallTracksDrawer()
    
    # Drawing Player Tracks
    output_video_frames = player_tracks_drawer.draw(video_frames, player_tracks, player_assignment)
    
    # Drawing Ball Tracks
    output_video_frames = ball_tracks_drawer.draw(output_video_frames, ball_tracks)

    # Save video
    save_video(output_video_frames, "output_videos/video_1.avi")

if __name__ == '__main__':
    main()