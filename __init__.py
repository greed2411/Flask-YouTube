from flask import Flask, render_template, request, redirect, flash, url_for
from ydl import get_media, verify

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

			if verify(attempted_url) :

				result = get_media(attempted_url, num_choice)
				return redirect(url_for('home_page'))
			
			return render_template('error_template.html' , title = "Invalid URL", 
															message = "Invalid URL",
    													   subline = "Welp :|", 
    													   image_location = url_for('static', filename = 'images/house-simpson.jpg'))


	return render_template('index.html', name_of_company = name_of_company, download_location = download_location, title = title)
	

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_template.html' , title = "404 bud", 
    												message = "Page not found or doesn't exist",
    												subline = "Welp :|", 
    												image_location = url_for('static', filename = 'images/queen-band-simpson.jpg') ), 404
	
@app.errorhandler(400) 
def bad_request(error): 
	return render_template('error_template.html' , title = "Aaaah ...", 
													message = "We don't know what happened",
    												subline = "Probably because you didn't give a choice of download and/or a valid URL", 
    												image_location = url_for('static', filename = 'images/gangam-style-simpson.jpg')), 400

if __name__ == '__main__':
	
	app.run(debug = True)