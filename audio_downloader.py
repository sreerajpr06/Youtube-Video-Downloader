import pafy

if __name__ == "__main__":
  
    link = input("Enter the url : ")
    video = pafy.new(link) 
    bestaudio = video.getbestaudio() 
    bestaudio.download() 

