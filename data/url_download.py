
import requests
import sys
import os

# file_name = sys.argv[1]
urls = []

for file_name in sys.argv[1:]:
	print("downloading ", file_name, " images")
	f_in = open("urls/" + file_name + ".txt", "r")
	i = 0
	for url in f_in:
		if i% 50 == 0:
			print("downloading image ", i)
		url = url.rstrip()
		
		try:
			if not os.path.exists("images/" + file_name):
				os.makedirs("images/" + file_name)
			f_out = open("images/" + file_name + "/" + file_name + str(i) + ".jpg", "wb")
			f_out.write(requests.get(url).content)
			f_out.close()
		except Exception as e:
			print("Error in file ", i)
			print(e)
		i += 1