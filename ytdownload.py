from pytube import YouTube
import title
print("Please input your youtube link below:")
link = input(">")
print("")
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()
print("Video title: " + yt.title)
print("Resolution: " + ys.resolution)
ys.download("")
print("download has been completed")
