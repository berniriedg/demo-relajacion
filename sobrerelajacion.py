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


# Setup de discretizacion
Nptos = 5
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
w = 1
for i in range(1, Nptos-1):
    for j in range(1, Nptos-1):
        phi[i,j] = ((1 - w) * phi[i, j] +
                    w / 4 * (phi[i+1, j] + phi[i-1, j] +
                             phi[i, j+1] + phi[i, j-1] +
                             h**2 * q(i, j, h)))










