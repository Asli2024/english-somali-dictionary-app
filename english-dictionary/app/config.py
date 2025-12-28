import os
from typing import Optional

class Settings:
    # AWS Configuration
    AWS_REGION: str = os.getenv("AWS_REGION", "eu-west-2")
    AWS_ACCESS_KEY_ID: Optional[str] = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: Optional[str] = os.getenv("AWS_SECRET_ACCESS_KEY")

    # DynamoDB Configuration
    USE_DYNAMODB: bool = os.getenv("USE_DYNAMODB", "True").lower() == "true"
    DYNAMODB_TABLE_NAME: Optional[str] = os.getenv("DYNAMODB_TABLE_NAME")
    dynamodb_region: str = os.getenv("AWS_REGION", "eu-west-2")

    # Bedrock Configuration
    MODEL_ID: str = "anthropic.claude-3-7-sonnet-20250219-v1:0"
    MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", "4096"))
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.3"))
    TOP_P: float = float(os.getenv("TOP_P", "0.9"))

settings = Settings()
