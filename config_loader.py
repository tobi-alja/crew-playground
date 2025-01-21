import yaml
from pathlib import Path

def load_config(config_file):
    config_path = Path(__file__).parent / 'config' / config_file
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def get_agent_config():
    return load_config('agents.yaml')

def get_task_config():
    return load_config('tasks.yaml')