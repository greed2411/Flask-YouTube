from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
	title = "YDL"
	name_of_company = "YouTube Downloader"
	download_location = "YouTube URL"
	return render_template('index.html', name_of_company = name_of_company, download_location = download_location, title = title)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
	
	app.run(debug = True)