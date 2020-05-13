from flask import Flask, render_template, request, redirect
from pytube import YouTube


app = Flask(__name__)
link = str()
res = []

@app.route('/', methods=['POST', 'GET'])

def index():
    if request.method == 'POST':
        link = request.form['URL']

        try:
            yt = YouTube(link)
            stream = yt.streams
            res = [s.resolution for s in stream if s.resolution!=None if s.is_adaptive==False]
            res = list(dict.fromkeys(res))
            res = list(sorted(res, reverse=True))
            title = yt.title
            return render_template('/downloadPg.html', res=res, title=title, link=link)

        except:
            return "Error!"
    else:
        return render_template('index.html')


@app.route('/resChoose/', methods=['POST', 'GET'])

def resChoose():

    if request.method == 'POST':
        try:
            link = str(request.form['URL'])
            res = str(request.form['res'])
            yt = YouTube(link)
            stream = yt.streams.filter(res=res, adaptive=False)
            stream = stream.first()
            stream.download()
            return render_template('index.html')
        except:
            return "Error downloading"    

    else:
        return render_template('downloadPg.html')


if __name__ == "__main__":
    app.run(debug=True)
