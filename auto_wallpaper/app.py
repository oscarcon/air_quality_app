#!/usr/bin/python3 -u
from astral import Astral
from astral import Location
from astral import AstralGeocoder
from datetime import datetime, timezone
import threading
import subprocess
import pytz
import logging
import sys

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s',level=logging.INFO)
# class BackgroundConfig: 
#     @classmethod
#     def run(date_time):
#         pass
def datetime_to_hours(date_time):
    return date_time.hour + date_time.minute/60 + date_time.second/3600
# astral = Astral()
# city = astral['Hanoi']
# print(city.timezone)

location = Location()
location.name = 'Phanthiet'
location.region = 'Middle'
location.latitude = 11
location.longitude = 108
location.timezone = 'Asia/Saigon'
location.elevation = 0
sun = location.sun()

print(sun['dawn'])
print(sun['sunrise'])
print(sun['sunset'])
print(sun['dusk'])
print(sun['noon'])
time_line = {
    'dawn': datetime_to_hours(sun['dawn']),
    'dusk': datetime_to_hours(sun['dusk']),
    'noon': datetime_to_hours(sun['noon']),
} 
time_line.update({
    'before_dawn': time_line['dawn']/2,
    'after_noon': (time_line['dusk'] + time_line['noon'])/2,
    'night': (24 + time_line['dusk'])/2
})
print(time_line)

def set_background(image_path):
    pass

def main():
    current_time = datetime_to_hours(datetime.now())
    if current_time >= 0 and current_time < time_line['before_dawn']:
        interval = time_line['before_dawn'] - current_time
        background = 'file:///home/huy/Pictures/midnight.png'
    elif current_time < time_line['dawn']:
        interval = time_line['dawn'] - current_time
        background = 'file:///home/huy/Pictures/dawn.jpg'
    elif current_time < time_line['noon']:
        interval = time_line['noon'] - current_time
        background = 'file:///home/huy/Pictures/noon.jpg'
    elif current_time < time_line['after_noon']:
        interval = time_line['after_noon'] - current_time
        background = 'file:///home/huy/Pictures/noon.jpg'
    elif current_time < time_line['dusk']:
        interval = time_line['dusk'] - current_time
        background = 'file:///home/huy/Pictures/dusk.jpg'
    elif current_time < time_line['night']:
        interval = time_line['night'] - current_time
        background = 'file:///home/huy/Pictures/moon_night.jpg'
    else:
        interval = 24 - current_time
        background = 'file:///home/huy/Pictures/midnight.png'
    update_command = 'gsettings set org.gnome.desktop.background \
        picture-uri ' + background
    logging.info('Change background to %s' % background)
    sys.stdout.flush()
    subprocess.call(update_command, shell=True)
    threading.Timer(interval*3600, main).start()

if __name__ == '__main__':
    logging.info("Auto Wallpaper Service")
    sys.stdout.flush()
    main()
    






