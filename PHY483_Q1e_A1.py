import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np

c = 3*10**8
v = 0.99*c
gamma = 1/(math.sqrt(1-(v**2)/(c**2)))
k=1
q=1
theta = 0

r = np.linspace(0,100,100)

def E(r, theta):
    return ((k*q)/((v**2 * gamma**2 / c**2)*(math.cos(theta))**2 +1)**(3/2)) * 1/r**(3/2)

E0 = E(r, 0)

fig, ax = plt.subplots()
# ax.plot(E0, r, 'b-', label = "Theta = 0")
ax.plot(E(r, 3*math.pi/2), r, 'r--', label = "Theta = 3pi/2")
# ax.plot(E(r, math.pi/4), r, 'g-', label = "Theta = pi/4")
ax.set(xlabel='r', ylabel='E(r, theta)',
       title='Plot of Electrical field E(r,t) at t=0')
legend = ax.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.ylim(-5,50)
ax.grid()
plt.show()

def B(r, theta):
    return ((k*q*gamma*v)/((v**2 * gamma**2 / c**2)*(math.cos(theta))**2 +1)**(3/2)) * 1/r**(3/2)

Bz = B(r, theta)
By = -B(r, theta)

fig, ax = plt.subplots()
ax.plot(B(r, 3*math.pi/2), r, 'g--', label = "Theta = 3pi/2")
ax.set(xlabel='z', ylabel='B(r, theta)',
       title='Plot of Magnetic field Bz at t=0')
legend = ax.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.ylim(-5,50)
ax.grid()
plt.show()

fig, ax = plt.subplots()
ax.plot(-B(r, 3*math.pi/2), r, 'b--', label = "Theta = 3pi/2")
ax.set(xlabel='y', ylabel='B(r, theta)',
       title='Plot of Magnetic field By at t=0')
legend = ax.legend(loc='upper left', shadow=True, fontsize='x-large')
plt.ylim(-5,50)
ax.grid()
plt.show()
