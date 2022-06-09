import boto3
from app.core.config import get_settings

settings = get_settings()

comprehend = boto3.client(
    "comprehend",
    region_name="ap-northeast-2",
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
)
