#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
En este script resolvemos el problema:
nabla^2 phi = q
q = 2 (2 - x^2 - y^2)
blah blah

usando el metodo de la sobre-relajacion.
'''

import numpy as np


# Setup de discretizacion
Nptos = 5
Lx = Ly = 2
h = Lx / (Nptos - 1)

phi = np.zeros((Nptos, Nptos))







