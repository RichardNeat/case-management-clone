from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class MinioMediaStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    custom_domain = False
    file_overwrite = False
    default_acl = "private"

    def __init__(self, *args, **kwargs):
        kwargs["endpoint_url"] = settings.AWS_S3_ENDPOINT_URL
        kwargs["use_ssl"] = False
        kwargs["addressing_style"] = "path"
        super().__init__(*args, **kwargs)
