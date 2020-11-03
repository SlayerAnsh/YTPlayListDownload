from pytube import Playlist
from pytube import YouTube
import logging


# making logger to print progress of the download
# If not needed you can comment this block of code
logger = logging.getLogger('pytube.streams')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)


# Path where you want to save. Will make it platform independent in near future till then remember to change '\' to '/' for linux 
SavePath = "F://Automation//YouTube"

# playlist link goes here
playlist = Playlist('https://www.youtube.com/playlist?list=listdGoesHere')

# print total number of videos in the given playlist
print('Number of videos in playlist: %s' % len(playlist.video_urls))


i = 0;
for video_url in playlist.video_urls:
    # Print url of current cideo. You can check title also
    print(video_url)

    # Adjust range according too your need. Use it to limit number of videos to download
    if i < 20:
    	i = i+1
    	continue;
    if i > 30:
    	break;
    i=i+1
    
    # Downloading video part.
    yt = YouTube(str(video_url))
    yt.streams.first().download(SavePath)
    print("\n--------------------------------------------------------------------------------\n")


# NOTE -> If file is already present download will be skipped.