
import argparse
import signer

argParser = argparse.ArgumentParser(description="Prepend Signature to Files") 
argParser.add_argument('--dir_path', type=str, help='Path to the directory whose files are to be signed')
argParser.add_argument('--author', type=str, help="Full name of file owner")
args = argParser.parse_args()

signer.Sign(args.dir_path, args.author) 