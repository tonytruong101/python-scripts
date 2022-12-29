import boto3
import datetime

# Create an S3 client
s3 = boto3.client('s3')

# Set the name of the bucket and the prefix for the files you want to upload
bucket_name = 'my-bucket'
prefix = 'files/'

# Set the number of days after which you want to delete old files
days_to_keep = 5

# Get the current timestamp
now = datetime.datetime.utcnow()

# Iterate over all the objects in the bucket
objects = s3.list_objects(Bucket=bucket_name, Prefix=prefix)
for obj in objects['Contents']:
  # Get the last modified timestamp for the object
  last_modified = obj['LastModified']

  # Calculate the age of the object in days
  age_in_days = (now - last_modified).days

  # If the age of the object is greater than the number of days to keep, delete it
  if age_in_days > days_to_keep:
    s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
    print(f'Deleted object: {obj["Key"]}')

# Upload a file to S3
filename = 'file.txt'
s3.upload_file(filename, bucket_name, prefix + filename)
print(f'Uploaded {filename} to {prefix + filename}')

