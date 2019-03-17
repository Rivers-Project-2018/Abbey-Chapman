import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=plt.figaspect(1)*0.7)
ax = Axes3D(fig)

plt.rcParams['axes.edgecolor']='white'
plt.rcParams["figure.figsize"] = [10,8]

ax.grid(False)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

ax.xaxis.pane.set_edgecolor('w')
ax.yaxis.pane.set_edgecolor('w')
ax.zaxis.pane.set_edgecolor('w')

sl = 956.56

a = [sl, sl]
b = [sl, sl]
c = [2, 0]

d = [sl, 0]
e = [sl, sl]
f = [0, 0]

g = [sl, sl]
h = [sl, 0]
i = [0, 0]

ax.plot(a, b, c, '--', color = 'k')
ax.plot(d, e, f, '--', color = 'k')
ax.plot(g, h, i, '--', color = 'k')

x = [sl, sl, sl, 0, 0, 0, sl, sl, 0, 0, 0, 0]
y = [sl, 0, 0, 0, 0, sl, sl, 0, 0, 0, sl, sl]
z = [2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0, 2]

ax.plot(x, y, z, color = 'k')

ax.text(650, -520, 0, 'Side-length [m]', size=13)
ax.text(-225, 350, 0, 'Side-length [m]', size=13)
ax.text(-50, 900, 1.3, 'Depth [m]',size=13)

ax.text(1200, 300, 2.2, '956.56m', size=13)
ax.text(600, 1000, 2.25, '956.56m',size=13)

ax.set_zticks([0, 2])

ax.set_xlim(sl,0)
ax.set_ylim(0,sl)
ax.set_zlim(0,10)