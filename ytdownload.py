from pytube import YouTube

print("Please input your youtube link below:")
link = raw_input(">")
print("")
yt = YouTube(link)
# Use a different method to download the highest resolution video
ys = yt.streams.first()
print("Video title: " + yt.title)
print("Resolution: " + ys.resolution)
# Provide a valid path to save the downloaded video
ys.download("/path/to/save/video")
print("download has been completed")
