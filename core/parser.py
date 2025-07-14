import json
from typing import Any, Dict, List

import pandas as pd
import yaml


def parse_yaml(yaml_path: str) -> List[Dict[str, Any]]:
    with open(yaml_path, "r") as f:
        plan = yaml.safe_load(f)
    job_steps = plan.get("job", [])
    for step in job_steps:
        if "preprocessing" in step:
            return step["preprocessing"]
    return []


def parse_json(json_path: str) -> Dict[str, Any]:
    try:
        with open(json_path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise ValueError(f"Failed to parse JSON: {e}")


def parse_csv(csv_path: str) -> pd.DataFrame:
    return pd.read_csv(csv_path)
