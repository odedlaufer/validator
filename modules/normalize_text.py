def apply(df, from_column, to_column):
    df[to_column] = df[from_column].astype(str).str.lower().str.strip()
    return df
