import pandas as pd
from utils import get_posts_date_range

if __name__ == '__main__':
    # open dataset
    df = pd.read_csv('./Dataset/reddit_wsb.csv')

    # overview of the data
    print('Scrape posts range:', get_posts_date_range(df))
    print('df keys', df.keys())
