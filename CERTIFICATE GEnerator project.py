from PIL import Image,ImageDraw,ImageFont
import pandas as pd
df = pd.read_csv("student list1.csv")
for index,j in df.iterrows():
    img=Image.open('CERTIFICATE  TEMPLATE.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(550,730),text='{}'.format(j['NAME']),fill=(0,137,209),font=ImageFont.truetype('arial.ttf',100))
    draw.text(xy=(550,990),text='{}'.format(j['PROJECT NAME']),fill=(0,0,102),font=ImageFont.truetype('arial.ttf',75))
    draw.text(xy=(370,1220),text='{}'.format(j['MENTOR NAME']),fill=(102,0,51),font=ImageFont.truetype('arial.ttf',30))
    draw.text(xy=(860,1200),text='{}'.format(j['DATE']),fill=(102,0,51),font=ImageFont.truetype('arial.ttf',75))
    draw.text(xy=(970,1340),text='{}'.format(j['CERTIFICATE NUMBER']),fill=(0,137,209),font=ImageFont.truetype('arial.ttf',75))
    img.save('CERTIFICATES\{}.jpg'.format(j['NAME']))