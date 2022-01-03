import base64
import csv
import os

filename = 'MS-Celeb-1M//data//aligned_face_images//FaceImageCroppedWithAlignment.tsv'
outputDir = 'imgs'

with open(filename, 'r') as tsvF:
    reader = csv.reader(tsvF, delimiter='\t')
    i = 0
    for row in reader:
        MID, imgSearchRank, faceID, data = row[0], row[1], row[4], base64.b64decode(row[-1])

        saveDir = os.path.join(outputDir, MID)
        savePath = os.path.join(saveDir, "{}-{}.jpg".format(imgSearchRank, faceID))

        if not os.path.exists(saveDir):
            os.makedirs(saveDir)
            # print("makedirs {}".format(saveDir))
        with open(savePath, 'wb') as f:
            f.write(data)

        i += 1
        if i % 1000 == 0:
            print("Extract {} images".format(i))
