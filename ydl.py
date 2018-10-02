import subprocess
import requests
from bs4 import BeautifulSoup
from fetcher import id_generator

"""
	YouTube Downloader used to download the best quality
	audio,
	video,
	Playlist of audio files,
	Playlist of video files
	from a URL belonging to https://www.youtube.com/

	Started working on : 21-06-2017

"""


def fetch_name(url):
    """ To get the title of the YouTube Page """
    youtube_page = requests.get(url)
    bsObj = BeautifulSoup(youtube_page.text, "html.parser")
    return bsObj.title.text


def verify(url):
    """
	To check whether `url` belongs to YouTube, if yes returns True
	else False
	"""
    if "www.youtube.com" in url or "youtu.be" in url:
        return True
    return False


def get_media(url, choice):
    """
	Uses `choice`, to download the required content from `url`
	"""
    id_generated = id_generator()
    try:

        if url == "":

            pass

        else:

            if choice == 1:

                subprocess.call(
                    'youtube-dl -f 251 -o "media/Audio downloads/{id_generated}.%(ext)s" -q --no-playlist --extract-audio --audio-format mp3 --no-warnings "{url}"'.format(
                        id_generated=id_generated, url=url
                    ),
                    shell=True,
                )
                return id_generated

            elif choice == 2:

                subprocess.call(
                    'youtube-dl -f 22 -o "media/Video downloads/{id_generated}.%(ext)s" -q --no-playlist --no-warnings "{url}"'.format(
                        id_generated=id_generated, url=url
                    ),
                    shell=True,
                )
                return id_generated

            elif choice == 3:

                subprocess.call(
                    'youtube-dl -i -o "media/{id_generated}/%(playlist_index)s.%(title)s.%(ext)s" --yes-playlist --extract-audio --audio-format mp3 --no-warnings "{url}"'.format(
                        id_generated=id_generated, url=url
                    ),
                    shell=True,
                )
                return id_generated

            elif choice == 4:
                return id_generated

                subprocess.call(
                    'youtube-dl -i -o "media/{id_generated}/%(playlist_index)s.%(title)s.%(ext)s" --yes-playlist --newline --no-warnings "{url}"'.format(
                        id_generated=id_generated, url=url
                    ),
                    shell=True,
                )

    except Exception as e:  # for any other unknown errors,  used it to get the other exceptions mentioned above, while debugging used to print `e`

        return e


if __name__ == "___main__":

    print("This is a borrowed script")

else:
    url = ""
    choice = 1
    verify(url)
    get_media(url, choice)

