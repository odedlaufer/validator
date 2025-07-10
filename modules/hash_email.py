import hashlib


def apply(df, from_column, to_column):
    def hash_email(value):
        return (
            hashlib.sha256(value.encode('utf-8')).hexdigest()
            if isinstance(value, str)
            else ValueError
        )

    df[to_column] = df[from_column].apply(hash_email)
    return df
