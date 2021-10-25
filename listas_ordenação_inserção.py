# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 14:36:45 2021

@author: lucid
"""
def ordenacao_insercao(seq):
    for i in range(1,len(seq)):
        j=i
        while j>0 and seq[j-1]>seq[j]:
            t=seq[j]
            seq[j],seq[j-1]=seq[j-1],t
            j-=1
            


        
    return seq
print(ordenacao_insercao(seq))
    
