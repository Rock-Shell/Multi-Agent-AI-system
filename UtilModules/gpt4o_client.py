from AppConfig.AppConfigHelper import get_config
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=get_config('api_key'),
    api_version=get_config('api_version'),
    azure_endpoint=get_config('api_base')
)
