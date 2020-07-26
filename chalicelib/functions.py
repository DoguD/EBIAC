def name_to_color_code(name):
    seed = 1
    limit = 255 * 255 * 255
    for char in name:
        seed *= ord(char)
    hex_code = hex(seed % limit)
    return hex_code


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
