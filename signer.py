from os import path, listdir, stat
import argparse
import time
from symbols import symbols
import platform


argParser = argparse.ArgumentParser(description="Prepend Signature to Files") 
argParser.add_argument('dir_path', type=str, help='Path to the directory whose files are to be signed')
argParser.add_argument('author', type=str, help="Full name of file owner")
args = argParser.parse_args()

# check that argment specified is a valid file or directory
assert(path.isdir(args.dir_path) or path.isfile(args.dir_path)), "You have to specify a directory by setting --dir_path"
if path.isdir(args.dir_path):
    assert(len(listdir(args.dir_path)) > 0), "No files to sign here"


# Get File extension 
getExtension = lambda fileName : fileName.split('.')[-1]

# Check if a file has extension
hasExtension = lambda fileName : len(fileName.split('.'))>0

# Get the time the file was created
def createdAt(filePath): 
    # We can get the time the file is created on Windows but only last modified time on linux
    if platform.system() in ('Windows', 'Linux'):
        return time.ctime(path.getctime(filePath))
    else:
        # we are on Mac Os, we can get the time the file was created
        return time.ctime(stat(filePath).st_birthtime)

# Generates signature content
def generateSignature(symbol, name, date):
    signature = "{open}\n**\n * author :   \t{name}\n * created : \t{date}\n**\n{close}\n"
    return signature.format(open=symbol[0], close=symbol[1], name=name, date=date)

# Signs a file
def signFile(filePath, symbol): 
    date = createdAt(filePath)
    signature = generateSignature(symbol, args.author, date) 
    f = open(filePath, 'r')
    contents = f.readlines()
    contents.insert(0, signature)
    f.close()
    with open(filePath, 'w+') as f:
        f.write(''.join(contents))

# Get comment symbol based on file extension
def getSymbol(extension): 
    return symbols[extension]

# signing a file
if path.isfile(args.dir_path):
    symbol = getSymbol(getExtension(args.dir_path))
    if symbol:
        signFile(args.dir_path, symbol)
    else:
        print("Oops! File type not supported")
#signing files in a folder
else:
    for file in listdir(args.dir_path):
        symbol = getSymbol(getExtension(file))
        filePath = args.dir_path + "/" + file
        if symbol:
            signFile(filePath, symbol)
        else:
            print("oops! File type not supported")

print("Done! File(s) successfully signed")