import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def dotplot(seq1,seq2):
    seq1=seq1.lower()
    seq2=seq2.lower()
    mat=np.zeros((len(seq1),len(seq2)))
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if(seq1[i]==seq2[j]):
                mat[i,j]=1
    return(mat)

mat=dotplot('AtagAA','AatctATa')
print("Matrix is :", mat)

print("Dot - plot is :")
plt.scatter(np.where(mat==1)[0],np.where(mat==1)[1])