import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams["figure.figsize"] = [10,10]
plt.rcParams['axes.edgecolor']='white'
fig, ax = plt.subplots()

#Import the Data
Calder=pd.read_csv('Calder Data.csv')
day = Calder['Day in December']
height = Calder['Height (m)']

#Scale our Data
def scale(x):
    return ((x-min(x))/(max(x)-min(x)))
scaledday = scale(day)
scaledheight = scale(height)

#finding and using ht from the hm.
ht=4.5
HM = []
for i in height:
    if i>=ht:
        HM.append(i)
hm=sum(HM)/len(HM)

#Finding qt and qm.
def Q(x):
    if x<=2.107 and x>=0.342:
        y = (8.459*((x-0.342)**2.239))
    elif x<=3.088 and x>2.107:
        y = (21.5*((x-0.826)**1.37))
    elif x<=max(height) and x>3.088:
        y = (2.086*((x+0.856)**2.515))
    return(y)
qt = Q(ht)
qm = Q(hm)   

#Rating Curve
Flow = []
for i in height:
    if i<=2.107 and i>=0.342:
        Flow.append(8.459*((i-0.342)**2.239))
    elif i<=3.088 and i>2.107:
        Flow.append(21.5*((i-0.826)**1.37))
    elif i<=max(height) and i>3.088:
        Flow.append(2.086*((i+0.856)**2.515))

scaledFlow = []
for i in Flow:
    scaledFlow.append((i-min(Flow))/(max(Flow)-min(Flow)))


#Plot the Rating Curve using Q NOT the Flow Rate.
negheight = -scaledheight
ax.plot(negheight,scaledFlow,'black',linewidth=2)
ax.plot([0,-1],[0,1],'forestgreen',linestyle='--', marker='', linewidth=2)

#Plot the Flow Rate and Height against the Date.
negday = -(scaledday)
ax.plot(scaledday, scaledFlow, 'black', linewidth=2)
ax.plot(negheight, negday, 'black', linewidth=2)

#Plot the lines illustrating ht,hm,qt,qm
#Scaling ht,hm,qt and qm.
scaledht = (ht-min(height))/(max(height)-min(height))
scaledhm = (hm-min(height))/(max(height)-min(height))
scaledqt = (qt-min(Flow))/(max(Flow)-min(Flow))
scaledqm = (qm-min(Flow))/(max(Flow)-min(Flow))
ax.plot([-scaledht,-scaledht],[-1,scaledqt], 'black', linestyle='--', linewidth=1)
ax.plot([-scaledhm,-scaledhm],[-1,scaledqm], 'black', linestyle='--', linewidth=1)
ax.plot([-scaledht,1],[scaledqt,scaledqt], 'black', linestyle='--', linewidth=1)
ax.plot([-scaledhm,1],[scaledqm,scaledqm], 'black', linestyle='--', linewidth=1)

#Fiddly plot to plot the box around the F.E.V. and the Tf line.
ax.plot([67/200,67/200,67/200],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([67/160,67/160,67/160],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([67/200,67/160],[-1/5,-1/5], 'black', linewidth=1)
ax.plot([67/200,67/200],[scaledqm,scaledqt], 'black',linewidth=1.5)
ax.plot([67/200,67/160],[scaledqm,scaledqm], 'black',linewidth=1.5)
ax.plot([67/200,67/160],[scaledqt,scaledqt], 'black',linewidth=1.5)
ax.plot([67/160,67/160],[scaledqm,scaledqt], 'black',linewidth=1.5)

#Formatting the ticks and the Axis.
ticks_x = [-4731/4466,-533/638,-2731/4466,-1731/4466,-731/4466,1/4,2/4,3/4,1]
#This describes the position I want each tick to be on a graph with x axis from -1 to 1.
#done by doing (2-min(height))/(max(height)-min(height)) to find where 2 should be 
#positioned on the axis.
ticks_y = [-1,-3/4,-2/4,-1/4,2413/11593,4643/11593,7143/11593,9643/11593,1.047442422]
ax.set_xticks(ticks_x)
ax.set_yticks(ticks_y)
Ticks_x = [6,5,4,3,2,26,27,28,29]
Ticks_y = [29,28,27,26,50,100,150,200,250]
ax.set_xticklabels(Ticks_x)
ax.set_yticklabels(Ticks_y)
ax.spines['left'].set_position(('center'))
ax.spines['bottom'].set_position(('center'))
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.tick_params(axis='x', colors='black', direction='out', length=10, width=1)
ax.tick_params(axis='y', colors='black', direction='out', length=10, width=1)

#Graph Title.
plt.title('Calder Graph')

#Graph Labels.
plt.text(-0.7, -1,'$h_t$')
plt.text(-13/15, -1,'$h_m$')
plt.text(1, scaledqm,'$Q_m$')
plt.text(1, scaledqt,'$Q_t$')
plt.text(0.45,0.675,'F.E.V.', size=15)
plt.text(0.355,-0.19,'$T_f$',size=13)
plt.text(0.331,-0.212,'<')
plt.text(0.4,-0.212,'>')

#Axis Labels.
plt.text(0, 1.05,'Flow $[m^3/s]$', size=10)
plt.text(0.75, -0.13,'Day in December', size=10)
plt.text(-0.35, -1.09,'Day in December', size=10)
plt.text(-1.1, 0.02,'Height $[m]$', size=10)

#Arrows at end of Axis.
plt.text(-0.015,1.07,'^')
plt.text(-0.011,-1.11,'v')
plt.text(1.08,-0.015,'>')
plt.text(-1.1,-0.015,'<')

#Text on Graph.
plt.text(0.4,-0.4,'$F.E.V.≈--Mm^3$', size=15)
plt.text(0.4,-0.475,'$T_f=--hrs$', size=15)
plt.text(0.4,-0.55,'$h_t=4.5m$', size=15)
plt.text(0.4,-0.625,'$h_m=5.24m$', size=15)
plt.text(0.4,-0.7,'$Q_t=142.02m^3/s$', size=15)
plt.text(0.4,-0.775,'$Q_m=196.28m^3/s$', size=15)

#Fill in the F.E.V.
QT=[]
for i in scaledFlow:
    i = scaledqt
    QT.append(i)
#Because I have to make qt into a list otherwise I get an error because I'm comparing
#a list with a float.
a=np.array(scaledFlow)
b=np.array(QT)
#Puts lists into an array as opposed to a list. Means that Python finds it easier to
#compare the 2.
ax.fill_between(scaledday,a,b,where=a>=b,facecolor='forestgreen')