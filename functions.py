# -*- coding: utf-8 -*-
def name_to_color_code(name):
    seed = 1
    limit = 254 * 254 * 254
    for char in name:
        seed *= ord(char)
    hex_code = hex(seed % limit)[2:]
    if len(hex_code) > 6:
        hex_code = hex_code[:6]
    #hex_code = '#' + hex_code
    return hex_code.upper()


def get_index():
    f = open("./index.txt", "r")
    index = int(f.read())
    return index


def update_index():
    f = open("./index.txt", "r")
    index = int(f.read()) + 1
    f.close()
    f = open("./index.txt", "w")
    f.write(str(index))
