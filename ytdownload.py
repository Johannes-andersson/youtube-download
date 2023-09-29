from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
      youtubeObject.download()
  except:
    print("There has been an error in downloading try again ")
  print("This download has completed with success! Enjoy and watch offline! ")

link = input("Put your youtube link here !! URL: ")
Download(link)
