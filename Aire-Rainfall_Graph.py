import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams["figure.figsize"] = [13,3]
plt.rcParams['axes.edgecolor']='black'
fig, ax1 = plt.subplots()

#Import the Data
Warwick = pd.read_csv('Aire Stage.csv')
date = Warwick['Time stamp']
stage = Warwick['Value[m]']

Warwick2 = pd.read_csv('Aire-Rainfall.csv')
date1 = Warwick2['Time stamp']
rainfall = Warwick2['Rainfall [mm]']

converted_dates = [datetime.strptime(i, '%d/%m/%Y %H:%M') for i in date]
dates = [datetime.strptime(i, '%d/%m/%Y') for i in date1]

Date = matplotlib.dates.date2num(converted_dates)
Dates = matplotlib.dates.date2num(dates)
hfmt = matplotlib.dates.DateFormatter('%d/%m/%Y')

print(Date)


ax1.set_xlim(735719,736053.98958333)

ax2 = ax1.twinx()

ax2.set_ylim(0,5.5)
ax1.bar(Dates, rainfall, align='center', color='cornflowerblue')
ax2.plot(Date, stage, 'black', linewidth=1, color='k')
ax2.xaxis.set_major_formatter(hfmt)
ax2.set_ylabel('$\overline{h}$ [m]')
ax2.set_xlabel('Date')
ax1.set_ylabel('Rainfall [mm]', color='cornflowerblue')
ax1.tick_params(axis='y', labelcolor='cornflowerblue')
plt.show()
