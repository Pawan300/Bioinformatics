import pandas as pd
import numpy as np

gap_penalty=-1    #You can change this score 
match_score=2
mismatch_score=-1

def initialize(r,c):
    mat=np.zeros((r+1,c+1))
    mat[0]=[-i for i in range(len(mat[0]))]
    mat[:,0]=[-i for i in range(len(mat[:,0]))]
    return(mat)

def match(seq1,seq2):
    mat=np.ones((len(seq1),len(seq2)))
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if(seq1[i]==seq2[j]):
                mat[i,j]=match_score
            else:
                mat[i,j]=mismatch_score
    return(mat)

def backtrack(mat,seq1,seq2,match_table):
    a_a=""
    a_b=""
    i=len(seq1)
    j=len(seq2)
    while(i>0 or j>0):
        if(i>0 and j>0 and mat[i,j]==mat[i-1,j-1]+match_table[i-1,j-1]):
            a_a = seq1[i-1] + a_a
            a_b = seq2[j-1] + a_b
            i = i-1
            j = j-1
        elif(i>0 and mat[i,j]==mat[i-1,j]+gap_penalty):
            a_a = seq1[i-1] + a_a
            a_b = '_' + a_b
            i =i-1
        else:
            a_a = '_' + a_a
            a_b = seq2[j-1] + a_b
            j =j-1            
    return(a_a,a_b)

def matrix(mat,match_table):
    for i in range(1,mat.shape[0]):
        for j in range(1,mat.shape[1]):
            a=mat[i-1,j]+gap_penalty
            b=mat[i,j-1]+gap_penalty
            c=mat[i-1,j-1]+match_table[i-1,j-1]
            mat[i,j]=max(a,b,c)
    return(mat)

def n_w(seq1,seq2):
    seq1=seq1.lower()
    seq2=seq2.lower()
    mat=initialize(len(seq1),len(seq2))
    match_table=match(seq1,seq2)
    mat=matrix(mat,match_table)
    alignment=backtrack(mat,seq1,seq2,match_table)
    print(mat)
    return(alignment)

print("Result is :")
print("Input is ('GLYCINE','CYSTEINE')")
print(n_w('GLYCINE','CYSTEINE'))