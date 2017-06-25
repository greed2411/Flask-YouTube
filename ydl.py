import subprocess
import os
import urllib.request
import urllib.error
import sys
import bs4


"""
	YouTube Downloader used to download the best quality 
	audio, 
	video,
	Playlist of audio files,
	Playlist of video files
	from a URL belonging to https://www.youtube.com/
	
	Started working on : 21-06-2017
	
"""

def internet_on():
	"""
		Checking whether connected to the internet 
		if not connected to internet but connected to wifi, not yet logged in, 
		returns a '200' code for trying to fetch results (wifi defualt login page)
		URLError if there is no internet or default wifi redirecting, AttributeError for handling 'Nonetype' object (response) in the above
	"""
	try:
		
		response = urllib.request.urlopen('http://google.com', timeout=1)
		soup = bs4.BeautifulSoup(response, "html.parser") 						 
		if soup.title.text == 'Google': 								  
		
			return True

	except (urllib.request.URLError, AttributeError) : 
		
		return False 	

def verify(url):
	"""
		Verifying URL, whether it's a URL, whether that URL belongs to YouTube or not
	"""
	
	checking_internet = internet_on()
	
	if checking_internet == True:
		
		try :
			
			separation = url.split('/')  
			
			if separation[2] == 'www.youtube.com' or separation[2] == 'youtu.be':
				
				"""
					Not checking whether URL is a playlist URL or not because of 
					YouTube's new User's 'My Mix' of songs, which don't have a 'playlist' in their URL
				"""
				
				#print('URL belongs to YouTube')		
				return True
			
			else:
				
				return "Not a YouTube URL" # test case : 'https://mail.google.com/mail/u/0/#inbox'
		
		except Exception:
			
			return 'Oops , Not a valid URL' # test case : 'affdfsffasf'
	
	else:
		
		return "Hmmm... you're not connected to the Internet"


def get_media(url, choice):
	
	try:
		
		check = verify(url)
		if check == True:
			
			if choice == 1:
				
				subprocess.call('youtube-dl -f 251 -o "/media/Audio downloads from youtube-dl/%(title)s.%(ext)s" -q --no-playlist --extract-audio --audio-format mp3 --no-warnings "{url}"'.format(url=url), shell=True)
				#print('\n\nThe process is over and your file is probably residing in ' + os.getcwd() + '\\media\Audio downloads from youtube-dl' )
			
			elif choice == 2:
				
				subprocess.call('youtube-dl  -o "/media/Video downloads from youtube-dl/%(title)s.%(ext)s" -q --no-playlist --no-warnings "{url}"'.format(url=url), shell=True)
				#print('\n\nThe process is over and your file is probably residing in ' + os.getcwd() + '\\media\Video downloads from youtube-dl' )
			
			elif choice == 3:
				
				subprocess.call('youtube-dl -i -o "%/media/(playlist)s/%(playlist_index)s.%(title)s.%(ext)s" --yes-playlist --extract-audio --audio-format mp3 --no-warnings "{url}"'.format(url=url), shell=True)
				#print('\n\nThe process is over and currently residing in the current working directgory with the name of the folder same as that of playlist!')
			
			elif choice == 4:
				
				subprocess.call('youtube-dl -i -o "%/media/(playlist)s/%(playlist_index)s.%(title)s.%(ext)s" --yes-playlist --newline --no-warnings "{url}"'.format(url=url), shell=True)
				#print('\n\nThe process is over and currently residing in the current working directgory with the name of the folder same as that of playlist!')
			return "Success!!"
		
		elif check == "Not a YouTube URL" :
			
			return "Not a YouTube URL"
		
		elif check == 'Oops , Not a valid URL' :
		
			return 'Oops , Not a valid URL'
		
				
			
	except Exception as e: #for any other unknown errors,  used it to get the other exceptions mentioned above
		
		return e

url = ""
choice = 1		
get_media(url, choice)
	


