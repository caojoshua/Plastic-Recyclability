
#this puts images into a csv file
#use img_to_bin.py instead, I/O for binary is way faster

recyclable = ["imagenet_lotion_bottle", "plastic_milk_jug", "plastic_shampoo_bottle", "plastic_soap_bottle", "plastic_water_bottle",
				"scrapsort_github", "thung_recyclable"]
non_recyclable = ["bubblewrap", "frozen_food_bag", "packing_foam", "packing_peanut", "plastic_bag", "plastic_cd", "plastic_coffee_lid"
					"plastic_cutlery", "plastic_shopping_bag", "plastic_straw", "plastic_tupperware", "plastic_yogurt_container", 
					"potato_chop_bag", "pvc_pipe", "squeeze_bottle", "stadium_cups"]

import os
from PIL import Image

IMAGE_SIZE = 128

out_file = open("data.csv", "w")
error_file = open("errors.txt", "w")

for dir in os.listdir("images"):
	print("working on " + dir)
	for file in os.listdir("images/" + dir):
		try:
			img = Image.open("images/" + dir + "/" + file)
			img = img.resize((IMAGE_SIZE, IMAGE_SIZE))
			img = img.convert('RGB')
			
			s = ""
			for i in range(IMAGE_SIZE):
				for j in range(IMAGE_SIZE):
					pixel = img.getpixel((i, j))
					s += str(pixel[0]) + "," + str(pixel[1]) + "," + str(pixel[2]) + ","
			s = s.rstrip(",") + "\n"
			out_file.write(s)
		except Exception as e:
			print("error while processing " + "images/" + dir + "/" + file)
			error_file.write("images/" + dir + "/" + file + "\n")
		
out_file.close()
	