import os
import unittest
import signer
import symbols
from random import randint

class AppTests(unittest.TestCase):
    """
    Ensure to add the project to PYTHON_PATH in order to make the package visible to this test file
    Also, make sure you run this test from the test directory
    """
    def test_sign(self):

        def randomName():
            return "".join("abcdefghijklmnopqrstuvwxyz"[randint(0,100)%26] for i in range(5))

        # current working directory must be the /test directory
        pathToTestFile = os.path.join(os.getcwd() + "/sample/")
        samplefiles = os.listdir(pathToTestFile)

        for file in samplefiles:
            # Lets deal with files
            if len(file.split("."))>0 and file.split(".")[-1] in symbols.symbols:
                with open(pathToTestFile + file, "r") as f:
                    # keep the old file contents before signing
                    oldContent = f.read()
                author = randomName()
                # sign test files
                signer.Sign(pathToTestFile+file, author)
                with open(pathToTestFile+file, "r") as f:
                    self.assertTrue(author in f.read())
                # write back the old file contents after signing
                with open(pathToTestFile + file, "w") as f:
                    f.write(oldContent)

if __name__ == "__main__":
    unittest.main()

