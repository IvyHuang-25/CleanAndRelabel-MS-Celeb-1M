import os
from shutil import copyfile
import base64
import csv
import os



imgFolder = './imgs'
cleanFolder = './clean_imgs'
washList = './MS-Celeb-1M_clean_list.txt'

wlFile = open(washList, 'r')
goodFiles = wlFile.readlines()
goodFiles = [f.strip('\n ') for f in goodFiles]
goodFiles = [f.strip('\r ') for f in goodFiles]

count = 0
for goodFile in goodFiles:
    filename, label = goodFile.split(' ')
    filepath = os.path.join(imgFolder, filename)

    if os.path.exists(filepath):
        count += 1

        cleanpath = os.path.join(cleanFolder, label)
        if not os.path.exists(cleanpath):
            os.makedirs(cleanpath)
            print("makedirs {}".format(cleanpath))
        cleanpath = os.path.join(cleanpath, filename.split('/')[-1])

        copyfile(src=filepath, dst=cleanpath)
        print(count)
