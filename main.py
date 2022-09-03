import os, time
try:
	from youtube_dl import YoutubeDL as youtube
except ModuleNotFoundError:
	os.system("pip install youtube_dl")
def clear_system():
	if os.name == 'nt':
		os.system("cls")
	elif os.name == 'posix':
		os.system("clear")
def download(url):
	info = youtube().extract_info(
		url = url,
		download = False
	)
	with youtube({
		'format': 'bestaudio/best',
		'keepvideo': False,
		'outtmpl': "{}.mp3".format(info['title'])
	}) as ready_to:
		ready_to.download([info['webpage_url']])

banner = """
	Youtube mp3 converter
	Source: https://github.com/meicookies/ytconverter

	Coded by ./meicookies
"""

while True:
	clear_system()
	print(banner)
	file = input("Input file: ")
	try:
		file = open(file, 'r')
		for url in file.readlines():
			download(url)
	except FileNotFoundError:
		print("{} file not found". format(file))
		time.sleep(2)
		clear_system()
