from os import path, listdir, stat
import time
from symbols import symbols
import platform



# Get File extension 
getExtension = lambda fileName : fileName.split('.')[-1]

# Check if a file has extension
hasExtension = lambda fileName : len(fileName.split('.'))>0

# Get the time a file was created
def createdAt(filePath): 
    # We can get the time the file is created on Windows but only last modified time on linux
    if platform.system() in ('Windows', 'Linux'):
        return time.ctime(path.getctime(filePath))
    else:
        # we are on Mac Os, we can get the time the file was created
        return time.ctime(stat(filePath).st_birthtime)

# Generates signature content
def generateSignature(symbol, name, date):

    signature_one = "{open}\n**\n * author :   \t{name}\n * created : \t{date}\n**\n{close}\n"

    signature_mul = "{open}\n{open}**\n{open} * author :   \t{name}\n{open} * created : \t{date}\n{open}**\n{close}\n"

    if symbol[2]:

        return signature_mul.format(open=symbol[0], close=symbol[1], name=name, date=date)

    else:

        return signature_one.format(open=symbol[0], close=symbol[1], name=name, date=date)


# Checks if file has already been signed before 
def fileAlreadySigned(contents, signature):
    return signature[0:40] in contents[0:50]  #checking 0-50th index of the string instead of the whole string, to increase search time
# Signs a file
def signFile(filePath, symbol, author): 
    date = createdAt(filePath)
    signature = generateSignature(symbol, author, date)
    f = open(filePath, 'r')
    contents = f.readlines()
 
    if not fileAlreadySigned(''.join(contents).lstrip(), signature):
        contents.insert(0, signature)
        f.close()
        with open(filePath, 'w+') as f:
            f.write(''.join(contents))
        print("File successfully signed")

        #R code block
    elif not fileAlreadySigned(''.join(contents)):
        contents.insert(0, signature)
        f.close()
        with open(filePath, 'w+') as f:
            f.write(''.join(contents))
            print("File already signed before")

# Get comment symbol based on file extension
def getSymbol(extension): 
    return symbols[extension]

def Sign(dir_path, author, *args):
    # check that argument specified is a valid file or directory
    assert(path.isdir(dir_path) or path.isfile(dir_path)), "You have to specify a directory by setting --dir_path"
    # check that there are files presents in the specified directory
    if path.isdir(dir_path):
        assert(len(listdir(dir_path)) > 0), "No files to sign here"

    # signing a file
    if path.isfile(dir_path):
        symbol = getSymbol(getExtension(dir_path))
        if symbol:
            signFile(dir_path, symbol,author)
        else:
            print("Oops! File type not supported")
    #signing files in a folder
    else:
        for file in listdir(dir_path):
            symbol = getSymbol(getExtension(file))
            filePath = dir_path + "/" + file
            if symbol and path.isfile(filePath):
                signFile(filePath, symbol,author)
            else:
                print("Oops! File type not supported or Encountered a folder")

