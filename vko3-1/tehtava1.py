import requests
import logging
import boto3
from botocore.exceptions import ClientError
import os


# Hakee jason dataa urlista
data = requests.get('https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json')
data_dict = data.json()

with open("checkpoint.txt", "w") as file_object:
    for row in data_dict["items"]:
        file_object.write("\n"f"{row['parameter']}")


def create_bucket(bucket_name, region=None):

    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

   


if __name__ == "__main__":
    create_bucket("katri-checkpoint-3", "eu-north-1")
    upload_file("checkpoint.txt", "katri-checkpoint-3")
