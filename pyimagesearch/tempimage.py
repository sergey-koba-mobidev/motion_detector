# import the necessary packages
import uuid
import os

# import the necessary packages
import uuid
import os


class TempImage:

    def __init__(self, basePath="./", name="", ext=".jpg"):
        # construct the file path
        self.path = "{base_path}/{name}{ext}".format(base_path=basePath,
                                                     name=name, ext=ext)

    def cleanup(self):
        # remove the file
        os.remove(self.path)
