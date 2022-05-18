import cv2
import argparse
from pathlib import Path

print('Cropping...')
parser = argparse.ArgumentParser()
parser.add_argument('path')

args = parser.parse_args()

folder = './'+args.path+'_face'
Path(folder).mkdir(parents=True, exist_ok=True)
counter = 0

for path in Path(args.path).glob('*.jpg'):
    try:
        image = cv2.imread(args.path + '/'+path.name)
    except:
        pass
    gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    try:
        (x, y, w, h) = faces[0]
        face = image[y-40:y + h + 40, x-40:x + w + 40]
        path_name = folder + '/' + str(counter) + '.jpg'
        cv2.imwrite(path_name, face)
        counter += 1
    except:
        pass

