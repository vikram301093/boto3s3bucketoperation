---
name: Not able to execute create_bucket() function of boto3 for aws s3 to create bucket.
  It is only working in us-east-1 region.
about: Describe this issue template's purpose here.

---

Hi,

I am trying to create bucket using boto3 create_bucket() function in aws.
I am not able to create bucket unless i am using us-east-1 region where it is working.
I am also observed that only create_bucket function is not working in all region except us-east-1, all other function like list_buckets(), upload_file() is working fine for all region.

I have configure the aws credential using aws configure command.

Below is my code:-

import boto3
s3 = boto3.client("s3")
s3.create_bucket(Bucket = "myfirstbucketvikram301093", CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
print("Bucket List: %s" % buckets)
filename = 'myfirstupload.text'
bucket_name = 'myfirstbucketvikram301093'
s3.upload_file(filename,bucket_name,filename)

I am finding below error when running in all region except us-east-1 :-

Traceback (most recent call last):
  File "all3operation.py", line 5, in <module>
    s3.create_bucket(Bucket = "myfirstbucketvikram301093")
  File "/root/anaconda3/lib/python3.5/site-packages/botocore/client.py", line 314, in _api_call
    return self._make_api_call(operation_name, kwargs)
  File "/root/anaconda3/lib/python3.5/site-packages/botocore/client.py", line 612, in _make_api_call
    raise error_class(parsed_response, operation_name)
botocore.exceptions.ClientError: An error occurred (IllegalLocationConstraintException) when calling the CreateBucket operation: The unspecified location constraint is incompatible for the region specific endpoint this request was sent to.


So my doubt is that boto3 functions are regions specific ?
