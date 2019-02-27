#proper clarification for requirement is required
import boto3
s3_resource = boto3.resource('s3')
s3_resource.create_bucket(Bucket=YOUR_BUCKET_NAME, CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})
s3_resource.Bucket(first_bucket_name).upload_file(Filename=first_file_name, Key=first_file_name)
s3_resource.Object(second_bucket_name, first_file_name).delete()
