# debug_run.py
from cli.cli import run_processing, run_validation, setup_logger
from core.parser import parse_csv, parse_json, parse_yaml

if __name__ == "__main__":
    logger = setup_logger()

    modules = parse_yaml("plan.yaml")
    json_config = parse_json("config.json")
    df = parse_csv("data.csv")

    run_validation(modules, json_config, df, logger)
    df_processed = run_processing(modules, df, logger)

    df_processed.to_csv("debug_output.csv", index=False)
    logger.info("Debug run completed.")


# import argparse
# import importlib
# import json
# from pathlib import Path

# import pandas as pd
# import yaml

# MANDATORY = ["sku", "category", "gender", "color", "image_url", "price"]


# def parse_yaml(yaml_path):
#     with open(yaml_path, 'r') as f:
#         plan = yaml.safe_load(f)
#     job_steps = plan.get("job", [])
#     for step in job_steps:
#         if "preprocessing" in step:
#             return step["preprocessing"]
#     return []


# def parse_json(json_path):
#     with open(json_path, 'r') as f:
#         return json.load(f)


# def validate_mandatory_fields(modules, json_config, df_csv):
#     to_columns = [list(m.values())[0]["to_column"] for m in modules]
#     csv_columns = df_csv.columns.tolist()
#     json_values = json_config.values()

#     for field in MANDATORY:
#         if field in to_columns:
#             if field not in json_values:
#                 raise ValueError(
#                     f"Mandatory field '{field}' is in YAML but missing from config.json"
#                 )
#         else:
#             client_col = json_config.get(field)
#             if not client_col:
#                 raise ValueError(
#                     f"Mandatory field '{field}' missing in YAML and not mapped in config.json"
#                 )
#             if client_col not in csv_columns:
#                 raise ValueError(
#                     f"Mandatory field: '{field}' expected as column '{client_col}' in CSV but not found."
#                 )


# def validate_from_columns(modules, df_csv):
#     csv_columns = df_csv.columns.tolist()
#     for module in modules:
#         module_body = list(module.values())[0]
#         from_col = module_body["from_column"]
#         if from_col not in csv_columns:
#             raise ValueError(f"'from_column' {from_col} not found in CSV headers")


# def apply_modules(modules, df):
#     for module_entry in modules:
#         module_name = list(module_entry.keys())[0]
#         module_data = module_entry[module_name]
#         from_col = module_data["from_column"]
#         to_col = module_data["to_column"]

#         try:
#             mod = importlib.import_module(f"modules.{module_name}")
#             df = mod.apply(df, from_col, to_col)
#             print(f"Applied module: {module_name} | {from_col} -> {to_col}")
#         except Exception as e:
#             raise RuntimeError(f"Failed to apply module '{module_name}: {e}'")
#     return df


# def main():
#     parser = argparse.ArgumentParser(description="Validate  and process YAML, JSON and CSV files.")
#     parser.add_argument("--yaml", required=True, help="Path to plan.yaml")
#     parser.add_argument("--json", required=True, help="Path to the config.json file")
#     parser.add_argument("--csv", required=True, help="Path to the data.csv file")
#     args = parser.parse_args()

#     modules = parse_yaml(args.yaml)
#     json_config = parse_json(args.json)
#     df_csv = pd.read_csv(args.csv)

#     validate_mandatory_fields(modules, json_config, df_csv)
#     validate_from_columns(modules, df_csv)

#     print("Validation passed.")

#     df_processed = apply_modules(modules, df_csv)
#     output = 'processed_csv.csv'
#     df_processed.to_csv(output, index=False)
#     print(f"Done. Processed CSV saved to {output}")


# if __name__ == "__main__":
#     main()
