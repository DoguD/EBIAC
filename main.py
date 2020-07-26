# -*- coding: utf-8 -*-
import csv
import functions
import color_namer
import image_generation
from name_list_manipulator import *

# Generate and open file
generate_source_file(100, 0)

name_list = open('src/names/ordered_mixed_name_list.csv')
name_list = csv.reader(name_list)

# Create a list consisting name, color and color name
names = []
error_counter = 0
for name in name_list:
    try:
        color = functions.name_to_color_code(name[0])
        actual_name, closest_name = color_namer.get_colour_name(tuple(int(color[i:i+2], 16) for i in (0, 2, 4)))
        if actual_name is None:
            color_name = closest_name
        else:
            color_name = actual_name
        names.append((name[0], '#'+color, color_name))
    except:
        error_counter += 1

print ('Color and color name generation errors occured:', error_counter)

# Generate images
index = 0
for element in names:
    image_generation.generate_and_save_image(element[0],element[1], element[2], index)
    index += 1
