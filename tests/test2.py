from PIL import Image
from glob import glob
from io import BytesIO
import base64


'''
filenames = glob('images/phone*.png')
number_of_images = len(filenames)
width, height = Image.open(filenames[0]).size
total_height = height*number_of_images
stacked = Image.new('RGBA', (width, total_height))

for index,filename in enumerate(filenames):
    image = Image.open(filename)
    stacked.paste(image,(0,index*height))
stacked.save('stacked.png')
'''


'''
for digit in range(0,10):
    filename = 'images/{}.png'.format(digit)
    image = Image.open(filename).convert('LA')
    width, height = image.size
    histogram = image.histogram()
    print('{} ----> {},{}'.format(digit,histogram[0],histogram[-1]))
'''



base64_image = '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'
image = Image.open(BytesIO(base64.b64decode(base64_image))).convert('LA')
#image = Image.open('images/phone9.png')
left_margins = (5,39,63,86,122,146,169,207,231,268,292)
DIGITS_BY_HIST = {358: '0', 162: '1',331: '2', 328: '3', 285: '4', 336: '5', 396: '6',216: '7', 403: '8', 383: '9'}
digits=[]
for index, left_margin in enumerate(left_margins, start=1):
    box = (left_margin, 13, left_margin+21, 13+31)
    digit = image.crop(box)

    #digit.show()
    digit.save('cifri/'+str(index)+'.png')

    characteristic = digit.histogram()[0]
    digits.append(DIGITS_BY_HIST.get(characteristic, 'x'))
print( ''.join(digits))


