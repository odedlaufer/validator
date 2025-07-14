from typing import Dict, List

import pandas as pd

from core.constants import MANDATORY_FIELDS


def validate_mandatory_fields(
    modules: List[Dict[str, Dict[str, str]]], json_config: Dict[str, str], df_csv: pd.DataFrame
) -> None:
    to_columns = [list(m.values())[0]["to_column"] for m in modules]
    csv_columns = df_csv.columns.tolist()
    json_values = json_config.values()

    for field in MANDATORY_FIELDS:
        if field in to_columns:
            if field not in json_values:
                raise ValueError(
                    f"Mandatory field '{field}' is in YAML but missing from config.json"
                )
        else:
            client_col = json_config.get(field)
            if not client_col:
                raise ValueError(
                    f"Mandatory field '{field}' missing in YAML and not mapped in config.json"
                )
            if client_col not in csv_columns:
                raise ValueError(
                    f"Mandatory field: '{field}' expected as column '{client_col}' in CSV but not found."
                )


def validate_from_columns(modules: List[Dict[str, Dict[str, str]]], df_csv: pd.DataFrame) -> None:
    csv_columns = df_csv.columns.tolist()
    for module in modules:
        module_body = list(module.values())[0]
        from_col = module_body["from_column"]
        if from_col not in csv_columns:
            raise ValueError(f"'from_column' {from_col} not found in CSV headers.")
