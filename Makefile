VALID_PATH=/Users/odedlaufer/validation/test_data/valid
INVALID_PATH=/Users/odedlaufer/validation/test_data/invalid

valid:
	python main.py --yaml $(VALID_PATH)/plan.yaml --json $(VALID_PATH)/config.json --csv $(VALID_PATH)/data.csv

invalid:
	python main.py --yaml $(INVALID_PATH)/plan.yaml --json $(INVALID_PATH)/config.json --csv $(INVALID_PATH)/data.csv

clean:
	rm -f processed_output.csv

test:
	make valid
	make invalid || true

.PHONY: valid invalid clean test