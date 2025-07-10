import pandas as pd

from validation.validate_and_process import validate_from_columns, validate_mandatory_fields

MANDATORY = ["sku", "price", "color"]


def test_validation_passes_with_yaml_and_config_mapping():
    modules = [
        {"clean_price": {"from_column": "raw_price", "to_column": "price"}},
        {"normalize_text": {"from_column": "product_color", "to_column": "color"}},
    ]

    config = {
        "sku": "sku",
        "price": "price",
        "color": "color",
        "category": "category",
        "image_url": "image_url",
        "pdp_link": "pdp_link",
        "gender": "gender",
    }

    df = pd.DataFrame(
        columns=["raw_price", "product_color", "sku", "category", "image_url", "pdp_link", "gender"]
    )

    # should not raise
    validate_mandatory_fields(modules, config, df)
    validate_from_columns(modules, df)


def test_validation_fails_missing_from_column():
    modules = [{"clean_price": {"from_column": "missing", "to_column": "price"}}]
    df = pd.DataFrame(columns=["price"])
    try:
        validate_from_columns(modules, df)
        assert False, "Expected ValueError for missing from_column"
    except ValueError as e:
        assert "from_column" in str(e)


def test_validation_fails_missing_mandatory_field_everywhere():
    modules = [{"normalize_text": {"from_column": "product", "to_column": "product_cleaned"}}]
    config = {"price": "price"}  # 'sku' missing
    df = pd.DataFrame(columns=["product", "price"])
    try:
        validate_mandatory_fields(modules, config, df)
        assert False, "Expected ValueError for missing mandatory field"
    except ValueError as e:
        assert "Mandatory field" in str(e)
