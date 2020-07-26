from PIL import Image, ImageFilter, ImageDraw, ImageFont

base = Image.open('base.jpg').convert('RGBA')

# make a blank image for the text, initialized to transparent text color
im = Image.new('RGBA', base.size, (255,255,255,0))

# get a drawing context
draw = ImageDraw.Draw(im)
main_color = '#ff0000'
name = 'Do'+u'\u011f'+'u'

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
draw.text((140+brand_length[0], 530), u'\u00ae', 'black', font=registered_fnt)

# Name and color
name_fnt = ImageFont.truetype('Roboto-Medium.ttf', 40)
draw.text((140, 520+brand_length[1]), name, 'black', font=name_fnt)


'''
# draw text, half opacity
d.text((10,10), "Hello", fill=(255,255,255,128))
# draw text, full opacity
d.text((10,60), "World", fill=(255,255,255,255))
'''

out = Image.alpha_composite(base, im)

out.save('test.png')
