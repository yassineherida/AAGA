#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 18:24:01 2020

@author: herida
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:40:16 2020

@author: herida
"""
from hypothesis.strategies import integers, lists
from hypothesis import given
from hypothesis.stateful import rule, precondition, RuleBasedStateMachine

def inf (cle1,cle2):
    return int(cle1,16)<int(cle2,16)

def eg(cle1,cle2):
    return int(cle1,16)==int(cle2,16)
def parent2(i):
    if(i==0 or (i - 1) // 2 <0):
        return -1
    return (i - 1) // 2
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
def SupMin2(A):
    d=len(A)
    c=A[0]
    A[0]=A[d-1]
    B=A[0:d-1]
    MinHeap(B,0)
    return B,c

def Ajout(A,i):

    A=A+[i]
    pos=len(A)-1
    e=parent2(pos)
    MinHeap2(A,e)
    return A
   
def MinHeap(A,i):
    if (len(A)==0 or len(A)==1):
        return A
    l=gauche(i)
    r=droite(i)
    s=len(A)-1
    p=i
   # print(A)
    #print("i",i)
    #print ("a de i",A[i])
    if(l <=s ):
        #print ("left",A[l])
        if (A[l]<A[i]) :
            p=l
    if( r<=s ):
        #print ("right",A[r])
        if (A[r]<A[p]):
                p=r

    if (p !=i):
        stock=A[i]
        A[i]=A[p]
        A[p]=stock
        #print("p est",p)
        if (gauche(p)<=s or droite(p)<=s ):
            #print("next")
            #MinHeap2(A,i)
            MinHeap(A,p)
    #MinHeap(A,0)
def MinHeap2(A,i):
    l=gauche(i)
    r=droite(i)
    s=len(A)-1
    p=i
    if(l <=s):
        if (A[l]<A[i]):
            p=l
    if( r<=s):
        if (A[r]<A[p]):
                p=r
   
    if (p !=i):
        stock=A[i]
        A[i]=A[p]
        A[p]=stock
        if (parent(i)!=-1):
            MinHeap2(A,parent2(i))





def heapempty(heap):
    return not heap



@given(lists(integers()))
def test_croissant(ls):
    print(ls)
    h = []
    for l in ls:
        h=Ajout(h, l)
    r = []
    for i in range (0,len(h)):
        h,c=SupMin2(h)
        r.append(c)
    assert r == sorted(ls)
    
if __name__ == "__main__":
    print("yes")
    test_croissant()
print("fini")