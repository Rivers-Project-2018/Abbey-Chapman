import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams["figure.figsize"] = [10,10]
plt.rcParams['axes.edgecolor']='white'
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

#finding and using ht from the hm.
#According to gaugemap.co.uk, the stage at which flooding is possible is at `~0.95m
#I added 20% on to this and decided to use 1.14 as my ht
ht=1.14
HM = []
for i in height:
    if i>=ht:
        HM.append(i)
hm=sum(HM)/len(HM)

#Finding qt and qm.
def Q(x):
    if x<=0.938 and x>=0.136:
        y = (158.04*((x-0.263)**2.854))
    elif x<=max(height) and x>0.938:
        y = (87.0362*((x-0.359)**0.962))
    return(y)
qt = Q(ht)
qm = Q(hm)   

#Rating Curve
Flow = []
for i in height:
    if i<=0.938 and i>=0.136:
        Flow.append(158.04*((i-0.263)**2.854))
    elif i<=max(height) and i>0.938:
        Flow.append(87.0362*((i-0.359)**0.962))

scaledFlow = []
for i in Flow:
    scaledFlow.append((i-min(Flow))/(max(Flow)-min(Flow)))


#Plot the Rating Curve using Q NOT the Flow Rate.
negheight = -scaledheight
ax.plot(negheight,scaledFlow,'black',linewidth=2)
ax.plot([0,-1],[0,1],'tomato',linestyle='--', marker='', linewidth=2)
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
ax.plot([0.075,0.075,0.075],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([0.735,0.735,0.735],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([0.075,0.735],[-1/5,-1/5], 'black', linewidth=1)
ax.plot([0.075,0.075],[scaledqm,scaledqt], 'black',linewidth=1.5)
ax.plot([0.075,0.735],[scaledqm,scaledqm], 'black',linewidth=1.5)
ax.plot([0.075,0.735],[scaledqt,scaledqt], 'black',linewidth=1.5)
ax.plot([0.735,0.735],[scaledqm,scaledqt], 'black',linewidth=1.5)

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
plt.title('Stratford-upon-Avon Graph')

#Graph labels.
plt.text(-0.37, -1,'$h_t$')
plt.text(-0.78, -1,'$h_m$')
plt.text(1, scaledqm,'$Q_m$')
plt.text(1, scaledqt,'$Q_t$')
plt.text(0.75,0.63,'F.E.V.', size=15)
plt.text(0.4,-0.18,'$T_f$',size=13)
plt.text(0.07,-0.21,'<')
plt.text(0.72,-0.21,'>')

#Axis Labels.
plt.text(0, 1.05,'Flow Rate $[m^3/s]$', size=10)
plt.text(0.75, -0.13,'Day in November', size=10)
plt.text(-0.35, -1.09,'Day in November', size=10)
plt.text(-1.1, 0.02,'Height $[m]$', size=10)

#Arrows at end of Axis.
plt.text(-0.015,1.07,'^')
plt.text(-0.011,-1.11,'v')
plt.text(1.08,-0.01,'>')
plt.text(-1.11,-0.01,'<')

#Text on Graph.
plt.text(0.4,-0.4,'$F.E.V.≈24.23Mm^3$', size=15)
plt.text(0.4,-0.475,'$T_f=159.19hrs$', size=15)
plt.text(0.4,-0.55,'$h_t=1.14m$', size=15)
plt.text(0.4,-0.625,'$h_m=1.65m$', size=15)
plt.text(0.4,-0.7,'$Q_t=68.62m^3/s$', size=15)
plt.text(0.4,-0.775,'$Q_m=110.89m^3/s$', size=15)

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
ax.fill_between(scaledday,a,b,where=a>=b,facecolor='tomato')

#Find the Tf
idx = np.argwhere(np.diff(np.sign(b - a))).flatten()
print(scaledday[idx])
def unscaleday(x):
    return (((max(day)-min(day))*x)+min(day))
c=unscaleday(0.074)
d=unscaleday(0.738)
Tf=(d-c)*24
#find Tf in seconds
Tfs=Tf*(60**2)

#Find F.E.V
FEV=(qm-qt)*Tfs