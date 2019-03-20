import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.grid']=False
plt.rcParams["figure.figsize"] = [8,6]
plt.rcParams['axes.edgecolor']='black'
fig, ax1 = plt.subplots()

#Import the Data
Stratford = pd.read_csv('Stratford FEV.csv')
hT = Stratford['hT']
FEV = Stratford['FEV']
Side = Stratford['Square Lake']

ax1.set_xlabel('$h_T$ [m]', size=15)
ax1.set_ylabel('$FEV$ [Mm$^3$]', size=15, color='tomato')
ax1.plot(hT, FEV, color='tomato', marker='x', markeredgecolor='k')
ax1.tick_params(axis='y', labelcolor='tomato')
ax1.set_ybound(0,35)
ax1.set_ylim(0,35)
ax1.set_xlim(1,1.889)


ax2 = ax1.twinx()

ax2.set_ylabel('2m deep square lake side length [m]', size=15, color='cornflowerblue')
ax2.plot(hT, Side, color='cornflowerblue', marker='o', markeredgecolor='k')
ax2.tick_params(axis='y', labelcolor='cornflowerblue')
ax2.set_ybound(0,6000)

fig.tight_layout()
plt.show()