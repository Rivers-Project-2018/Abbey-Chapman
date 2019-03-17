import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [10,10]
plt.rcParams['axes.edgecolor']='white'


plt.xlim(0,2200)
plt.ylim(0,2200)

plt.xlabel('x (m)', size=17)
plt.ylabel('y (m)',size=17)

plt.arrow(0,1900,1130,0,head_width=25,head_length=25,color='black')
plt.arrow(1161,1900,-1120,0,head_width=25,head_length=25,color='black')

plt.arrow(1161,490,960,0,head_width=25,head_length=25,color='black')
plt.arrow(2150,490,-955,0,head_width=25,head_length=25,color='black')

plt.arrow(0,1250,2120,0,head_width=25,head_length=25,color='black')
plt.arrow(2150,1250,-2120,0,head_width=25,head_length=25,color='black')

plt.plot([0,2150],[0,0],linewidth=5,color='black')
plt.plot([0,0],[0,2150],linewidth=5,color='black')
plt.plot([2150,2150],[2150,0],linewidth=3,color='black')
plt.plot([0,2150],[2150,2150],linewidth=3,color='black')

plt.plot([1161,1161],[0,2150],linewidth=3,color='black')
plt.plot([580.5,580.5],[0,2150],linewidth=3,color='black')

plt.text(50,1950,'Cononley Washlands/Holden Park: 50.4%',fontsize=15,color='blue',fontweight='demibold')
plt.text(410,1830,'£35M or £0.69M/1%',fontsize=15,color='blue')

plt.text(1350,1170,'£70.1M or £0.7M/1%',fontsize=15,color='black')

plt.text(1300,520,'Higher Walls: 49.6%',fontsize=15,color='black',fontweight='demibold')
plt.text(1300,430,'£35.1M or £0.707M/1%',fontsize=15,color='black')

ticksx=[500,1000,1500,2000]
ticksy=[500,1000,1500,2000]

plt.xticks(ticksx)
plt.yticks(ticksy)

plt.tick_params(labelsize=15)