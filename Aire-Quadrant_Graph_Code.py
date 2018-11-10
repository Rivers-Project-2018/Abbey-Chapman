import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["figure.figsize"] = [10,10]
plt.rcParams['axes.edgecolor']='white'

armley=pd.read_csv('Aire Data.csv')
day = armley['Day in December']
flow = armley['Flow Rate (m^3/s)']
height = armley['Height (m)']

def scale(x):
    return ((x-min(x))/(max(x)-min(x)))

scaledday = scale(day)
scaledflow = scale(flow)
scaledheight = scale(height)
negday = -(scaledday)
negheight = -(scaledheight)

scaledht = (3.9-min(height))/(max(height)-min(height))
scaledhm = (4.77-min(height))/(max(height)-min(height))
scaledqm = (300.2-min(flow))/(max(flow)-min(flow))
scaledqt = (219.1-min(flow))/(max(flow)-min(flow))

a = ((max(height)-min(height))/(max(height)-min(height)))
b = ((max(flow)-min(flow))/(max(flow)-min(flow)))

fig, ax = plt.subplots()

ax.plot(scaledday, scaledflow, 'black', linewidth=2)
ax.plot(negheight, negday, 'black', linewidth=2)
ax.plot(negheight, scaledflow, 'black', linewidth=2)

ax.plot([0,-1*a], [0,b], 'black', linestyle='--', marker='', linewidth=2)

ax.plot([-scaledht,-scaledht],[-1,scaledqt], 'black', linestyle='--', linewidth=1)
ax.plot([-scaledhm,-scaledhm],[-1,scaledqm], 'black', linestyle='--', linewidth=1)
ax.plot([-scaledht,1],[scaledqt,scaledqt], 'black', linestyle='--', linewidth=1)
ax.plot([-scaledhm,1],[scaledqm,scaledqm], 'black', linestyle='--', linewidth=1)

ax.plot([71/250,71/250,71/250],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([69/125,69/125,69/125],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([71/250,69/125],[-1/5,-1/5], 'black', linewidth=1)
ax.plot([71/250,71/250],[scaledqm,scaledqt], 'black',linewidth=1.5)
ax.plot([71/250,69/125],[scaledqm,scaledqm], 'black',linewidth=1.5)
ax.plot([71/250,69/125],[scaledqt,scaledqt], 'black',linewidth=1.5)
ax.plot([69/125,69/125],[scaledqm,scaledqt], 'black',linewidth=1.5)

ticks_x = [-4874/4091,-3874/4091,-2874/4091,-1874/4091,-874/4091,1/5,2/5,3/5,4/5,1]
#done by doing (2-min(height))/(max(height)-min(height)) to find where 2 should be positioned on the axis.
ticks_y = [-1,-4/5,-3/5,-2/5,-1/5,3/52,17/78,59/156,7/13,109/156,67/78,53/52]
ax.set_xticks(ticks_x)
ax.set_yticks(ticks_y)
Ticks_x = [6,5,4,3,2,26,27,28,29,30]
Ticks_y = [30,29,28,27,26,50,100,150,200,250,300,350]
ax.set_xticklabels(Ticks_x)
ax.set_yticklabels(Ticks_y)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.tick_params(axis='x', colors='black', direction='out', length=10, width=1)
ax.tick_params(axis='y', colors='black', direction='out', length=10, width=1)

ax.fill_between(scaledday, scaledflow, scaledqt, where=scaledflow >= scaledqt, facecolor='gray')

plt.title('Aire Graph')

plt.text(-4/6, -1,'$h_t$')
plt.text(-13/15, -1,'$h_m$')
plt.text(1, 187/210,'$Q_m$')
plt.text(1, 87/140,'$Q_t$')
plt.text(0.34,0.70,'F.E.V.', size=15)
plt.text(0.4,-0.18,'$T_f$')
plt.text(0.27,-0.213,'<')
plt.text(0.535,-0.213,'>')

plt.text(0, 1.05,'Flow $[m^3/s]$', size=10)
plt.text(0.75, -0.13,'Day in December', size=10)
plt.text(-0.35, -1.09,'Day in December', size=10)
plt.text(-1.1, 0.02,'Height $[m]$', size=10)

plt.text(-0.015,1.07,'^')
plt.text(-0.011,-1.11,'v')
plt.text(1.08,-0.015,'>')
plt.text(-1.1,-0.015,'<')

plt.text(0.4,-0.4,'$F.E.V.≈9.34Mm^3$', size=15)
plt.text(0.4,-0.475,'$T_f=32.00hrs$', size=15)
plt.text(0.4,-0.55,'$h_t=3.90m$', size=15)
plt.text(0.4,-0.625,'$h_m=4.77m$', size=15)
plt.text(0.4,-0.7,'$Q_t=219.1m^3/s$', size=15)
plt.text(0.4,-0.775,'$Q_m=300.2m^3/s$', size=15)