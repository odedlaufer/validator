import pandas as pd
import pytest

from core.validator import validate_from_columns, validate_mandatory_fields


def test_validation_passes_with_yaml_and_config_mapping(monkeypatch):
    monkeypatch.setattr("core.constants.MANDATORY_FIELDS", ["sku", "price", "color"])

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

    # Should not raise
    validate_mandatory_fields(modules, config, df)
    validate_from_columns(modules, df)


def test_validation_fails_missing_from_column():
    modules = [{"clean_price": {"from_column": "missing", "to_column": "price"}}]
    df = pd.DataFrame(columns=["price"])

    with pytest.raises(ValueError, match="from_column.*not found"):
        validate_from_columns(modules, df)


def test_validation_fails_missing_mandatory_field(monkeypatch):
    monkeypatch.setattr("core.constants.MANDATORY_FIELDS", ["sku", "price"])

    modules = [{"normalize_text": {"from_column": "product", "to_column": "product_cleaned"}}]
    config = {"price": "price"}  # 'sku' is missing
    df = pd.DataFrame(columns=["product", "price"])

    with pytest.raises(ValueError, match="Mandatory field"):
        validate_mandatory_fields(modules, config, df)
