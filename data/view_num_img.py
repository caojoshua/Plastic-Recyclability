
recyclable = ["detergent", "hdpe_bottle", "imagenet_bottled_water", "imagenet_lotion_bottle", "plastic_milk_jug", 
				"plastic_shampoo_bottle", "plastic_soap_bottle", "plastic_water_bottle", "scrapsort_github", "thung_recyclable"]
non_recyclable = ["bubblewrap", "frozen_food_bag", "packing_foam", "packing_peanuts", "plastic_bag", "plastic_cd", "plastic_coffee_lid",
					"plastic_cutlery", "plastic_shopping_bag", "plastic_straw", "plastic_tupperware", "plastic_yogurt_container", 
					"potato_chip_bag", "pvc_pipe", "squeeze_bottle", "stadium_cups"]

import os

r_total = 0
nr_total = 0
for dir in os.listdir("images"):
	i = 0
	for img in os.listdir("images/" + dir):
		i += 1
	print(dir, ": ", i)
	if dir in recyclable:
		r_total += i
	elif dir in non_recyclable:
		nr_total += i
	else:
		print(dir, " not included in dataset")
print("recyclable total:", r_total)
print("non recyclable total:", nr_total)
print("total:", r_total + nr_total)

