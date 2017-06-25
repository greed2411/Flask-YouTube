from flask import Flask, render_template, request, redirect, flash, url_for
from ydl import get_media

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home_page():
	title = "YDL"
	name_of_company = "YouTube Downloader"
	download_location = "YouTube URL"
	if request.method == 'POST':
		
			attempted_url = request.form['url']
			CHOICES ={"Audio": 1,
					 "Video": 2,
					 "Audio Playlist": 3,
					 "Video Playlist": 4
					}
			attempted_choice = list(CHOICES.keys())[list(CHOICES.values()).index(int(request.form['submit']))]
			num_choice = CHOICES.get(attempted_choice)
			user_options = [attempted_url, num_choice]
			result = get_media(attempted_url, num_choice)
					
	return render_template('index.html', name_of_company = name_of_company, download_location = download_location, title = title)
	

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html' , title = "404 bud"), 404
	
@app.errorhandler(400) 
def page_not_found(error): 
	return render_template('invalid.html', title = "Invalid URL"), 400

if __name__ == '__main__':
	
	app.run(debug = True)