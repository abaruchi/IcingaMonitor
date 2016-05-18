import time as t
import sys

import uploadS3 as s3

# main
AWS_ACCESS_KEY = sys.argv[1]
AWS_ACCESS_SECRET_KEY = sys.argv[2]

file = open('testing_s3.txt', 'r+')
timestamp = t.strftime("%d_%m_%Y")

key = "backup/"+timestamp+"/"+file.name
print (key)
bucket = "icingabucket"

if s3.upload_to_s3(AWS_ACCESS_KEY, AWS_ACCESS_SECRET_KEY, file, bucket, key):
    print 'It worked!'
else:
    print 'The upload failed...'