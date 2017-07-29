# Flask-YouTube

Locally deployed Flask App (synchronous)  for downloading audio files, video files, playlists of both video and audio, from a valid YouTube URL at the best quality out there.

Tested and developed on ***Windows7 32-bit SP1, Ubuntu GNOME 16.04*** LTS with **Anaconda's Python distro, 3.6.1**

#### Command Line Programs used

  * `youtube-dl` - Used to download the file from the internet.
  * `ffmpeg` - Used for postprocess data, i.e., to convert file from .webm to .mp3 format.
  
#### Dependencies 

  * [flask](http://flask.pocoo.org/) - A micro framework for backend.
  * [bs4](https://www.crummy.com/software/BeautifulSoup/) - For parsing the html document.
  * [lxml](http://lxml.de/) - helps BeautifulSoup while parsing, instead of the defualt slow html parser.
  
  if you don't have them, 
  
  ```pip_installation
  pip install flask bs4 lxml
  ```
  for more instructions on how to install `youtube-dl` and `ffmpeg` on your machine visit the [YDL](https://github.com/Jaiimmortal/YDL#steps-to-follow-for-installing-dependencies) repository.
### Screenshots

#### Homepage on Ubuntu

![Homepage](/../master/Flask-YouTube-Materialize&Ubuntu/homepage-ubuntu_materialize.png?raw=true "homepage")

#### Homepage on Windows 7

![Homepage](/../master/Screenshots/Flask-YouTube-homepage-master.png?raw=true "homepage")

![Homepage](/../master/Screenshots/Flask-YouTube-homepage.png?raw=true "homepage")

### Output page

![Output](/../master/Screenshots/output.JPG?raw=true "file-downloads")


#### Responsive Design
![mobile version](/../master/Screenshots/mobile.JPG?raw=true "homepage")

![responsive-design](/../master/Screenshots/responsive-design.JPG?raw=true "homepage")


#### Errors
![Page not found](/../master/Screenshots/error-jinja-templates.JPG?raw=true "homepage")
