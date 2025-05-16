import yaml
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(BASE_DIR, "config.yaml")
prompt_config_path = os.path.join(BASE_DIR, "promptConfig.yaml")


with open(config_path) as f:
    config_data = yaml.load(f, Loader=yaml.FullLoader)

with open(prompt_config_path) as f:
    prompt_data = yaml.load(f, Loader=yaml.FullLoader)


def get_config(key):
    value = config_data.get(key)
    return value


def get_prompt(key):
    prompt = prompt_data.get(key)
    return prompt
