#importing the module
from pytube import YouTube

#where to save
SAVE_PATH="(location of the path)"

#link of the video to be downloaded
link="(link)"

try:
  #object creation from YouTube which was imported in the beginning
  yt=YouTube(link)
except:
  #to handle exception
  print("Connection error")
  
#filters out all the files from "mp4" extention
mp4files=yt.filter('mp4')

#to set the name of the file
yt.set_filename("(filename)")

#get the video with extention and resolution passed in the get() function
d_video=yt.get(mp4files[-1].extention,mp4files[-1].resolution)

try:
 #downloading the video
 d_video.download(SAVE_PATH)
except:
 print("some error")
 
print("download complete") 
 
