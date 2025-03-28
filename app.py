from flask import Flask, send_file, render_template
from pytubefix import YouTube
from pytubefix.cli import on_progress

def getMpFour(link):
    
    yt = YouTube(link , on_progress_callback = on_progress)
    print(yt.title)
    
    video = yt.streams.get_highest_resolution()
    filePath = video.download('./video')
    return filePath

app = Flask(__name__)

@app.route('/index')
def index() :
    return render_template('index.html')

@app.route("/<path:arg>")
def getVideo(arg) :
    file_path = getMpFour(arg)
    response = send_file(file_path, as_attachment=True)
    return response 

@app.route('/download')
def download() :
    return render_template('download.html')

@app.route('/')
def main() :
    return render_template('main.html')


if __name__ == '__main__' :
    app.run(debug=True)