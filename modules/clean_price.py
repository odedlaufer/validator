import re


def apply(df, from_column, to_column):
    def clean(value):
        if isinstance(value, str):
            return float(re.sub(r'[^\d.]', '', value))
        return value

    df[to_column] = df[from_column].apply(clean)
    return df
