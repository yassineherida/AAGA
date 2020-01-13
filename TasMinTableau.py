from cle_comparaison import inf

import math


def parent(i):
    if(i==0):
        return -1
    if (i==1 or i == 2):
        return 0
    s=i/2
    if (i%2==0):
        return s-1
    return s
def gauche(i):
    return (2*i)+1
def droite(i):
    return (2*(i))+2

def SupMin(A):
    d=len(A)
    A[0]=A[d-1]
    B=A[0:d-1]
    MinHeap(B,0)
    return B
def Union(A,B):
    if(A==[]):
        return B
    if (B==[]):
        return A
    return BuildMin_Heap(A+B)
def ConsIter(A):
    return BuildMin_Heap(A)
def BuildMin_Heap(A):
    s=(len(A)-1)/2.0
    s=math.floor(s)
    s=int(s)
    for i in range(s,-1,-1):
        MinHeap(A,i)
    return A 


def Ajout(A,i):

    A=A+[i]
    pos=len(A)-1
    e=parent(pos)
    if(e==-1):
        return [i]
    MinHeap2(A,e)
    return A
def MinHeaper(A,i):
    MinHeap(A,i)
    return A
    
def MinHeap(A,i):
    
    l=gauche(i)
    r=droite(i)
    s=len(A)-1
    p=i
    
    if(l <=s):
        if (inf(A[l],A[i])) :
            p=l
    if( r<=s):
        if (inf(A[r],A[p])):
                p=r

    if (p !=i):
        stock=A[i]
        A[i]=A[p]
        A[p]=stock
        if (gauche(p)<=s and droite(p)<=s ):
            MinHeap(A,p)
def MinHeap2(A,i):
    l=gauche(i)
    r=droite(i)
    s=len(A)-1
    p=i
    if(l <=s):
        if (inf(A[l],A[i])):
            p=l
    if( r<=s):
        if (inf(A[r],A[p])):
                p=r
   
    if (p !=i):
        stock=A[i]
        A[i]=A[p]
        A[p]=stock
        if (parent(i)!=-1):
            MinHeap(A,parent(i))

