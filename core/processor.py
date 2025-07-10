import importlib


def apply_modules(modules, df, logger):
    for module_entry in modules:
        module_name = list(module_entry.keys())[0]
        module_data = module_entry[module_name]
        from_col = module_data["from_column"]
        to_col = module_data["to_column"]

        try:
            mod = importlib.import_module(f"modules.{module_name}")
            df = mod.apply(df, from_col, to_col)
            logger.info(f"Applied module: {module_name} | {from_col} -> {to_col}")
        except Exception as e:
            logger.error(f"Failed to apply module '{module_name}': {e}")
            raise
    return df
