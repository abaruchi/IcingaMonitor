import os
import time

import boto
from boto.s3.key import Key


def upload_to_s3(aws_access_key_id, aws_secret_access_key, file, bucket, key,
                 callback=None, md5=None, reduced_redundancy=False,
                 content_type=None):

    try:
        size = os.fstat(file.fileno()).st_size
    except:
        file.seek(0, os.SEEK_END)
        size = file.tell()

    conn = boto.connect_s3(aws_access_key_id, aws_secret_access_key)
    bucket = conn.get_bucket(bucket, validate=True)
    k = Key(bucket)
    k.key = key
    if content_type:
        k.set_metadata('Content-Type', content_type)
    sent = k.set_contents_from_file(file, cb=callback, md5=md5,
                                    reduced_redundancy=reduced_redundancy,
                                    rewind=True)
    file.seek(0)

    if sent == size:
        return True
    return False

AWS_ACCESS_KEY = 'AKIAI2VT7X6ANQ3O73RA'
AWS_ACCESS_SECRET_KEY = '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'

file = open('testing_s3.txt', 'r+')
timestamp = time.strftime("%d_%m_%Y")

key = "backup/"+timestamp+"/"+file.name
print (key)
bucket = "icingabucket"

if upload_to_s3(AWS_ACCESS_KEY, AWS_ACCESS_SECRET_KEY, file, bucket, key):
    print 'It worked!'
else:
    print 'The upload failed...'
