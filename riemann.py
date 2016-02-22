#!/usr/bin/env python
# Grant David Meadors
# 02016-02-22 (JD 2457441)
# g r a n t . m e a d o r s @ a e i . m p g . d e
# Experimenting with the Riemann tensor
print 'Hello'

import numpy as np
dimension = 4
indices = np.arange(4)
zeros = np.zeros_like(indices)
ag, bg = np.meshgrid(zeros,zeros)
g_munu = ag

def derivative(f, mu):
    print f 
