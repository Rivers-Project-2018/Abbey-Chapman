import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

armley=pd.read_csv('Aire Data.csv')
day = armley['Day in December']
flow = armley['Flow Rate (m^3/s)']
height = armley['Height (m)']

fig, ax = plt.subplots(figsize=(5, 5))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position(('axes',0.045))
ax.spines['left'].set_position(('axes',0.045))
ax.tick_params(axis='x', colors='black', direction='out', length=10, width=1)
ax.tick_params(axis='y', colors='black', direction='out', length=10, width=1)

Q=[]
for i in height:
    if i<=0.685:
        Q.append(30.69*((i-0.156)**1.115))
    elif i<=1.917 and i>0.685:
        Q.append(27.884*((i-0.028)**1.462))
    elif i<=4.17 and i>1.917:
        Q.append(30.127*((i-0.153)**1.502))
#Need to figure out how Q is defined for i>4.17 in order to plot for all i in
#height.

a=[]
for i in height:
    if i<=4.17:
        a.append(i)
        
A = max(height)
B = max(flow)
#change to max(Q) when we figure out how to get Q for hight values of height.
ax.plot([0,A], [0,B], 'black', linestyle='--', marker='')

print(len(height))
print(len(Q))
print(len(a))
print(min(height))
print(max(height))

ax.plot(a,Q, 'blue', linewidth=5)

H = np.arange(0.165,max(a),0.001)
#this creates a list of all values from 0.165 to max(a), which is 4.17, in
#increments of 0.001, to the same degree of uncertainty as the data provided.
#I used 0.156 as it is the value of a in the first increment.

Q_2 = []
for i in H:
    if i<=0.685 and i>=0.156:
        Q_2.append(30.69*((i-0.156)**1.115))
#i>=0.156 because otherwise you get 'nan'i.e. a math error because you'd be
#doing (neg)^1.115
    elif i<=1.917 and i>0.685:
        Q_2.append(27.884*((i-0.028)**1.462))
    elif i<=4.17 and i>1.917:
        Q_2.append(30.127*((i-0.153)**1.502))

ax.plot(H,Q_2, 'black')


    

    



    
    
    
    



