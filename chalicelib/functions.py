def name_to_color_code(name):
    seed = 1
    limit = 255 * 255 * 255
    for char in name:
        seed *= ord(char)
    hex_code = hex(seed % limit)
    return hex_code
