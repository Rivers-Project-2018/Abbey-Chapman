import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams["figure.figsize"] = [10,10]
plt.rcParams['axes.edgecolor']='white'
fig, ax = plt.subplots()

#Import the Data
Don=pd.read_csv('Don Data.csv')
day = Don['Day in December']
height = Don['Height (m)']

#Scale our Data
def scale(x):
    return ((x-min(x))/(max(x)-min(x)))
scaledday = scale(day)
scaledheight = scale(height)

#finding and using ht from the hm.
ht=2.9
HM = []
for i in height:
    if i>=ht:
        HM.append(i)
hm=sum(HM)/len(HM)

#Finding qt and qm.
def Q(x):
    if x<=0.52 and x>=0:
        y = (78.4407*((x-0.223)**1.7742))
    elif x<=0.931 and x>0.52:
        y = (77.2829*((x-0.3077)**1.3803))
    elif x<=1.436 and x>0.931:
        y = (79.5956*((x-0.34)**1.2967))
    elif x<=max(height) and x>1.436:
        y = (41.3367*((x+0.5767)**1.1066))
    return(y)
qt = Q(ht)
qm = Q(hm)   

#Rating Curve
Flow = []
for i in height:
    if i<=0.52 and i>=0:
        Flow.append(78.4407*((i-0.223)**1.7742))
    elif i<=0.931 and i>0.52:
        Flow.append(77.2829*((i-0.3077)**1.3803))
    elif i<=1.436 and i>0.931:
        Flow.append(79.5956*((i-0.34)**1.2967))
    elif i<=max(height) and i>1.436:
        Flow.append(41.3367*((i+0.5767)**1.1066))

scaledFlow = []
for i in Flow:
    scaledFlow.append((i-min(Flow))/(max(Flow)-min(Flow)))


#Plot the Rating Curve using Q NOT the Flow Rate.
negheight = -scaledheight
ax.plot(negheight,scaledFlow,'black',linewidth=2)
ax.plot([0,-1],[0,1],'gold',linestyle='--', marker='', linewidth=2)

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
ax.plot([1/8,1/8,1/8],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([107/400,107/400,107/400],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([1/8,107/400],[-1/5,-1/5], 'black', linewidth=1)
ax.plot([1/8,1/8],[scaledqm,scaledqt], 'black',linewidth=1.5)
ax.plot([1/8,107/400],[scaledqm,scaledqm], 'black',linewidth=1.5)
ax.plot([1/8,107/400],[scaledqt,scaledqt], 'black',linewidth=1.5)
ax.plot([107/400,107/400],[scaledqm,scaledqt], 'black',linewidth=1.5)

#Formatting the ticks and the Axis.
ticks_x = [-4481/4156,-3481/4156,-2481/4156,-1481/4156,-481/4156,1/4,2/4,3/4,1]
#This describes the position I want each tick to be on a graph with x axis from -1 to 1.
#done by doing (2-min(height))/(max(height)-min(height)) to find where 2 should be 
#positioned on the axis.
ticks_y = [-1,-3/4,-2/4,-1/4,1024/6249,758/2083,3524/6249,4774/6249,2008/2083,1.164026244]
ax.set_xticks(ticks_x)
ax.set_yticks(ticks_y)
Ticks_x = [6,5,4,3,2,26,27,28,29]
Ticks_y = [29,28,27,26,50,100,150,200,250,300]
ax.set_xticklabels(Ticks_x)
ax.set_yticklabels(Ticks_y)
ax.spines['left'].set_position(('center'))
ax.spines['bottom'].set_position(('center'))
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.tick_params(axis='x', colors='black', direction='out', length=10, width=1)
ax.tick_params(axis='y', colors='black', direction='out', length=10, width=1)

#Graph Title.
plt.title('Don Graph')

#Graph Labels.
plt.text(-0.57, -1,'$h_t$')
plt.text(-0.85, -1,'$h_m$')
plt.text(1, scaledqm,'$Q_m$')
plt.text(1, scaledqt,'$Q_t$')
plt.text(0.3,0.73,'F.E.V.', size=15)
plt.text(0.17,-0.19,'$T_f$',size=13)
plt.text(0.12,-0.212,'<')
plt.text(0.25,-0.212,'>')

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
plt.text(0.4,-0.55,'$h_t=2.90m$', size=15)
plt.text(0.4,-0.625,'$h_m=4.06m$', size=15)
plt.text(0.4,-0.7,'$Q_t=164.13m^3/s$', size=15)
plt.text(0.4,-0.775,'$Q_m=225.67m^3/s$', size=15)

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
ax.fill_between(scaledday,a,b,where=a>=b,facecolor='gold')