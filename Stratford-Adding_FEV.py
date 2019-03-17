import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['axes.grid']=False
plt.rcParams["figure.figsize"] = [8,6]
plt.rcParams['axes.edgecolor']='black'
fig, ax = plt.subplots()

a=[4.28,1.82,0.31]
b=[2.15,1.16,0.22]
c=[1.8,0.66,0.09]
d=[0.33]
h=[1.6,1.7,1.8]

ax.plot(h,a, color='tomato', marker='x', markeredgecolor='k')
ax.plot(h,b, color='blue', marker='o', markeredgecolor='k')
ax.plot(h,c, color='green', marker='^', markeredgecolor='k')
ax.scatter(1.6,d, color='k', marker='s')
ax.set_ylim(0,4.5)
ax.set_xlim(1.595,1.805)
ax.set_xlabel('$h_T$ [m]', size=15)
ax.set_ylabel('$FEV$ [Mm$^3$]', size=15)
ax.xaxis.set_ticks(np.arange(1.6,1.9,0.1))