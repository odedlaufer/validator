include .env

VALID_PATH ?= ./test_data/valid
INVALID_PATH ?= ./test_data/invalid

MOUNT_PATH=/app/test_data


IMAGE=cli-validator


valid:
	python main.py --yaml $(VALID_PATH)/plan.yaml --json $(VALID_PATH)/config.json --csv $(VALID_PATH)/data.csv


invalid:
	python main.py --yaml $(INVALID_PATH)/plan.yaml --json $(INVALID_PATH)/config.json --csv $(INVALID_PATH)/data.csv


docker-build:
	docker build -t $(IMAGE) .


docker-valid:
	docker run --rm -v $(dir $(VALID_PATH)):/app/test_data $(IMAGE) \
		--yaml test_data/valid/plan.yaml \
		--json test_data/valid/config.json \
		--csv test_data/valid/data.csv


docker-invalid:
	docker run --rm -v $(dir $(INVALID_PATH)):/app/test_data $(IMAGE) \
		--yaml test_data/invalid/plan.yaml \
		--json test_data/invalid/config.json \
		--csv test_data/invalid/data.csv

clean:
	rm -f processed_output.csv

test:
	make valid
	make invalid || true

docker-test: docker-valid docker-invalid

lint:
	pre-commit run --all-files

.PHONY: valid invalid docker-valid docker-invalid docker-build test docker-test clean
