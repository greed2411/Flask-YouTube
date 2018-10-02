# Flask-YouTube

Locally deployed Flask App (synchronous)  for downloading audio files, video files, playlists of both video and audio, from a valid YouTube URL at the best quality out there.

Tested and developed on ***Ubuntu GNOME 18.04*** LTS with **Anaconda's Python distro, 3.6.5**

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

![Homepage](/../master/homepage-ubuntu_materialize.png?raw=true "homepage")


