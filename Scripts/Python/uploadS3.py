import tinys3

access_key_id = "AKIAI2VT7X6ANQ3O73RA"
access_key = "TCyah0k3ufq9uAMl9bEoROfGIvlgtbWUsVrYWZTm"

conn = tinys3.Connection(access_key_id, access_key, tls=True,
                         endpoint='s3.amazonaws.com')

f = open('testing_s3.txt','rb')
print conn.upload('testing_s3.txt',f,'testing-bucket')
print conn.get('./testing_s3.txt','testing-bucket')
