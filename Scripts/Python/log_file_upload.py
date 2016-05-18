import time as t
import sys

import uploadS3 as s3

# main
AWS_ACCESS_KEY = sys.argv[1]
AWS_ACCESS_SECRET_KEY = sys.argv[2]

file = open('/tmp/docker_logfiles.tar.gz', 'r+')
timestamp = t.strftime("%d_%m_%Y")
file_name = "docker_logfiles.tar.gz"

key = "logs/"+timestamp+"/"+file_name
print (key)
bucket = "icingabucket"

if s3.upload_to_s3(AWS_ACCESS_KEY, AWS_ACCESS_SECRET_KEY, file, bucket, key):
    print 'File sent to S3'
else:
    print 'The upload failed'
