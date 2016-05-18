import uploadS3 as s3
import time as t

AWS_ACCESS_KEY = 'AKIAI2VT7X6ANQ3O73RA'
AWS_ACCESS_SECRET_KEY = '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'

file = open('testing_s3.txt', 'r+')
timestamp = t.strftime("%d_%m_%Y")

key = "backup/"+timestamp+"/"+file.name
print (key)
bucket = "icingabucket"

if s3.upload_to_s3(AWS_ACCESS_KEY, AWS_ACCESS_SECRET_KEY, file, bucket, key):
    print 'It worked!'
else:
    print 'The upload failed...'