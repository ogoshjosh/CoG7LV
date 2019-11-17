#!/usr/bin/env python

# Imports
import os
import glob
from pydub import AudioSegment
import logging

# Media Directory Pat
media_dir = r'/Users/joshua/Desktop/Audio Files/{}'.format(media_type)  # Path where the media is located
extension_list = ('*.mp4', '*.flv', '*.m4a')
media_type = ('video', 'audio', 'music')


# Audio Converter: converts audio in audio directory path
os.chdir(media_dir)
for extension in extension_list:
    for audio in glob.glob(extension):
        mp3_filename = os.path.splitext(os.path.basename(audio))[0] + '.mp3'
        AudioSegment.from_file(audio).export(mp3_filename, format='mp3')

os.chdir(media_dir)
for media in media_type:
    for video in glob.glob(type):
        media_type = os.path.splitext(os.path.basename(media)

# Built-in Debugging to handle conversion issues
l = logging.getLogger("pydub.converter")
l.setLevel(logging.DEBUG)
l.addHandler(logging.StreamHandler())
