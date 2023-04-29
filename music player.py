import os
import tkinter as tk
from tkinter import filedialog
import pygame

# Set up pygame mixer
pygame.mixer.init()

# Define global variables
paused = False
stopped = True

# Define a function to play music
def play_music(file):
    global stopped
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    stopped = False

# Define a function to pause music
def pause_music():
    global paused
    if not paused:
        pygame.mixer.music.pause()
        paused = True
    else:
        pygame.mixer.music.unpause()
        paused = False

# Define a function to stop music
def stop_music():
    global stopped
    pygame.mixer.music.stop()
    stopped = True

# Define a function to open a file dialog and select a music file
def choose_music_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        play_music(file_path)

# Define the main function
def main():
    global stopped
    # Create the main window
    window = tk.Tk()
    window.title("Music Player")

    # Create the widgets
    choose_button = tk.Button(window, text="Choose File", command=choose_music_file)
    play_button = tk.Button(window, text="Play", command=lambda: play_music(file_path.get()))
    pause_button = tk.Button(window, text="Pause", command=pause_music)
    stop_button = tk.Button(window, text="Stop", command=stop_music)
    file_path = tk.Entry(window, width=50)

    # Pack the widgets
    choose_button.pack(pady=5)
    file_path.pack(pady=5)
    play_button.pack(pady=5)
    pause_button.pack(pady=5)
    stop_button.pack(pady=5)

    # Run the main loop
    window.mainloop()

# Call the main function
if __name__ == "__main__":
    main()

