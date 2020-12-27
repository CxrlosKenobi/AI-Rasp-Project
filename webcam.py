# Usar picamera
import subprocess
import datetime
import time
import os
from subprocess import Popen, PIPE

homeDIr = '/home/pi/AI';
destDir = '/home/pi/AI/uwphotos/';

count = 0;
limit = 2;

while (count < limit):
    outImg = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S');
    outImg = 'test_' + outImg + '.jpg';
    camIn = ['fswebcam', '-r', '640x480', '-d', '/dev/video0', '-i', '0', outImg];
    mvPic = ['mv', (homeDir + outImg), (destDir + outImg)];
    print('**** Start ****');

    # Call 'fswebcam' to take the Image
    process = Popen(camIn, stdout=PIPE, stderr=PIPE);
    stdout, stderr = process.communicate();
    print('---STDERR---');
    print(stderr.decode('utf-8'));
    time.sleep(5);

    # Call 'mv' to move the image to the USB drive
    print('---STDERR---');
    os.system('mv ' + outImg + ' uwphotos')
    print('**** End ****');

    count += 1;
    time.sleep(5);
