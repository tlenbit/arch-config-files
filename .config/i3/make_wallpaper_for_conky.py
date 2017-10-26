#!/home/cristo/anaconda3/bin/python3

from PIL import Image
import sys
import numpy as np


# koefs for transparency
conky_koef = 0.7

# rgb of conky background
c_r = 7
c_g = 54
c_b = 66

def process_region(region, box, conky_koef):
  for i in range(0, box[2]-box[0]):
    for j in range(0, box[3]-box[1]):
      r,g,b = region.getpixel((i, j))
      wallpaper_koef = 1 - conky_koef
      r = int(c_r * conky_koef + r * wallpaper_koef)
      g = int(c_g * conky_koef + g * wallpaper_koef)
      b = int(c_b * conky_koef + b * wallpaper_koef)
      region.putpixel((i,j),(r,g,b))

def calculate_brightness(region, box):
  size = float((box[2]-box[0])*(box[3]-box[1]))
  pixels_sum = 0.0
  for i in range(0, box[2]-box[0]):
    for j in range(0, box[3]-box[1]):
      pixels_sum += sum(region.getpixel((i,j)))
  return pixels_sum/(size*3)

def calculate_std(region, box):
  bri_list = []
  for i in range(0, box[2]-box[0]):
    for j in range(0, box[3]-box[1]):
      bri = sum(region.getpixel((i,j)))/(3*255)
      bri_list.append(bri)
  return np.std(bri_list)

i = 1
l = len(sys.argv) - 1

# left upper right lower
boxes = [(30, 70, 440, 960), (1630, 800, 1850, 960)]
# (1500, 110, 1835, 250)


def change_pics():
  
  i = 1
  l = len(sys.argv) - 1

  for image_path in sys.argv[1:]:
    print(str(i) + ' of ' + str(l) + ' ...')
    try:
      im = Image.open(image_path)
      for box in boxes:
        region = im.crop(box)
        # 0 - 255
        bri = calculate_brightness(region, box)
        # 0 - 1.0
        bri = float(bri)/255
        print('bri ' + str(bri))
        std = calculate_std(region, box)
        print('std ' + str(std))
        conky_koef = (bri*(4)+std*(10))/5
        print('conky_koef ' + str(conky_koef))
        process_region(region, box, conky_koef)
        im.paste(region, box)
      im.save('/home/cristo/.config/i3/wallpapers_for_conky/' + image_path.split('/')[-1] )
    except Exception as e:
      print('Something gone wrong with ' + image_path + '\n' + str(e) + '\n')
  
    i += 1

change_pics()
