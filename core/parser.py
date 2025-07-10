import json

import pandas as pd
import yaml


def parse_yaml(yaml_path):
    with open(yaml_path, "r") as f:
        plan = yaml.safe_load(f)
    job_steps = plan.get("job", [])
    for step in job_steps:
        if "preprocessing" in step:
            return step["preprocessing"]
    return []


def parse_json(json_path):
    with open(json_path, "r") as f:
        return json.load(f)


def parse_csv(csv_path):
    return pd.read_csv(csv_path)
