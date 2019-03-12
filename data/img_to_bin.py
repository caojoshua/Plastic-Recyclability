
recyclable = ["detergent", "hdpe_bottle", "imagenet_bottled_water", "imagenet_lotion_bottle", "plastic_milk_jug", 
				"plastic_shampoo_bottle", "plastic_soap_bottle", "plastic_water_bottle", "scrapsort_github", "thung_recyclable"]
non_recyclable = ["bubblewrap", "frozen_food_bag", "packing_foam", "packing_peanuts", "plastic_bag", "plastic_cd", "plastic_coffee_lid",
					"plastic_cutlery", "plastic_shopping_bag", "plastic_straw", "plastic_tupperware", "plastic_yogurt_container", 
					"potato_chip_bag", "pvc_pipe", "squeeze_bottle", "stadium_cups"]

import os
from PIL import Image

IMAGE_SIZE = 128
BATCH_SIZE = 1000

inputs = None
labels = open("batches/labels.bin", "wb")
error_file = open("errors.txt", "w")

zero = 0
one = 1

i = 0

def write_image(path):
	img = Image.open(path)
	img = img.resize((IMAGE_SIZE, IMAGE_SIZE))
	img = img.convert('RGB')
	inputs.write(img.tobytes())
	
for dir in os.listdir("images"):
	print("working on " + dir)
	for file in os.listdir("images/" + dir):
		try:
			#create a new batch every BATCH_SIZE
			if i % BATCH_SIZE == 0:
				if inputs is not None:
					inputs.close()
				batch_num = str(i // BATCH_SIZE)
				print("creating batch", batch_num)
				inputs = open("batches/batch" + batch_num + ".bin", "wb")
			#write image and its corresponding label
			if dir in recyclable:
				write_image("images/" + dir + "/" + file)
				labels.write(zero.to_bytes(1, byteorder='big'))
			elif dir in non_recyclable:
				write_image("images/" + dir + "/" + file)
				labels.write(one.to_bytes(1, byteorder='big'))
			else:
				raise Exception(dir + " not in recyclable or non-recyclable")
		except Exception as e:
			print("error while processing " + "images/" + dir + "/" + file)
			print(e)
			error_file.write("images/" + dir + "/" + file + "\n")
		i += 1
		
inputs.close()
labels.close()
error_file.close()
	