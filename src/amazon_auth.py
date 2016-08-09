import boto
import boto.s3
import sys
from boto.s3.key import Key
import os
import ConfigParser

config = ConfigParser.RawConfigParser()
config.optionxform = str
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'config'))

ACCESS_KEY_ID = config.get("amazon", "key") 
SECRET_ACCESS_KEY = config.get("amazon", "secret") 
def get_bucket():
  bucket_name = config.get("amazon", "bucket")
  conn = boto.connect_s3(ACCESS_KEY_ID, SECRET_ACCESS_KEY)
  return conn.get_bucket(bucket_name, validate=False)

def get_folders():
  folders = config.get("amazon", "folders").split(",") 
  return folders

def get_files(folders):
  all_files = []
  for folder in folders:
    files = [folder + "/" + f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    all_files.extend(files)
  return all_files

def upload_to_s3(filename, folder, bucket):
  key = bucket.new_key(filename.split("/")[-1])
  key.set_contents_from_filename(filename, cb=percent_cb, num_cb=10)



def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

#key = bucket.new_key('akey') 
#key.set_contents_from_filename(testfile, cb=percent_cb, num_cb=10)


if __name__ == "__main__":
  folds = get_folders()
  files = get_files(folds)
  for f in files:
    upload_to_s3(f, '', get_bucket())
