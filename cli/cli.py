import argparse
import logging

from core.parser import parse_csv, parse_json, parse_yaml
from core.processor import apply_modules
from core.validator import validate_from_columns, validate_mandatory_fields


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%H:%M:%S",
    )
    return logging.getLogger("csv-validator")


def run_validation(modules, json_config, df, logger):
    logger.info("Validating YAML and CSV...")
    validate_mandatory_fields(modules, json_config, df)
    validate_from_columns(modules, df)
    logger.info("Validation passed.")


def run_processing(modules, df, logger):
    logger.info("Applying preprocessing modules...")
    return apply_modules(modules, df, logger)


def main():
    parser = argparse.ArgumentParser(description="Validate and process YAML, JSON, and CSV files.")
    parser.add_argument("--yaml", required=True, help="Path to the plan.yaml file")
    parser.add_argument("--json", required=True, help="Path to the config.json file")
    parser.add_argument("--csv", required=True, help="Path to the data.csv file")
    parser.add_argument(
        "--output", default="processed_output.csv", help="Path to save the processed CSV"
    )
    args = parser.parse_args()

    logger = setup_logger()

    try:
        modules = parse_yaml(args.yaml)
        json_config = parse_json(args.json)
        df = parse_csv(args.csv)

        run_validation(modules, json_config, df, logger)
        df_processed = run_processing(modules, df, logger)

        df_processed.to_csv(args.output, index=False)
        logger.info(f"Done! Processed CSV saved to: {args.output}")

    except Exception as e:
        logger.error(f"Unhandled exception occurred: {e}")
        exit(1)
