import youtube_dl
import os
import sys
import shutil

# os.chdir(sys.argv[1])

print(os.getcwd())

output_folder = "musics"    # temporary work folder

class MyLogger(object):
    def debug(self, msg):
        print(msg)

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
	'format': 'bestaudio/best',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
	'logger': MyLogger(),
	'progress_hooks': [my_hook],
	'download_archive': 'archive.txt',
	'outtmpl': output_folder + '/%(title)s.%(ext)s',
    'ffmpeg-location': os.path.dirname(os.path.realpath(__file__)) + "FFmpeg",
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	ydl.download(['https://www.youtube.com/playlist?list=PLhcRZbMC1DBerCC_T_09x3MZfh1mmS7aY'])
	

files = os.listdir(output_folder)
# file_destination = "D:\\Users\\Sofa\\Desktop\\musiques\\Youtube\\"  # final destination of music files
file_destination = "musics/"

for f in files:
	if '.mp3' in f:
		shutil.move(output_folder + f, file_destination)
