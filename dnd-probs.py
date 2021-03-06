import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Hardcoded Values
DC = 14
oppCon = 2

def ADD(vals1, vals2):
    '''Adds probability values for comp1 abd comp2'''
    probs = []
    for i in vals1:
        for j in vals1:
            probs.append(i+j)
    return probs

def computeProbs(n, s, plus=0, extra=None):
    '''Computes outcomes for a roll of nDs+add'''
    out = None
    if n==1:
        out = range(1+plus,s+1+plus)
    else:
        comp1 = computeProbs(n-1, s, plus, extra)
        comp2 = computeProbs(1, s, plus, extra)
        out = ADD(comp1,comp2)

    if extra=='halfOnSave':
        pSave = 20+oppCon-DC

    return out

def chart(rolls):
    total = []
    boundMin = 100
    boundMax = 0
    for roll in rolls:
        nStr,sStr = roll.split('d')
        n = int(nStr)
        s = int(sStr)
        x = computeProbs(n,s)
        # have to add this line to fix the automatic bins
        boundMin = min(min(x),boundMin)
        boundMax = max(max(x),boundMax)
        total.append(x)

    bins = range(boundMin, boundMax+2)
    plt.hist(total, bins=bins, label=rolls)
    plt.legend(loc='upper right')
    plt.show()