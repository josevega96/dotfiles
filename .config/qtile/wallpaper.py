##
#download daily bing wallpaper based on https://github.com/mammuth/bing-wallpaper/blob/master/bing_wallpaper.py
##


import datetime
import os 
import errno
import socket
from shutil import copy
from urllib.request import urlopen,urlretrieve
from xml.dom import minidom
import sys

home=os.path.expanduser('~')
save_dir=home+'/Pictures/wallpaper'



def create_dir():
    try:
         os.makedirs(save_dir)
    except OSError as Exception:
        if Exception.errno != errno.EEXIST:
            raise


def download_wallpaper(idx=0):

    day=datetime.datetime.now()
    yesterday= datetime.datetime.now() - datetime.timedelta(days=1)
    print(yesterday.strftime('%d-%m-%Y'))
    pic_path = save_dir + day.strftime('/wall_%d-%m-%Y') + '.png'
    yesterday_pic= save_dir + yesterday.strftime('/wall_%d-%m-%Y')+'.png'
   
   
    try:
        #get url for the xml file
        usock = urlopen(''.join(['http://www.bing.com/HPImageArchive.aspx?format=xml&idx=',
                                 str(idx), '&n=1&mkt=en-US']))  # ru-RU, because they always have 1920x1200 resolution
    except socket.error as msg:
        if os.path.isfile(yesterday_pic):
            return yesterday_pic
        else:
            return pic_path
        
    try:
        #parse the xml file
        xmldoc=minidom.parse(usock)
    except Exception as e:
        print('Error while processing XML index #', idx, e)
        return
    for element in xmldoc.getElementsByTagName('url'):
        url='http://www.bing.com' + element.firstChild.nodeValue
        if os.path.isdir(save_dir):
            print('Wallpapers directory found')
        else:
            create_dir()

    if(int(day.strftime('%H'))<=6):
        return yesterday_pic

    if os.path.isfile(pic_path):
        return pic_path

    urlretrieve(url.replace('_1366x768', '_1920x1200'), pic_path)
    try:
        os.remove(yesterday_pic)
    except OSError as Exception:
        if Exception.errno != errno.EEXIST:
            print('file not found')

    # copy to lightdm backgrounds folder
    try:
        copy(pic_path,'/usr/share/backgrounds/back.jpg')
    except  IOError as e:
        print('Unable to copy file')

    return pic_path

    

if __name__ == "__main__":
   file_dir= download_wallpaper()
   print (file_dir)
          