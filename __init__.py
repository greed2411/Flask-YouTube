from flask import Flask, render_template, request, redirect, flash, url_for, send_file, session
from ydl import get_media, verify, fetch_name
from zipper import zipping

app = Flask(__name__)
app.secret_key = 'supposed to be a secret'

@app.route('/return-file/')
def return_file():
	
	num_choice = session.get('choice')
	filename = session.get('filename')

	if num_choice == 1 :
		filename_formatted = filename + '.mp3'
		location = 'media\Audio downloads\{}.mp3'.format(session.get('id'))
	
	if num_choice == 2 :
		filename_formatted = filename + '.mp4'
		location = 'media\Video downloads\{}.mp4'.format(session.get('id'))
	
	if num_choice == 3 or num_choice == 4 :
		filename_formatted = filename + '.zip'
		location = 'media\{}.zip'.format(session.get('id'))
	
	return send_file(location, attachment_filename = filename_formatted, as_attachment = True)

@app.route('/file-downloads/')
def file_downloads():
	
	url = session.get('url')
	filename = fetch_name(url)
	session['filename'] = filename
	num_choice = session.get('choice')
	location = 'media\{}'.format(session.get('id'))
	id_generated = session.get('id')

	if num_choice == 3 or num_choice ==4:
		zipping(id_generated, location)

	flash('Successfully downloaded {}'.format(filename))
	return render_template('downloads.html', title="Yay", message = "Sir, it appears the file is ready for download.", 
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

				result_id = get_media(attempted_url, num_choice)
				session['url'] = attempted_url
				session['id'] = result_id
				session['choice'] = num_choice
				#return render_template('index.html', title = result_id)
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
