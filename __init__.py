from flask import Flask, render_template, request, redirect, flash, url_for


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home_page():
	title = "YDL"
	name_of_company = "YouTube Downloader"
	download_location = "YouTube URL"
	if request.method == 'POST':
		
			attempted_url = request.form['url']
			FACILITIES ={"Audio": "1",
					 "Video": "2",
					 "Audio Playlist": "3",
					 "Video Playlist": "4"
					}
			attempted_choice = list(FACILITIES.keys())[list(FACILITIES.values()).index(str(request.form['submit']))]
			user_options = [attempted_url, attempted_choice]
			return redirect(url_for('home_page'))
			#return render_template('index.html', title = user_options)
		
	return render_template('index.html', name_of_company = name_of_company, download_location = download_location, title = title)
	

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
	
	app.run(debug = True)