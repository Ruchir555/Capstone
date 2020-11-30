from sympy import *
import numpy as np
# import PHY483_A1_Q4

t, r, theta, phi, L, G, M, lamb = symbols('t r θ phi L G M Λ')
# L = symbols('L')


xup = Matrix([t, r, theta, phi])    #spatial components of x^mu
# print(xup)

gdndn = Matrix([[(1-(2*G*M/r) - (lamb*r**2/3)), 0, 0, 0],         #g_{munu}
                [0, -(1-(2*G*M/r) - (lamb*r**2/3))**(-1), 0, 0],
                [0, 0, -r**2, 0],
                [0, 0, 0, -(r**2)*(sin(theta))**2]])

gupup = gdndn.inv(method = 'GE')
# gupup = Matrix([[(1-(r**2/L**2))**(-1), 0, 0, 0],         #g^{munu}
#                 [0, -(1-(r**2/L**2)), 0, 0],
#                 [0, 0, -1/r**2, 0],
#                 [0, 0, 0, -1/((r**2)*(sin(theta))**2 )]])

Gammaupdndn = MutableDenseNDimArray.zeros(4, 4, 4)

print("Rank of Gammaupdndn:", Gammaupdndn.rank())   #3 - rank 3
print("Shape of Gammaupdndn:", Gammaupdndn.shape, '\n')    #(4,4,4) - 4*4*4 tensor
print("Gamma^{mu}_{nu, lambda}: \n"
      "[mu, nu, lambda]    Value \n")

counter = 0
for mu in range(0,4):
    for nu in range(0,4):
        for lamb in range(0,4):
            for sigma in range(0,4):
                Gammaupdndn[mu, nu, lamb] = (1/2)*gupup[mu, sigma]*(diff(gdndn[sigma, lamb], xup[nu]) + diff(gdndn[nu, sigma], xup[lamb]) - diff(gdndn[nu, lamb], xup[sigma]))
                if(Gammaupdndn[mu, nu, lamb] != 0):
                    print( '[', mu, nu, lamb, ']', '','','', simplify(Gammaupdndn[mu, nu, lamb]))
                    counter += 1
if (counter==0):
    print("No nonzero components of the Christoffels!")


Riemann_Tensor = MutableDenseNDimArray.zeros(4, 4, 4, 4) #4*4*4*4 Riemann Tensor
# print("\nRiemann Tensor:\n",Riemann_Tensor,'\n')                #initialize


print("\nRank of Riemann_Tensor:", Riemann_Tensor.rank())   #3 - rank 3
print("Shape of Riemann_Tensor:", Riemann_Tensor.shape, '\n')    #(4,4,4,4) - 4*4*4*4 tensor

def GAMMAUPDNDN(mu, nu, lamb):
    G = MutableDenseNDimArray.zeros(4, 4, 4)
    # for mu in range(0, 4):
    #     for nu in range(0, 4):
    #         for lamb in range(0, 4):
    for sigma in range(0, 4):
        G[mu, nu, lamb] += (1 / 2) * gupup[mu, sigma] * (diff(gdndn[sigma, lamb], xup[nu]) + diff(gdndn[nu, sigma], xup[lamb]) - diff(gdndn[nu, lamb], xup[sigma]))

    if (G[mu, nu, lamb] != 0):
        return G[mu, nu, lamb]
    else:
        return 0

def Riemann_4Tensor(rho, sigma, mu, nu):
    R = MutableDenseNDimArray.zeros(4, 4, 4, 4)
    R[rho, sigma, mu, nu] = diff(GAMMAUPDNDN(rho, sigma, nu), xup[mu]) - \
                            diff(GAMMAUPDNDN(rho, sigma, mu), xup[nu])
    for lamb in range(0, 4):    #add terms that sum over lambda separately to not double count
        R[rho, sigma, mu, nu] += GAMMAUPDNDN(lamb, sigma, nu) * GAMMAUPDNDN(rho, lamb, mu) \
                                 - GAMMAUPDNDN(lamb, sigma, mu) * GAMMAUPDNDN(rho, lamb, nu)

    if (R[rho, sigma, mu, nu] != 0):
        return R[rho, sigma, mu, nu]
    else:
        return 0

print("\n\nR^{rho}_{sigma, mu, nu}: \n"
      "[rho, sigma, mu, nu]    Value \n")
for rho in range(0,4):
    for sigma in range(0,4):
        for mu in range(0,4):
            for nu in range(0,4):
                if (Riemann_4Tensor(rho, sigma, mu, nu) != 0):
                    print('[', rho, sigma, mu, nu, ']', '', '', '', simplify(Riemann_4Tensor(rho, sigma, mu, nu)))

def Riemann_2Tensor(mu, nu):
    R = MutableDenseNDimArray.zeros(4, 4)

    for lamb in range(0, 4):    #add terms that sum over lambda separately to not double count
        R[mu, nu] += Riemann_4Tensor(lamb, mu, nu, lamb)

    if (R[mu, nu] != 0):
        return R[mu, nu]
    else:
        return 0

print("\nR_{mu, nu}: \n"
      "[mu, nu]    Value \n")
for mu in range(0, 4):
    for nu in range(0, 4):
        if (Riemann_2Tensor(mu, nu) != 0):
            print('[', mu, nu, ']', '', '', '', simplify(Riemann_2Tensor(mu, nu)))

def Ricci_scalar():
    R = 0
    for nu in range(0,4):
        for mu in range(0,4):
            R += Riemann_2Tensor(mu, nu)*gupup[nu, mu]
    return R

print('\nRicci scalar: ', simplify(Ricci_scalar()))

cosmological_constant = -Riemann_2Tensor(0,0)/gdndn[0,0] + Ricci_scalar()/2
print("Cosmological constant:", simplify(cosmological_constant))
