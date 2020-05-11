
import argparse
import signer
from os import getcwd
import getpass

author = getpass.getuser()
dir_path = getcwd()

# Argument will be passed if a file is selected from the windows explorer
argParser = argparse.ArgumentParser()
argParser.add_argument('--dir_path', type=str, help='')
args = argParser.parse_args()

if args.dir_path:
    dir_path = args.dir_path
    # for debug purpose
    print(dir_path)

# Sign files here
signer.Sign(dir_path, author)

# To keep the command line window open
input()