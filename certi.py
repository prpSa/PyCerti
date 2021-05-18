from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
df = pd.read_csv('list1.csv')
font = ImageFont.truetype('arial.ttf',60)
for index,j in df.iterrows():
    img = Image.open('certificate.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(850,650),text='{}'.format(j['Name']),fill=(0,0,0),font=font)
    img.save('pictures/{}.jpg'.format(j['Name']))
