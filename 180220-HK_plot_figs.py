"""
2018-02-22 17:42

Plot HK stocks & estate figs
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_style('white')
sns.set_context("poster")

# Read in data

hk_est = pd.read_csv('data/estates/hk.csv')
hk_est.date = pd.to_datetime(hk_est.date, format='%Y-%m-%d')
hk_est = hk_est.set_index('date')

hk_stk = pd.read_csv('data/stocks/^HSI.csv', header=0, names=['date', 'price'])
hk_stk.date = pd.to_datetime(hk_stk.date, format='%m/%d/%Y')
hk_stk = hk_stk.set_index('date')


def normalize_df(df, year, month):
    """ Parameters:
    df: the dataframe
    date: ref point for the normalization
    df must have price column
    Return df with norm_val column"""
    norm = df[(df.index.year == year) & (df.index.month == month)].price[0]
    df['norm_val'] = df.price / norm
    return df


def comparison(df_stk, df_est, year, month):
    """Paremeters:
    (df_stock, df_estate)
    plot by norm_val column
    """
    plt.figure(dpi=200)
    plt.plot(df_stk.norm_val, label='Stock')
    plt.plot(df_est.norm_val, label='Estate')
    plt.legend(loc=2)
    title = 'Stock vs Estate Value (Normalized at '\
        + str(year) + '-' + str(month) + ')'
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Normalized Value')
    # plt.xlim(year, 2018)
    plt.ylim(0, 6)
    plt.gca().yaxis.grid(True)
    plt.savefig('hk_figs/' + title.replace(' ', '_') + '.png')
    plt.close('all')

years = np.arange(1993, 2015)
months = np.arange(1, 13)

for year in years:
    for month in months:
        hk_est = normalize_df(hk_est, year, month)
        hk_stk = normalize_df(hk_stk, year, month)
        comparison(hk_stk, hk_est, year, month)
