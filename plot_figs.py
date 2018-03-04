"""
2018-02-22 17:42

Plot stocks & estate figs
(based on 180220-HK_plot_figs.py)

input: 
est_file: path to est file (string)
stk_file: path to stk file (string)
graph_name: name for the graphs (string)

Log:
2018-03-02  Added the red blob (point of normalization)
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from datetime import datetime
import animation

sns.set_style('white')
sns.set_context("poster")


def read_data(est_file, stk_file):
    est_data = pd.read_csv(est_file)
    est_data.date = pd.to_datetime(est_data.date, format='%Y-%m-%d')
    est_data = est_data.set_index('date')

    stk_data = pd.read_csv(stk_file, header=0, names=['date', 'price'])
    # stk_data.date = pd.to_datetime(stk_data.date, format='%m/%d/%Y')
    stk_data.date = pd.to_datetime(stk_data.date, format='%Y-%m-%d')
    stk_data = stk_data.set_index('date')
    return est_data, stk_data


def normalize_df(df, year, month):
    """ Parameters:
    df: the dataframe
    date: ref point for the normalization
    df must have price column
    Return df with norm_val column"""
    norm = df[(df.index.year == year) & (df.index.month == month)].price[0]
    df['norm_val'] = df.price / norm
    return df


def comparison_plot(df_stk, df_est, year, month, fig_name):
    """Paremeters:
    (df_stock, df_estate)
    plot by norm_val column
    """
    col_red = '#e15742'
    col_org = '#ffa021'

    plt.figure(dpi=100)
    # Plot time-series
    plt.plot(df_stk.norm_val, label='Stock')
    plt.plot(df_est.norm_val, label='Estate', color=col_org)
    # Point of Normalization
    plt.plot(np.datetime64(datetime(year, month, 1)), 1, '.',
             color=col_red,
             markersize=15,
             label='Point of Normalization')
    # Config plot
    plt.legend(loc=2)
    # Add an '0' if between month 01 to 09
    if month in np.arange(1, 10):
        title = 'Stock vs Estate Value (Normalized at '\
            + str(year) + '-0' + str(month) + ')'
    else:
        title = 'Stock vs Estate Value (Normalized at '\
            + str(year) + '-' + str(month) + ')'
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Normalized Value')
    # plt.xlim(year, 2018)
    plt.ylim(0, 6)
    plt.gca().yaxis.grid(True)
    plt.savefig(fig_name + '/' + title.replace(' ', '_') + '.png')
    plt.close('all')

# main script


def run_script(est_file, stk_file, fig_name, years, months, png_dir):
    est_data, stk_data = read_data(est_file, stk_file)

    for year in years:
        for month in months:
            est_data = normalize_df(est_data, year, month)
            stk_data = normalize_df(stk_data, year, month)
            comparison_plot(stk_data, est_data, year, month, fig_name)
    print('Figure Plotted')

    # animation
    animation.animate_all_pngs(png_dir)


# Parameters

if __name__ == '__main__':
    # HK
    # est_file = 'data/estates/hk.csv'    # require date & price column
    # stk_file = 'data/stocks/^HSI.csv'   # require date & price column
    # fig_name = 'hk_figs'
    # png_dir = './hk_figs/'
    # months = np.arange(1, 13)

    # UK
    est_file = 'data/estates/uk.csv'    # require date & price column
    stk_file = 'data/stocks/^FTSE.csv'   # require date & price column
    fig_name = 'uk_figs'
    png_dir = './uk_figs/'

    years = np.arange(1993, 2015)
    months = [3, 6, 9, 12]      # Plot quarterly
    run_script(est_file, stk_file, fig_name, years, months, png_dir)
