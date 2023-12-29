import io
import boto3
import pandas as pd
import datetime

s3_client = boto3.client("s3")

AWS_S3_BUCKET = "dataart-training-project-eu-north-1"
users_file_name = f"users/users{round(datetime.datetime.now().timestamp())}.csv"

df = pd.read_csv("/Users/mykhailobilyk/Downloads/Training Project Data - Video events/users.csv")

with io.StringIO() as csv_buffer:
    df.to_csv(csv_buffer, index=False)

    response = s3_client.put_object(
        Bucket=AWS_S3_BUCKET, Key=users_file_name, Body=csv_buffer.getvalue()
    )
