# import the necessary packages
import uuid
import os
import datetime
from PIL import Image
from motion_detector.s3_client import s3_client

class TempImage:

    def __init__(self, basePath, name, conf, ext=".jpg"):
        self.basePath = basePath
        self.name = name
        self.conf = conf
        self.ext  = ext
        # construct the file path
        self.path = "{base_path}/{name}{ext}".format(base_path=basePath,
                                                     name=name, ext=ext)
        self.th_path = "{base_path}/th_{name}{ext}".format(base_path=basePath,
                                                     name=name, ext=ext)
        self.client = s3_client(conf)

    def cleanup(self):
        # remove the file
        os.remove(self.path)
        os.remove(self.th_path)

    def create_thumbnail(self):
        size = 128, 128
        im = Image.open(self.path)
        im.thumbnail(size)
        im.save(self.th_path, "JPEG")

    def upload(self):
       file_name = "{name}{ext}".format(name=self.name, ext=self.ext)
       self.upload_file(file_name, self.path)

    def upload_thumbnail(self):
       file_name = "thumbnails/{name}{ext}".format(name=self.name, ext=self.ext)
       self.upload_file(file_name, self.th_path)

    def upload_file(self, file_name, path):
        # Upload picture to S3
        now = datetime.datetime.now()
        upload_filename = self.conf['s3_path'] + now.strftime(
            "%Y-%m-%d") + '/' + file_name
        self.client.upload_file(path,
                           self.conf['bucket'],
                           upload_filename,
                           ExtraArgs={'ACL': 'public-read'})
        print("[UPLOAD] " + upload_filename)
