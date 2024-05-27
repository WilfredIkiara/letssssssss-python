#youtube downloader
#The code below lets you download videos from youtube by listing the url
#and selecting the location of storage

from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")

        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path = save_path)
        print("Video dowloaded succesfully!")
    except Exception as e:
        print(e)

#url ="https://www.youtube.com/watch?v=H988Oc3_Q98"#darkness
#url = "https://www.youtube.com/watch?v=NXQBNBc-EiE"#watch over us
#save_path = "/home/gh0st/Desktop/code/2024 code/lets python/projects"

#download_video(url, save_path)

def open_file_dialogue():
    folder = filedialog.askdirectory()
    print(f"selected folder {folder}")
    return folder



if __name__ =="__main__":
      root = tk.Tk()#creates a tk window
      root.withdraw()#hides the initialized window

      video_url = input("please enter a youtube url:")
      save_dir = open_file_dialogue()

      if not save_dir:
          print("download started")
          print("please select a folder")
      else:
          download_video(video_url, save_dir)
          