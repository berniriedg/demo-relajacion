#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
En este script resolvemos el problema:
nabla^2 phi = q
q = 2 (2 - x^2 - y^2)
blah blah

usando el metodo de la sobre-relajacion.
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


# Setup de discretizacion
Nptos = 25
Lx = Ly = 2
h = Lx / (Nptos - 1)

phi = np.zeros((Nptos, Nptos))

def muestra(phi):
    print phi[::-1,:]

def q(i, j, h):
    # import ipdb; ipdb.set_trace()
    xi = i * h - 1
    yj = j * h - 1
    output = 2 * (2 - xi**2 - yj**2)
    return output


# una iteracion de sobre relajacion

def una_iteracion(phi, h, w=1):
    for i in range(1, Nptos-1):
        for j in range(1, Nptos-1):
            phi[i,j] = ((1 - w) * phi[i, j] +
                        w / 4 * (phi[i+1, j] + phi[i-1, j] +
                                 phi[i, j+1] + phi[i, j-1] +
                                 h**2 * q(i, j, h)))
    return phi

def no_ha_convergido(phi, phi_prev, tol_relativa):
    non_zero = phi != 0
    diff_relativa = (phi_prev[non_zero] - phi[non_zero]) / phi[non_zero]
    output = max(np.fabs(diff_relativa))
    return output > tol_relativa

tol_relativa = 1e-9
contador = 0
itermax = 10000

phi_prev = phi.copy()
phi = una_iteracion(phi, h)

while no_ha_convergido(phi, phi_prev, tol_relativa) and contador < itermax :
    phi_prev = phi.copy()
    phi = una_iteracion(phi, h)
    contador += 1

fig1 = plt.figure(1)
fig1.clf()
ax = fig1.add_subplot(111, projection='3d')

x = np.linspace(-1, 1, Nptos)
y = np.linspace(-1, 1, Nptos)
X, Y = np.meshgrid(x, y)

ax.plot_surface(X, Y, phi, rstride=1, cstride=1)
fig1.show()

fig2 = plt.figure(2)
fig2.clf()
ax2 = fig2.add_subplot(111)
ax2.imshow(phi, origin='bottom', interpolation='nearest')
ax2.contour(phi, origin='lower')

fig2.show()








