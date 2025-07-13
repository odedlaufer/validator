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
