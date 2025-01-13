import tkinter as tk
from tkinter import messagebox
import vlc
import time
import threading
import keyboard  # To detect key presses

# Function to play the video with sound
def play_video_with_sound(video_path):
    global stop_video
    stop_video = False  # Flag to stop playback

    # Create an instance of VLC
    instance = vlc.Instance()
    player = instance.media_player_new()
    
    # Set the video file
    media = instance.media_new(video_path)
    player.set_media(media)

    # Set fullscreen
    player.set_fullscreen(True)

    # Play the video
    player.play()

    # Keep the video playing and listen for stop signal
    while True:
        if stop_video:
            print("Stopping video playback.")
            player.stop()
            break

        state = player.get_state()
        if state in [vlc.State.Ended, vlc.State.Error]:  # Loop video
            player.stop()
            player.play()

        time.sleep(1)

# Function to listen for a stop key
def listen_for_stop_key():
    global stop_video
    keyboard.wait('q')  # Wait for the user to press 'q'
    stop_video = True  # Set the flag to stop the video

# Display a popup message
def show_message():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Alert", "You've been hacked (just kidding, it's for learning!)")
    root.destroy()

if __name__ == "__main__":
    # Path to your video file
    video_path = "video.mp4"

    # Show the message
    show_message()

    # Start the stop listener in a separate thread
    stop_thread = threading.Thread(target=listen_for_stop_key, daemon=True)
    stop_thread.start()

    # Play the video with sound in fullscreen
    play_video_with_sound(video_path)
