# IMPORTS
import pandas as pd
import numpy as np
import datetime as dt

from scipy.stats import norm

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns

# DATA PATH
path_mydata = 'INSERT FILE PATH HERE'
tab_perf = 'INSERT'
tab_sels = 'INSERT'
path_rfr = 'INSERT FILE PATH HERE'

# OTHER PARAMETERS
roll_beta_wdw = 12
sell_wdw = 365
today = dt.date(2021,9,12)
crnt_date = dt.date(2021,9,12)
sp500wts = {'Info Tech': 0.257, 'Health': 0.154, 'Comm': 0.108, 'Fin': 0.106, 'C Disc': 0.105, 'Inds': 0.079,
           'C Stap': 0.074, 'Util': 0.033, 'Ener': 0.03, 'RE': 0.029, 'Mat': 0.025}

# READ IN DATA

# Read in raw returns
data_perf_raw = pd.read_excel(path_mydata, sheet_name = tab_perf)
data_sels_raw = pd.read_excel(path_mydata, sheet_name = tab_sels)

# Work off of a copy
data_perf = data_perf_raw.copy()
data_sels = data_sels_raw.copy()

# Drop all columns except portfolio / S&P returns
data_perf = data_perf.loc[:,['Date','P_R_%','SP_R_%']].dropna()
data_perf = data_perf.set_index('Date')

# Drop last row (incomplete period)
data_perf = data_perf.drop(data_perf.tail(1).index)

# Read in 3 month T-bill as RFR
rfr = pd.read_csv(path_rfr)
rfr = rfr.rename(columns = {'DATE':'Date'})
rfr['Date'] = pd.to_datetime(rfr['Date'])
rfr = rfr.set_index('Date')
rfr = rfr.loc[data_perf.index[0]:data_perf.index[-1],:] / 100

# Convert 3 month T-bill to monthly rate
rfr = (1 + rfr)**(1/12) - 1

# Adjust return series for T-bill rate
data_perf = data_perf.sub(rfr.values)

# Create alpha and set date
data_perf['Alpha'] = data_perf['P_R_%'] - data_perf['SP_R_%']

# SET UP OUTPUT

df_op = pd.DataFrame(columns = ['Metric'])
df_compare = pd.DataFrame(index = data_perf.columns)

# PORTFOLIO PERFORMANCE CALCULATIONS











