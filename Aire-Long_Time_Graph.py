import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams["figure.figsize"] = [12,5]
plt.rcParams['axes.edgecolor']='black'
fig, ax = plt.subplots()

#Import the Data
Aire = pd.read_csv('Aire Stage.csv')
date = Aire['Time stamp']
stage = Aire['Value[m]']

converted_dates = [datetime.strptime(i, '%d/%m/%Y %H:%M') for i in date]

Date = matplotlib.dates.date2num(converted_dates)
hfmt = matplotlib.dates.DateFormatter('%d/%m/%Y')

ax.set_xlim(735719,736053.98958333)
ax.set_ylim(0,5.5)

ax.plot(Date, stage, 'black', linewidth=1)
ax.xaxis.set_major_formatter(hfmt)
ax.set_ylabel('$\overline{h}$ [m]')
plt.show()