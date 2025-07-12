from core.parser import parse_yaml


def test_parse_yaml_extracts_preprocessing_modules(tmp_path):
    yaml_content = """
job:
  - extract_data:
      source: s3
  - preprocessing:
      - normalize_text:
          from_column: name
          to_column: name_cleaned
      - hash_email:
          from_column: email
          to_column: email_hash
"""
    yaml_path = tmp_path / "plan.yaml"
    yaml_path.write_text(yaml_content)

    modules = parse_yaml(str(yaml_path))

    assert isinstance(modules, list)
    assert len(modules) == 2

    assert list(modules[0].keys())[0] == "normalize_text"
    assert modules[0]["normalize_text"]["from_column"] == "name"
    assert modules[1]["hash_email"]["to_column"] == "email_hash"
