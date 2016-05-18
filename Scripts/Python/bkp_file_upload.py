import sys
import time as t

import uploadS3 as s3


# main
AWS_ACCESS_KEY = sys.argv[1]
AWS_ACCESS_SECRET_KEY = sys.argv[2]

file = open('/tmp/icinga_backup.sql', 'rb')
timestamp = t.strftime("%d_%m_%Y")

key = "backup/"+timestamp+"/"+file.name
print (key)
bucket = "icingabucket"

if s3.upload_to_s3(AWS_ACCESS_KEY, AWS_ACCESS_SECRET_KEY, file, bucket, key):
    print 'File sent to S3'
else:
    print 'The upload failed'