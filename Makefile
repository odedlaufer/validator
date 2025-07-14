VALID_PATH ?= ./test_data/valid
INVALID_PATH ?= ./test_data/invalid
MOUNT_PATH = /app/test_data
IMAGE = cli-validator

valid: ## Run validator on valid input
	python main.py --yaml $(VALID_PATH)/plan.yaml --json $(VALID_PATH)/config.json --csv $(VALID_PATH)/data.csv

invalid: ## Run validator on invalid input
	python main.py --yaml $(INVALID_PATH)/plan.yaml --json $(INVALID_PATH)/config.json --csv $(INVALID_PATH)/data.csv

docker-build: ## Build Docker image
	docker build -t $(IMAGE) .

docker-valid: ## Run validator in Docker on valid input
	docker run --rm -v $(dir $(VALID_PATH)):/app/test_data $(IMAGE) \
		--yaml test_data/valid/plan.yaml \
		--json test_data/valid/config.json \
		--csv test_data/valid/data.csv

docker-invalid: ## Run validator in Docker on invalid input
	docker run --rm -v $(dir $(INVALID_PATH)):/app/test_data $(IMAGE) \
		--yaml test_data/invalid/plan.yaml \
		--json test_data/invalid/config.json \
		--csv test_data/invalid/data.csv

clean: ## Remove generated output file
	rm -f processed_output.csv

test: ## Run both valid and invalid cases
	make valid
	make invalid || true

docker-test: ## Run both Docker validation cases
	make docker-valid
	make docker-invalid

lint: ## Run pre-commit linting
	pre-commit run --all-files

help: ## Show this help message
	@awk 'BEGIN {FS = ":.*?## "}; /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' Makefile

.PHONY: valid invalid docker-valid docker-invalid docker-build test docker-test clean lint help