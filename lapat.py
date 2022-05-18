from PIL import Image
import shutil
import argparse
from pathlib import Path

print('Framing...')
parser = argparse.ArgumentParser()
parser.add_argument('path')
args = parser.parse_args()


frame_path = [path for path in Path('frames').glob('*.png')]
folder = './'+args.path+'_face'
output = './' + args.path+'_out'
Path(output).mkdir(parents=True, exist_ok=True)
counter = 0
for path in Path(folder).glob('*.jpg'):
    if counter == 4:
        counter = 0
    frame = Image.open(frame_path[counter]).resize((600, 600))
    background = Image.open(path).resize((600, 600))
    background.paste(frame, (0, 0), frame)
    background.save(output+'/'+path.name)
    counter += 1
shutil.rmtree(args.path, ignore_errors=True)
shutil.rmtree(args.path+'_face', ignore_errors=True)
