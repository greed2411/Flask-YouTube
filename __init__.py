from flask import Flask, render_template, request, redirect, flash, url_for, send_file
from ydl import get_media, verify

app = Flask(__name__)
app.secret_key = 'supposed to be a secret'

@app.route('/return-file/')
def return_file():
	flash('Success', 'info')
	return send_file('media\Audio downloads\\attention.mp3', attachment_filename = 'attention.mp3', as_attachment = True)

@app.route('/file-downloads/')
def file_downloads():
	flash('Success')
	return render_template('downloads.html', title="Yay", message = "Sir, it appears the file is ready for download", 
											image_location = url_for('static', filename = 'images/ironman-simpson.jpg'))
	


@app.route('/', methods = ['GET', 'POST'])
def home_page():
	"""
	Displaying homepage
	"""

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
				return redirect(url_for('file_downloads'))
			
			return render_template('error_template.html' , title = "Invalid URL", 
															message = "Are you being intentionally dense? Huh?",
    													   subline = "Invalid URL", 
    													   image_location = url_for('static', filename = 'images/house-simpson.jpg'))


	return render_template('index.html', name_of_company = name_of_company, download_location = download_location, title = title)
	

@app.errorhandler(404)
def page_not_found(error):
    """
	for anyone trying different links or searching for images within the server
    """
    return render_template('error_template.html' , title = "404 bud", 
    												message = "Time to make the chimi-fuckin'-changas. ",
    												subline = "404, not there", 
    												image_location = url_for('static', filename = 'images/deadpool-funny.jpg') ), 404


@app.errorhandler(400) 
def bad_request(error): 
	"""
	For handling situations where the server doesn't know what to do with the browser's request
	"""
	return render_template('error_template.html' , title = "Aaaah ...", 
													message = "나는 이해하지 못한다.",
    												subline = "Yeah, the server couldn't understand what you asked for, probably because you didn't give a choice of download.", 
    												image_location = url_for('static', filename = 'images/simpson-gangam.jpg')), 400


if __name__ == '__main__':
	
	app.run(debug = True)
