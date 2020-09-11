import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def cost_1(z):
    return -np.log(sigmoid(z))

def cost_1(z):
    return -np.log(sigmoid(z))

def cost_0(z):
    return -np.log(1.0 - sigmoid(z))

#plot of sigmoid
z = np.arange(-7, 7, 0.1)
phi_z = sigmoid(z)
plt.plot(z, phi_z)
plt.axvline(0.0, color='k')
plt.ylim(-0.1, 1.1)
plt.xlabel('$z$')
plt.ylabel("$\phi (z)$")
plt.yticks([0.0, 0.5, 1.0])
plt.title("Sigmoid function")
plt.tight_layout()
plt.show()

#plot of sigmoid
plt.clf()
z = np.arange(-10, 10, 0.1)
print(z)
phi_z = sigmoid(z)
#cal cost function at y = 1
c1 = [cost_1(x) for x in z]
plt.plot(phi_z, c1, label='J(w) if y=1')
#cal cost function at y = 0
c0 = [cost_0(x) for x in z]
#print(c0)
plt.plot(phi_z, c0, label='J(w) if y=0', linestyle='--')
plt.ylim(0.0, 5.1)
plt.xlim([0, 1])
plt.xlabel('$\phi$ (z)')
plt.ylabel('J(w)')
plt.legend(loc='upper center')
plt.tight_layout()
plt.show()

