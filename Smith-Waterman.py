import pandas as pd
import numpy as np

gap_penalty=-2
match_score=+3
mismatch_score=-4

def initialize(r,c):
    mat=np.zeros((r+1,c+1))
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

def matrix(mat,match_table):
    for i in range(1,mat.shape[0]):
        for j in range(1,mat.shape[1]):
            a=mat[i-1,j]+gap_penalty
            b=mat[i,j-1]+gap_penalty
            c=mat[i-1,j-1]+match_table[i-1,j-1]
            if(max(a,b,c)<0):
                mat[i,j]=0
            else:
                mat[i,j]=max(a,b,c)
    return(mat)

def backtracking(mat,match_table,seq1,seq2):
    max_ele=np.unravel_index(np.argmax(mat, axis=None), mat.shape)
    a=""
    b=""
    i=max_ele[0]
    j=max_ele[1]
    while(mat[i,j]!=0 and (i>0 or j>0)):
        if(i>0 and j>0 and mat[i,j]==mat[i-1,j-1]+match_table[i-1,j-1]):
            a=seq1[i-1]+a
            b=seq1[i-1]+b
            i = i-1
            j = j-1
        elif(i>0 and mat[i,j]==mat[i-1,j]+gap_penalty):
            a='_'+a
            b=seq1[i-1]+b
            i =i-1
        else:
            b = '_' +b
            a=seq2[j-1]+a
            j =j-1
    return(a,b)

def s_w(seq1,seq2):
    seq1=seq1.lower()
    seq2=seq2.lower()
    mat=initialize(len(seq1),len(seq2))
    match_table=match(seq1,seq2)
    mat=matrix(mat,match_table)
    print(mat)
    alignment=backtracking(mat,match_table,seq1,seq2)
    return(alignment)

print("Result is :")
print("Input is ('gcgatata','aacctatagct')")
print(s_w('gcgatata','aacctatagct'))