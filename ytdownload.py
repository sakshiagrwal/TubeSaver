from pytube import YouTube
import title
print(":")
link = input(">")
print("")
yt = YouTube(link)
ys = yt.streams.highest_resolution()
print("Video title: " + yt.title)
print("Resolution: " + ys.resolution)
ys.download("")
print("download has been completed")
