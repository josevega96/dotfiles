###
#grab colors from pywal
###

import json
import os
import pywal
from wallpaper import download_wallpaper

home = os.path.expanduser('~')

pic_dir=download_wallpaper()

image=pywal.image.get(pic_dir)

pallete=pywal.colors.get(image)

pywal.export.every(pallete,home+'/.cache/wal')

pywal.wallpaper.change(image)

pywal.sequences.send(pallete)

with open (home+'/.cache/wal/colors.json','r') as string:
    my_dict=json.load(string)

colors=[[str(my_dict['colors']['color0'])],
    [str(my_dict['colors']['color1'])],
    [str(my_dict['colors']['color2'])],
    [str(my_dict['colors']['color3'])],
    [str(my_dict['colors']['color4'])],
    [str(my_dict['colors']['color5'])],
    [str(my_dict['colors']['color6'])],
    [str(my_dict['colors']['color7'])],
    [str(my_dict['colors']['color8'])],
    [str(my_dict['colors']['color9'])],
    [str(my_dict['colors']['color10'])],
    [str(my_dict['colors']['color11'])],
    [str(my_dict['colors']['color12'])],
    [str(my_dict['colors']['color13'])],
    [str(my_dict['colors']['color14'])],
    [str(my_dict['colors']['color15'])]]

print(colors)

