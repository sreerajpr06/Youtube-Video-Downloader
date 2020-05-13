##https://www.youtube.com/watch?v=HgzGwKwLmgM
##https://www.youtube.com/watch?v=3swcKhG-xXs
from pytube import YouTube

def vidDownload(yt):
    try:
        stream = yt.streams
        res = [s.resolution for s in stream if s.resolution!=None]
        res = list(dict.fromkeys(res))
        res = list(sorted(res, reverse=True))
        
        for i in res:
            print(i, ' ')
    
        res = input("Enter the res : ")
        print(res)
        stream = yt.streams.filter(res=res)
        stream = stream.first()
        print(stream)
        #stream.download()
        print("success")
    except:
        print("Error")

if __name__ == "__main__":
    link = input("Enter the url : ")
    print(link)
    yt = YouTube(link)
    title = yt.title
    print(title)
    vidDownload(yt)

## res = [s.resolution for s in stream if s.resolution!=None]
    
   
