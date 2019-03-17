##Imput your own data here:##
#Your chosen threshold height.
ht=3.9

#Your rating curve coeffecients, listed starting from those corresponding to
#the lowest range of heights up until the heighest range.
a=[0.156,0.028,0.153]
b=[1.115,1.462,1.502]
c=[30.69,27.884,30.127]

#The upper and lower limits of the ranges of the river heights given for your
#rating curve.
lower_limits=[0.2,0.685,1.917]
upper_limits=[0.685,1.917,4.17]

#You do not have to change the following.
import matplotlib.pyplot as plt
import pandas as pd
fig, ax = plt.subplots()

#Import your data, your river height data must be saved into a csv file
#(we are using the file 'Aire Data.csv' but you must change what your csv file 
#is saved as) within the same folder as this code is saved. The first column must have the 
#heading 'Time', with time values converted into days (with the digits beyond the
#decimal point representing what the hours and seconds elapsed are in terms of a
#fraction of a day, more information on how to do this can be found at 
#https://github.com/Rivers-Project-2018/How-to-do-FEV-Analysis/blob/master/README.md) 
#and the second column must have the heading 'Height'.
Data=pd.read_csv('Aire Data.csv')
time=Data['Time']
height=Data['Height']

#####You do not have to change any of the rest of the code.#####
#But if you wish to change elements such as the colour or the x and y axis
#there are instructions on how to do so.
import bisect
import numpy as np

plt.rcParams["figure.figsize"] = [11,8]
plt.rcParams['axes.edgecolor']='white'
ax.spines['left'].set_position(('center'))
ax.spines['bottom'].set_position(('center'))
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')

time_increment=(time[1]-time[0])*24*3600

number_of_days=int((len(time)*(time[1]-time[0])))

def scale(x):
    return ((x-min(x))/(max(x)-min(x)))
scaledtime=scale(time)
scaledheight=scale(height)

w=[]
for i in range(len(a)):
    w.append(i)

def Q(x):
    z=0
    while z<w[-1]:
        if x>lower_limits[z] and x<=upper_limits[z]:
            y = (c[z]*((x-a[z])**b[z]))
            break
        elif x>upper_limits[z]:
            z = z+1
    else:
        y = (c[w[-1]]*((x-a[w[-1]])**b[w[-1]]))
    return(y)

qt = Q(ht)     
    
Flow = []
for i in height:
    Flow.append(Q(i))

scaledFlow = []
for i in Flow:
    scaledFlow.append((i-min(Flow))/(max(Flow)-min(Flow)))

negheight=-scaledheight
negday=-(scaledtime)

#To change the colour, change 'conrflowerblue' to another colour such as 'pink'.
ax.plot(negheight,scaledFlow,'black',linewidth=2)
ax.plot([0,-1],[0,1],'cornflowerblue',linestyle='--',marker='',linewidth=2)
ax.plot(scaledtime, scaledFlow,'black',linewidth=2)
ax.plot(negheight, negday,'black',linewidth=2)

scaledht = (ht-min(height))/(max(height)-min(height))
scaledqt = (qt-min(Flow))/(max(Flow)-min(Flow))

QT=[]
for i in scaledFlow:
    i = scaledqt
    QT.append(i)

SF=np.array(scaledFlow)
e=np.array(QT)
    
ax.fill_between(scaledtime,SF,e,where=SF>=e,facecolor='cornflowerblue')

idx = np.argwhere(np.diff(np.sign(SF - e))).flatten()

f=scaledtime[idx[0]]
g=scaledtime[idx[-1]]

def unscaletime(x):
    return (((max(time)-min(time))*x)+min(time))

C=unscaletime(f)
d=unscaletime(g)

Tf=(d-C)*24

time_increment=(time[1]-time[0])*24*3600

flow = []
for i in Flow:
    if i>=qt:
        flow.append((i-qt)*(time_increment))

FEV=sum(flow)

Tfs=Tf*(60**2)

qm=(FEV/Tfs)+qt
scaledqm = (qm-min(Flow))/(max(Flow)-min(Flow))

hm=((qm/c[-1])**(1/b[-1]))+a[-1]
scaledhm = (hm-min(height))/(max(height)-min(height))

ax.plot([-scaledht,-scaledht],[-1,scaledqt],'black',linestyle='--',linewidth=1)
ax.plot([-scaledhm,-scaledhm],[-1,scaledqm],'black',linestyle='--',linewidth=1)
ax.plot([-scaledht,1],[scaledqt,scaledqt],'black',linestyle='--',linewidth=1)
ax.plot([-scaledhm,1],[scaledqm,scaledqm],'black',linestyle='--',linewidth=1)

ax.plot([f,f,f],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([g,g,g],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([f,f],[scaledqm,scaledqt], 'black',linewidth=1.5)
ax.plot([f,g],[scaledqm,scaledqm], 'black',linewidth=1.5)
ax.plot([f,g],[scaledqt,scaledqt], 'black',linewidth=1.5)
ax.plot([g,g],[scaledqm,scaledqt], 'black',linewidth=1.5)
plt.annotate(s='', xy=(f-1/100,-1/5), xytext=(g+1/100,-1/5), arrowprops=dict(arrowstyle='<->'))

h=[]
for i in np.arange(1,number_of_days+1):
    h.append(i/number_of_days)

#If you wish to set the flow to be shown on the axis by a certain increment, change all 
#appearances of 50 in lines 153 and 157 to the desired increment, e.g 25 or 100.
#Otherwise leave as is.
l=np.arange(0,max(Flow)+50,50)
m=bisect.bisect(l,min(Flow))

n=[]
for i in np.arange(l[m],max(Flow)+50,50):
    n.append(int(i))

#If you wish to set the height to be shown on the axis by a certain increment, change all 
#appearances of 1 in lines 163 and 167 to the desired increment, e.g 0.25 or 0.5.
#Otherwise leave as is.
o=np.arange(0,max(height)+1,1)
p=bisect.bisect(o,min(height))

q=[]
for i in np.arange(o[p],max(height)+1,1):
    q.append(i)

k=[]
for i in q:
    k.append(-(i-min(height))/(max(height)-min(height))) 

j=[]
for i in n:
    j.append((i-min(Flow))/(max(Flow)-min(Flow)))

ticks_x=k+h

r=[]
for i in h:
    r.append(-i)

ticks_y=r+j


s=[]
for i in np.arange(1,number_of_days+1):
    s.append(i)

Ticks_x=q+s
Ticks_y=s+n
    
ax.set_xticks(ticks_x)
ax.set_yticks(ticks_y)
ax.set_xticklabels(Ticks_x)
ax.set_yticklabels(Ticks_y)

ax.tick_params(axis='x',colors='black',direction='out',length=9,width=1)
ax.tick_params(axis='y',colors='black',direction='out',length=10,width=1)

plt.text(-scaledht+1/100, -1,'$h_T$', size=13)
plt.text(-scaledhm+1/100, -1,'$h_m$', size=13)
plt.text(1, scaledqm,'$Q_m$', size=13)
plt.text(1, scaledqt,'$Q_T$', size=13)
plt.text(((f+g)/2)-1/50,-0.18,'$T_f$',size=13)

plt.text(0.01, 1.05,'$Q$ [m$^3$/s]', size=13)
plt.text(0.95, -0.17,'$t$ [day]', size=13)
plt.text(0.01, -1.09,'$t$ [day]', size=13)
plt.text(-1.1, 0.02,'$\overline {h}$ [m]', size=13)

ax.scatter(0,0,color='white')

A=round(FEV/(10**6),2)
B=round(Tf,2)
C=round(ht,2)
D=round(hm,2)
E=round(qt,2)
F=round(qm,2)

plt.text(0.4,-0.4,'$FEV$ ≈ '+ str(A) +'Mm$^3$', size=15)
plt.text(0.4,-0.475,'$T_f$ = '+ str(B) +'hrs', size=15)
plt.text(0.4,-0.55,'$h_T$ = '+ str(C) +'m', size=15)
plt.text(0.4,-0.625,'$h_m$ = '+ str(D) +'m', size=15)
plt.text(0.4,-0.7,'$Q_T$ = '+ str(E) +'m$^3$/s', size=15)
plt.text(0.4,-0.775,'$Q_m$ = '+ str(F) +'m$^3$/s', size=15)