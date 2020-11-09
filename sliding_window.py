import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def sliding_window(window,threshhold,seq1,seq2):
    seq1=seq1.lower()
    seq2=seq2.lower()
    result=[]
    if(len(seq1)>len(seq2)):
        seq2=seq2+'-'*(len(seq1)-len(seq2))
    else:
        seq1=seq1+'-'*(len(seq2)-len(seq1))
    i=0
    while(i<max(len(seq1),len(seq2))/window):
        s1=seq1[window*i:window*(i+1)]
        k=0
        while(k<len(seq2)/window):
            count=0
            s2=seq2[window*k:window*(k+1)]
            for l in range(0,min(len(s1),len(s2))):
                if(s1[l]==s2[l]):
                    count+=1
            if(count>=threshhold):
                result.append((i,k))
            k=k+1
        i=i+1
    return(result)

def dotplot(mat):
    l=[]
    r=[]
    for i in mat:
        l.append(i[0])
        r.append(i[1])
    plt.scatter(l,r)

seq1='aAGatACGCGtTCGgagtcgacgtagggatgctggatcgtagctgatcgatgatgatgctagctaggataatgagtagtaggatgatgagatgagatga'
seq2='AAGATagacgtgcatgcgtgcgggcccaaaattttggcacgtcagtgcagtcaatgagctagatcgagtaatgatgtagatagagtagatagcagatag'
dotplot(sliding_window(10,5,seq1,seq2))