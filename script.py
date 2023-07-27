from pytube import YouTube

video_url = input("Enter the URL of the YouTube video: ")

try:
    yt = YouTube(video_url)
    video_stream = yt.streams.get_highest_resolution()  # Get the highest resolution stream
    video_stream.download()  # Download the video
    print("Video downloaded successfully!")
except Exception as e:
    print("Error:", e)
