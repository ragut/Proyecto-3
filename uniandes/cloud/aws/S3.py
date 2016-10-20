import boto3
import os

class S3:

    s3 = None

    def __init__(self):
        self.s3 = boto3.resource('s3', region_name="us-west-2",
                                       aws_access_key_id=os.environ["aws_access_key_id"],
                                       aws_secret_access_key=os.environ["aws_secret_access_key"])

    def save_banner(self, url, name):
        data = open(url+name, 'rb')
        self.s3.Bucket('mebanner').put_object(Key=name, Body=data)
        data.close()
        os.remove(url+name)

    def delete_banner(self,name):
        bucket = self.s3.Bucket('mebanner')
        obj = bucket.Object(name)
        obj.delete()
