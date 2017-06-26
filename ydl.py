import subprocess

"""
	YouTube Downloader used to download the best quality 
	audio, 
	video,
	Playlist of audio files,
	Playlist of video files
	from a URL belonging to https://www.youtube.com/
	
	Started working on : 21-06-2017
	
"""
def verify(url):

	if 'www.youtube.com' in url or 'youtu.be' in url :
		return True
	return False

def get_media(url, choice):
	
	try:
				
		if choice == 1:
				
			subprocess.call('youtube-dl -f 251 -o "/media/Audio downloads/%(title)s.%(ext)s" -q --no-playlist --extract-audio --audio-format mp3 --no-warnings "{url}"'.format(url=url), shell=True)
						
		elif choice == 2:
				
			subprocess.call('youtube-dl  -o "/media/Video downloads/%(title)s.%(ext)s" -q --no-playlist --no-warnings "{url}"'.format(url=url), shell=True)
						
		elif choice == 3:
				
			subprocess.call('youtube-dl -i -o "%/media/Audio Playlists/(playlist)s/%(playlist_index)s.%(title)s.%(ext)s" --yes-playlist --extract-audio --audio-format mp3 --no-warnings "{url}"'.format(url=url), shell=True)
						
		elif choice == 4:
				
			subprocess.call('youtube-dl -i -o "%/media/Video Playlists/(playlist)s/%(playlist_index)s.%(title)s.%(ext)s" --yes-playlist --newline --no-warnings "{url}"'.format(url=url), shell=True)		
					
	except Exception as e: #for any other unknown errors,  used it to get the other exceptions mentioned above
		
		return e

url = ""
choice = 1
verify(url)		
get_media(url, choice)
	


