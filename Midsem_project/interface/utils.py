import os
import streamlit as st
import time
import boto3
from dotenv import load_dotenv
load_dotenv()

s3 = boto3.client(
    service_name="s3",
    region_name="eu-north-1",
    aws_access_key_id="AKIAVRUVWA22CPAH3THF",
    aws_secret_access_key="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",
)
bucket = "resume-bucket2"


def save_to_S3(uploadedfile):
    s3 = boto3.client(
        service_name="s3",
        region_name=os.getenv('AWS_REGION'),
        aws_access_key_id=os.getenv('ACCESS_KEY'),
        aws_secret_access_key=os.getenv('SECRET_KEY')
    )
    try:
        s3.upload_fileobj(uploadedfile,bucket , f"resume-{uploadedfile.name}")
        return
    except Exception as e:
        print(e)


def upload_file(uploadedfile):
    file_name = uploadedfile.name
    msg = st.toast(f'Uploading {file_name}...')
    try:
        save_to_S3(uploadedfile)
        msg.toast(f'Uploaded {file_name} successfully')
    except Exception:
        msg.toast(f'Error uploading {file_name}')


def get_number_of_resumes():
    paginator = s3.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket)

    object_count = 0
    for page in page_iterator:
        if 'Contents' in page:
            object_count += len(page['Contents'])

    return object_count