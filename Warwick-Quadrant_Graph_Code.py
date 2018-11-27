import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams["figure.figsize"] = [10,10]
plt.rcParams['axes.edgecolor']='white'
fig, ax = plt.subplots()

#Import the Data
Warwick=pd.read_csv('Warwick Data.csv')
day = Warwick['Day in November']
height = Warwick['Height (m)']

#Scale our Data
def scale(x):
    return ((x-min(x))/(max(x)-min(x)))
scaledday = scale(day)
scaledheight = scale(height)

#finding and using ht from the hm.
#According to gaugemap.co.uk, the stage at which flooding is possible is at ~1.5m
#I added 20% on to this and decided to use 1.8 as my ht
ht=1.8
HM = []
for i in height:
    if i>=ht:
        HM.append(i)
hm=sum(HM)/len(HM)

#Finding qt and qm.
def Q(x):
    if x<=max(height) and x>=0.960:
        y = (40.617*((x-0.917)**1.448))
    return(y)
qt = Q(ht)
qm = Q(hm)   

#Rating Curve
Flow = []
for i in height:
    if i<=max(height) and i>=0.960:
        Flow.append(40.617*((i-0.917)**1.448))

scaledFlow = []
for i in Flow:
    scaledFlow.append((i-min(Flow))/(max(Flow)-min(Flow)))


#Plot the Rating Curve using Q NOT the Flow Rate.
negheight = -scaledheight
ax.plot(negheight,scaledFlow,'black',linewidth=2)
ax.plot([0,-1],[0,1],'orange',linestyle='--', marker='', linewidth=2)
#Originally the dotted line was wrong because it went to the positional origin
#and not the actual origin.

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
ax.plot([0.05,0.05,0.05],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([0.775,0.775,0.775],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([0.05,0.775],[-1/5,-1/5], 'black', linewidth=1)
ax.plot([0.05,0.05],[scaledqm,scaledqt], 'black',linewidth=1.5)
ax.plot([0.05,0.775],[scaledqm,scaledqm], 'black',linewidth=1.5)
ax.plot([0.05,0.775],[scaledqt,scaledqt], 'black',linewidth=1.5)
ax.plot([0.775,0.775],[scaledqm,scaledqt], 'black',linewidth=1.5)

#Formatting the ticks and the Axis.
ticks_x = [-2241/2059,-1741/2059,-1241/2059,-741/2059,-241/2059,1/10,2/10,3/10,4/10,5/10,6/10,7/10,8/10,9/10,1]
#This describes the position I want each tick to be on a graph with x axis from -1 to 1.
#done by doing (2-min(height))/(max(height)-min(height)) to find where 2 should be 
#   positioned on the axis.
ticks_y = [-1,-9/10,-8/10,-7/10,-6/10,-5/10,-4/10,-3/10,-2/10,-1/10,47/387,829/2709,443/903,1829/2709,2329/2709,943/903]
ax.set_xticks(ticks_x)
ax.set_yticks(ticks_y)
Ticks_x = [3.5,3,2.5,2,1.5,22,23,24,25,26,27,28,29,30,1]
Ticks_y = [1,30,29,28,27,26,25,24,23,22,25,50,75,100,125,150]
ax.set_xticklabels(Ticks_x)
ax.set_yticklabels(Ticks_y)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.tick_params(axis='x', colors='black', direction='out', length=8, width=1)
ax.tick_params(axis='y', colors='black', direction='out', length=8, width=1)

#Graph Title.
plt.title('Warwick Graph')

#Graph labels.
plt.text(-0.25, -1,'$h_t$')
plt.text(-0.65, -1,'$h_m$')
plt.text(1, scaledqm,'$Q_m$')
plt.text(1, scaledqt,'$Q_t$')
plt.text(0.8,0.36,'F.E.V.', size=15)
plt.text(0.4,-0.18,'$T_f$',size=13)
plt.text(0.04,-0.21,'<')
plt.text(0.76,-0.21,'>')

#Axis Labels.
plt.text(0, 1.05,'Flow Rate $[m^3/s]$', size=10)
plt.text(0.8, -0.13,'Day in November', size=10)
plt.text(-0.35, -1.09,'Day in November', size=10)
plt.text(-1.1, 0.02,'Height $[m]$', size=10)

#Arrows at end of Axis.
plt.text(-0.015,1.07,'^')
plt.text(-0.011,-1.11,'v')
plt.text(1.08,-0.011,'>')
plt.text(-1.11,-0.011,'<')

#Text on Graph.
plt.text(0.4,-0.4,'$F.E.V.≈--Mm^3$', size=15)
plt.text(0.4,-0.475,'$T_f=--hrs$', size=15)
plt.text(0.4,-0.55,'$h_t=1.80m$', size=15)
plt.text(0.4,-0.625,'$h_m=2.62m$', size=15)
plt.text(0.4,-0.7,'$Q_t=33.92m^3/s$', size=15)
plt.text(0.4,-0.775,'$Q_m=87.85m^3/s$', size=15)

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
ax.fill_between(scaledday,a,b,where=a>=b,facecolor='orange')