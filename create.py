import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path')
args = parser.parse_args()

subprocess.run(['python', 'search.py', args.path])
subprocess.run(['python', 'crop.py', args.path])
subprocess.run(['python', 'lapat.py', args.path])

