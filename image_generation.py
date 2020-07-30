from PIL import Image, ImageFilter, ImageDraw, ImageFont
# -*- coding: utf-8 -*-

'''
import sys
reload(sys)  
sys.setdefaultencoding('Cp1252')
'''

def generate_and_save_image(name, main_color, color_name, index):
    base = Image.open('base.jpg').convert('RGBA')

    # make a blank image for the text, initialized to transparent text color
    im = Image.new('RGBA', base.size, (255, 255, 255, 0))

    draw = ImageDraw.Draw(im)

    # Draw the squares
    draw.rectangle(((0, 00), (750, 750)), main_color)
    draw.rectangle(((125, 25), (625, 725)), '#ffffff')
    draw.rectangle(((135, 35), (615, 520)), main_color)

    # Texts
    # Brand Text
    brand_fnt = ImageFont.truetype('Roboto-Medium.ttf', 70)
    brand = 'Filsiz Boya'
    draw.text((140, 520), brand, 'black', font=brand_fnt)

    # Registered Symbol
    brand_length = brand_fnt.getsize(brand)
    registered_fnt = ImageFont.truetype('Roboto-Medium.ttf', 30)
    draw.text((140 + brand_length[0], 530), u'\u00ae', 'black', font=registered_fnt)

    # Name and color name
    name_fnt = ImageFont.truetype('Roboto-Medium.ttf', 40)
    draw.text((140, 520 + brand_length[1]), name.decode('utf-8') + ' ' + color_name.title(), 'black', font=name_fnt)

    # Color
    name_length = name_fnt.getsize(name)
    color_fnt = ImageFont.truetype('Roboto-Medium.ttf', 30)
    draw.text((140, 520 + brand_length[1] + name_length[1] + 40), main_color, main_color, font=color_fnt)

    out = Image.alpha_composite(base, im)

    out.save('output/' + str(index) + '_' + name + '.png')

'''
main_color = '#FF0000'
name = u'DO\u011fu'
color_name = 'sarisi'
index = 0

generate_and_save_image(name, main_color, color_name, index)
'''