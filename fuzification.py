# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:09:15 2019

@author: ASUA
"""

import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

x=np.arange(0,5.05,0.1)
mfx=fuzz.trapmf(x,[2,2.5,3,4.5])

defuzz_centroid = fuzz.defuzz(x,mfx,'centroid')
defuzz_bisector = fuzz.defuzz(x,mfx,'bisector')
defuzz_mom =fuzz.defuzz(x,mfx,'mom')
defuzz_fom = fuzz.defuzz(x,mfx,'som')
defuzz_lom = fuzz.defuzz(x,mfx,'lom')
print(defuzz_centroid)
print(defuzz_bisector)
print(defuzz_mom)
print(defuzz_fom)
print(defuzz_lom)


labels=['centroid','bisector','mean of maximum','first of maximum','last of maximum']
xvals=[defuzz_centroid,
       defuzz_bisector,
       defuzz_mom,
       defuzz_fom,
       defuzz_lom]
colors = ['r','b','g','c','m']
ymax = [fuzz.interp_membership(x,mfx,i) for i in xvals]
print(ymax)

plt.figure(figsize=(8,5))

plt.plot(x,mfx,'k')
for xv, y,label, color in zip(xvals, ymax, labels, colors):
    plt.vlines(xv,0,y,label=label,color=color)
    plt.ylabel('Fuzzy membership')
    plt.xlabel('Universe variable (arb)')
    plt.ylim(-0.1,1.1)
    plt.legend(loc=2)
    
    plt.show()