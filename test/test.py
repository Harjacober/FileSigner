import os
import unittest
import signer
import symbols
from random import randint

class AppTests(unittest.TestCase):
    def test_sign(self):

        def randomName():
            return "".join("abcdefghijklmnopqrstuvwxyz"[randint(0,100)%26] for i in range(5))

        pathToTestFile = os.path.join(os.getcwd()+"/sample/")
        samplefiles = os.listdir(pathToTestFile)
        for inode in samplefiles:
            # Lets deal with files
            if inode.split(".")[-1] in symbols.symbols:
                with open(pathToTestFile+inode,"r") as f:
                    oldContent=f.read()
                author=randomName()
                signer.Sign(pathToTestFile+inode,author)
                with open(pathToTestFile+inode,"r") as f:
                    self.assertTrue(author in f.read())
                with open(pathToTestFile+inode,"w") as f:
                    f.write(oldContent)

if __name__ == "__main__":
    unittest.main()

