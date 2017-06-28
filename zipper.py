import shutil

def zipping(id_generated, location):
	""" To make zip file out of directory """
	if id_generated == "ABCDEF" or location == "media\\temporary" :
		pass
	
	else:
		shutil.make_archive(id_generated, 'zip', location)
		moving_zip_to = "media\\"
		moving_zip_from = "{id_generated}.zip".format(id_generated=id_generated)
		shutil.move(moving_zip_from, moving_zip_to)

if __name__ == '__main__':
	
	print("This script is supposed to be borrowed.")

else :

	location = "media\\temporary"
	id_generated = "ABCDEF"
	zipping(id_generated, location)