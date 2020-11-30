from sympy import *


t, r, theta, phi, L = symbols('t r θ phi L')
# L = symbols('L')

xup = Matrix([t, r, theta, phi])    #spatial components of x^mu
# print(xup)

# gdndn = Matrix([[(1-(r**2/L**2)), 0, 0, 0],         #g_{munu}
#                 [0, -(1-(r**2/L**2))**(-1), 0, 0],
#                 [0, 0, -r**2, 0],
#                 [0, 0, 0, -(r**2)*(sin(theta))**2]])
# gupup = Matrix([[(1-(r**2/L**2))**(-1), 0, 0, 0],         #g^{munu}
#                 [0, -(1-(r**2/L**2)), 0, 0],
#                 [0, 0, -1/r**2, 0],
#                 [0, 0, 0, -1/( (r**2)*(sin(theta))**2 )]])
gdndn = Matrix([[1, 0, 0, 0],         #g_{munu}
                [0, 1, 0, 0],
                [0, 0, r**2, 0],
                [0, 0, 0, r**2 * sin(theta)**2]])
gupup = Matrix([[1, 0, 0, 0],         #g^{munu}
                [0, 1, 0, 0],
                [0, 0, 1/r**2, 0],
                [0, 0, 0, 1/((r**2)*(sin(theta))**2 )]])

# t, x, y, z= symbols('t x y z')
#
# xup = Matrix([t, x, y, z])    #spatial components of x^mu
# # print(xup)
#
# gdndn = Matrix([[1, 0, 0, 0],         #g_{munu}
#                 [0, -1, 0, 0],
#                 [0, 0, -1, 0],
#                 [0, 0, 0, -1]])
# gupup = Matrix([[1, 0, 0, 0],         #g^{munu}
#                 [0, -1, 0, 0],
#                 [0, 0, -1, 0],
#                 [0, 0, 0, -1]])
# print(gupup[10])
# print(gdndn)
Gammaupdndn = MutableDenseNDimArray([ [[1, 0, 0, 0],         #g_{munu}
                [0, -1, 0, 0],
                [0, 0, -1, 0],
                [0, 0, 0, -1]],

                [[1, 0, 0, 0],  # g_{munu}
                                       [0, -1, 0, 0],
                                       [0, 0, -1, 0],
                                       [0, 0, 0, -1]],

                                      [[1, 0, 0, 0],  # g_{munu}
                                       [0, -1, 0, 0],
                                       [0, 0, -1, 0],
                                       [0, 0, 0, -1]],

                                      [[1, 0, 0, 0],  # g_{munu}
                                       [0, -1, 0, 0],
                                       [0, 0, -1, 0],
                                       [0, 0, 0, -1]] ])

print("Rank of Gammaupdndn:", Gammaupdndn.rank())   #3 - rank 3
print("Shape of Gammaupdndn:", Gammaupdndn.shape, '\n')    #(4,4,4) - 4*4*4 tensor
print("Gamma^{mu}_{nu, lambda}: \n"
      "[mu, nu, lambda]    Value \n")

Gupdndn_copy = MutableDenseNDimArray.zeros(4,4,4)
print(Gupdndn_copy)

counter = 0
for mu in range(0,4):
    for nu in range(0,4):
        for lamb in range(0,4):
            for sigma in range(0,4):
                Gammaupdndn[mu, nu, lamb] = (1/2)*gupup[mu, sigma]*(diff(gdndn[sigma, lamb], xup[nu]) + diff(gdndn[nu, sigma], xup[lamb]) - diff(gdndn[nu, lamb], xup[sigma]))

                if(Gammaupdndn[mu, nu, lamb] != 0):
                    print( '[', mu, nu, lamb, ']', '','','', Gammaupdndn[mu, nu, lamb])
                    counter += 1
                Gupdndn_copy[mu, nu, lamb] = Gammaupdndn[mu, nu, lamb]
if (counter==0):
    print("No nonzero components of the Christoffels!")

print(Gupdndn_copy)
print(Gammaupdndn[0,1,1])
print(Gupdndn_copy[0,1,1])
print(Gupdndn_copy[3,3,2])
print(Gammaupdndn[3,3,2])
print(gdndn[1,1])
print(diff(gdndn[1,1], xup[1]))

# a = MutableDenseNDimArray.zeros(4,4,4)
# b = MutableDenseNDimArray.zeros(4,4,4)
# print(a)
# a[1,1,1] = 3
# for i in range(0,4):
#     a[i,1,1] = L
#     b[i,1,1] = a[i,1,1]
# print(a)
# print(b)