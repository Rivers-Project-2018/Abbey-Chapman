import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams["figure.figsize"] = [13,6]
plt.rcParams['axes.edgecolor']='black'
fig, ax = plt.subplots()

#Import the Data
Stratford=pd.read_csv('Stratford Data.csv')
day = Stratford['Day in November']
height = Stratford['Height (m)']

#Scale our Data
def scale(x):
    return ((x-min(x))/(max(x)-min(x)))
scaledday = scale(day)
scaledheight = scale(height)
    
Flow = []
for i in height:
    if i<=0.938 and i>=0.136:
        Flow.append(158.04*((i-0.263)**2.854))
    elif i<=max(height) and i>0.938:
        Flow.append(87.0362*((i-0.359)**0.962))
        
ax.set_ylim(0,135)
ax.set_xlim(21,31)

Ticks_x=[22,23,24,25,26,27,28,29,30,31]
ticks_x=[1,2,3,4,5,6,7,8,9,10]
Ticks_y=[25,50,75,100,125]
ax.set_xticks(Ticks_x)
ax.set_xticklabels(ticks_x)
ax.set_yticks(Ticks_y)
plt.tick_params(labelsize=15)

ax.plot(day,Flow,color='black')

qta=115.42
qtb=120.48

Qta=[]
for i in Flow:
    i = qta
    Qta.append(i)

Qtb=[]
for i in Flow:
    i = qtb
    Qtb.append(i)
ax.plot(day,Qta,'--',color='k')
ax.plot(day,Qtb,':',color='k')

a=np.array(Qta)
b=np.array(Qtb)
c=np.array(Flow)

ax.fill_between(day,c,b,where=c>=b,facecolor='tomato')

time_increment=900

flow = []
for i in Flow:
    if i>=qtb:
        flow.append((i-qtb)*(time_increment))
Ve=sum(flow)
print(Ve)
plt.text(30.4,qtb+2,'$Q_{Ta}$', size=20)
plt.text(30.4,qta-7.5,'$Q_{Tb}$', size=20)
plt.text(24,62,'$Q_{Ta}$ = 115.42m$^3$/s', size=20)
plt.text(24,53,'$V_{ea}$ = 1.83Mm$^3$', size=20)
plt.text(24,41,'$Q_{Tb}$ = 120.48m$^3$/s', size=20)
plt.text(24,33,'$V_{eb}$ = 0.82m$^3$/s', size=20)

plt.xlabel('t [day]', size=17)
plt.ylabel('Q [m$^3$/s]',size=17)