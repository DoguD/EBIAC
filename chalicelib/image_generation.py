
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import sys

base = Image.open('base.jpg').convert('RGBA')

# make a blank image for the text, initialized to transparent text color
im = Image.new('RGBA', base.size, (255,255,255,0))

# get a drawing context
draw = ImageDraw.Draw(im)
main_color = '#ff0000'
name = 'Dogu'
draw.rectangle(((0, 00), (757, 757)), main_color)
draw.rectangle(((120, 20), (620, 720)), '#ffffff')
draw.rectangle(((130, 30), (600, 500)), main_color)

fnt = ImageFont.truetype('Roboto-Medium.ttf', 80)
draw.text((140, 520), 'PANTONE'+u'\u00ae', 'black', font=fnt)
draw.text((140, 620), name, 'black', font=fnt)


'''
# draw text, half opacity
d.text((10,10), "Hello", fill=(255,255,255,128))
# draw text, full opacity
d.text((10,60), "World", fill=(255,255,255,255))
'''

out = Image.alpha_composite(base, im)

out.save('test.png')
