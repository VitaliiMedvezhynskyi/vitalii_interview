import json, boto3, os

def lambda_handler (event, context):
    s3 = boto3.resource('s3')
bucket = s3.Bucket('my.s3.list.bucket')
for obj in bucket.objects.all():
    print(obj.key)