import boto3


s3 = boto3.client('s3')

def show_buckets():
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3, bucket_name, region=None):
    s3.create_bucket(Bucket = bucket_name,
                     CreateBucketConfiguration={
                         'LocationConstraint': region
                     } )
    print(f"Bucket {bucket_name} created.")


def upload_backup(s3, file_name, bucket_name, key_name):

    """
    Uploads a backup file to the specified S3 bucket.
    with  a new key name.

    """


    data = open(file_name, 'rb')
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("Backup uploaded successfully to bucket:", bucket_name)

bucket_name = "my-backup-bucket"
region = "us-east-2"

# create_bucket(s3, bucket_name, region)
# show_buckets(s3)
file_name = r"Path\To\Your\Backup\my_backup.tar.gz"
upload_backup(s3, file_name, bucket_name,"my_backup.tar.gz")
