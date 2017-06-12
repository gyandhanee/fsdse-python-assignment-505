import pandas as pd


def load_data():
    fh = open("./files/olympics.csv")
    df = pd.read_csv(fh, header=1)
    for name in df.columns:
        if '01' in name:
            df.rename(columns={name: name.replace('01 !', 'Gold')}, inplace=True)
        if '02' in name:
            df.rename(columns={name: name.replace('02 !', 'Silver')}, inplace=True)
        if '03' in name:
            df.rename(columns={name: name.replace('03 !', 'Bronze')}, inplace=True)
    country_names = []
    for i in df['Unnamed: 0']:
        a =  i.split("\xc2\xa0")
        country_names.append(a[0])
    df.set_index(pd.Series(country_names), inplace=True)

    df.drop('Totals', 0, inplace=True)
    return df


def first_country(df):
    return df.iloc[0]


def gold_medal(df):
    return df.iloc[:, 2].idxmax()


def biggest_difference_in_gold_medal(df):
    difference = (df['Gold'] - df['Gold.1'])
    return difference.idxmax()

def get_points(df):
    df["Points"] = (df['Gold.2'] * 3) + (df['Silver.2']*2) + (df['Bronze.2'])
    return df["Points"]
