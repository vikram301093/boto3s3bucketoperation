import boto3

s3 = boto3.client("s3")

s3.create_bucket(Bucket = "myfirstbucketvikram301093", CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})


# Call S3 to list current buckets
response = s3.list_buckets()

# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
print("Bucket List: %s" % buckets)

filename = 'myfirstupload.text'
bucket_name = 'myfirstbucketvikram301093'

s3.upload_file(filename,bucket_name,filename)
