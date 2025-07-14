# CLI Validator

A modular command-line tool for validating and processing CSV files based on a configuration plan defined in YAML and a column mapping provided via JSON. The tool supports dynamic preprocessing through plug-and-play modules, strict validation of mandatory fields, and automated processing pipelines.

---

## Features

- CLI interface using `argparse`
- Modular preprocessing via dynamic Python imports (`importlib`)
- YAML-driven workflow definition
- JSON-based column mapping
- CSV input and output with optional transformations
- Strict validation of required fields and source columns
- Pre-commit hooks and GitHub Actions CI/CD integration
- Dockerfile and Makefile for consistent development workflow
- Unit and integration test coverage using `pytest`

---

## Requirements

- Python 3.10+
- `pip` (Python package installer)
- Docker (optional, for containerized usage)

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/cli-validator.git
cd cli-validator
pip install -r requirements.txt
```
---

##** Usage**

```bash
python main.py \
  --yaml test_data/valid/plan.yaml \
  --json test_data/valid/config.json \
  --csv test_data/valid/data.csv \
  --output processed_output.csv

---

## **Arguments**

| Flag       | Description                          | Required                             |
| ---------- | ------------------------------------ | ------------------------------------ |
| `--yaml`   | Path to the YAML file with job steps | Yes                                  |
| `--json`   | Path to the JSON config mapping file | Yes                                  |
| `--csv`    | Path to the input CSV file           | Yes                                  |
| `--output` | Output path for the processed CSV    | No (default: `processed_output.csv`) |

---

## **Testing**

Run all unit and CLI tests using pytest:

```bash
pytest

To test the CLI with example datasets:

```bash
make test

---

## **Docker Usage**

Build the Docker image:

```bash
make docker-build

---

## **Project Structure**

cli/          - CLI entry point and orchestration (main.py, argument parsing)
core/         - Main logic for parsing, validation, processing
modules/      - Modular transformation steps (loaded dynamically)
test_data/    - Valid and invalid datasets for integration testing
tests/        - Unit and CLI integration tests

---

## **Development Tools**

Code Formatting: Black, isort
Linting: flake8
Security Scanning: gitleaks
Automation: Makefile
CI/CD: GitHub Actions (pre-commit, test jobs)

---

## **Author**

Oded Laufer - This project was developed as part of a learning initiative to build clean, testable, and extensible backend tools.
