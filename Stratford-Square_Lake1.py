import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [10,10]
plt.rcParams['axes.edgecolor']='white'


plt.xlim(0,1000)
plt.ylim(0,1000)

plt.xlabel('x [m]', size=17)
plt.ylabel('y [m]',size=17)

measure=['Brooks: £2.2M for 2.62% of FEV','Stanford reservoir pumps:£5.13M for 12.4% of FEV']



plt.plot([0,954],[0,0],linewidth=5,color='black')
plt.plot([0,0],[0,954],linewidth=5,color='black')
plt.plot([956.56,956.56],[956.56,0],linewidth=3,color='black')
plt.plot([0,956.56],[956.56,956.56],linewidth=3,color='black')

plt.bar(12.53,956.56,width=25.06,color='orange',label="Brooks: £2.2M for 2.62% of FEV")
plt.bar(84.37,956.56,width=118.61,color='cornflowerblue',label="Stanford reservoir pumps: £5.13M for 12.4% of FEV")
plt.bar(158.31,956.56,width=29.27,color='red',label="Stanford reservoir spillway: £1.17M for 3.06% of FEV")
plt.bar(564.75,956.56,width=784.07,color='purple',label="Temporary flood barriers: £[10.22,10.38]M for 81.92% of FEV")

ticksx=[100,200,300,400,500,600,700,800,900]
ticksy=[100,200,300,400,500,600,700,800,900]

plt.xticks(ticksx)
plt.yticks(ticksy)

plt.tick_params(labelsize=15)

plt.legend(bbox_to_anchor=(0.015, 0.55), loc=2, borderaxespad=0.,prop={'size': 15})
