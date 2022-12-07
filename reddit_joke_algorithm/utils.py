import pandas as pd


def get_posts_date_range(df:pd.DataFrame):
    return df['timestamp'].min(), df['timestamp'].max()