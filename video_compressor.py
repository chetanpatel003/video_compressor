import subprocess
import os
from ffmpy import FFmpeg
from time import sleep
import shutil

# input the directory, from where to pick the video files
input_dir = input()

# input the directory, where to save compressed files
output_dir = input()

for root, dirs ,files in os.walk(input_dir):
    for filename in files:
        input_name = root + '/' + filename
        inp={input_name:None}
        output_name = output_dir + '/' + filename
        outp = {output_name:'-vcodec h264 -b:v 4000k -acodec mp2'}
        ff = FFmpeg(inputs=inp,outputs=outp)
        
        # provide the directory
        os.chdir('user_dir')
        subprocess.run(ff.cmd , shell=True)
        # to delete the org file
        os.remove(input_name)


