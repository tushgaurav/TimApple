from PIL import Image, ImageFont, ImageDraw
from datetime import date
import csv
import random


def Certificate(message):
 # get the current date
    today = date.today()
    long_date = today.strftime("%B %d, %Y")

   # fetch random names from the names.csv file
    with open('data/names.csv') as file:
        reader = csv.DictReader(file)
        namelist = list(reader)
        namedict = dict(random.choice(namelist))
        name = namedict['fname'] + " " + namedict['lname']

    # opens the certificate image file
    image = Image.open('images/Tim Apple Bot Certificate.png')

    # initiliase the font and draw
    draw = ImageDraw.Draw(image)
    font_message = ImageFont.truetype('fonts/Poppins-Regular.ttf', 90)
    font_date = ImageFont.truetype('fonts/Poppins-Regular.ttf', 45)
    font_sign = ImageFont.truetype('fonts/Poppins-Regular.ttf', 45)

    # dimentions of the certificate image file
    width, height = image.size

    # set the color
    color = 'rgb(0, 0, 0)'

    # draw the text in the center of the image
    w, h = draw.textsize(message, font=font_message)
    draw.text(((width - w)/2, (height - h)/2),
              message, fill=color, font=font_message)

    # drawing the date
    wd, hd = 1512, 1125
    draw.text((wd, hd), long_date, fill=color, font=font_date)

    # draw the signed by
    ws, hs = 770, hd
    draw.text((ws, hs), name, fill=color, font=font_sign)

    image.save('images/output.png')
