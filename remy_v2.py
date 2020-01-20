# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def rand48(m, a, c, g, n):
    if(n==0):
        return g
    else:
        res = (a *rand48(m, a, c, g, n-1) + c)%m
        return res

tab = 123456789+2**40
btab=""
graine = 123456789+2**40
modulo = 2**48
c = 11
a = 25214903917
n = 1
cpt=0
def bit_suivant():
     global btab
     global tab,cpt,n
     if(cpt == 0):
        cpt=48
        tab = rand48(modulo, a, c, tab, n) 
        #print(tab)
        if(n==2):
            n=1
        btab = tab
        
     bit = btab%2
     btab=btab//2
     cpt-=1
     #btab = btab[1:]
     return bit

rand48(2**48, 25214903917, 11, 0, 10)

def genInt(n):
    nbbits=1
    e=n+1
    n2=n
    while(n//2!=0):
        nbbits+=1
        n=n//2
    while (e>n2):
        e=0
        for i in range (nbbits):
            
            z=bit_suivant()
            
            e=e+z*(2**i)
    return e



class Tree:
    def __init__(self, gauche, droite,parent, racine = False):
        self.racine = racine
        self.gauche = gauche 
        self.droite = droite
        self.parent=parent
        
    
def arbre2str(t):
    if(t.gauche == None and t.droite == None):
        return "()"
    
    else:
        print("ici")
        return "( "+arbre2str(t.gauche) + " " + arbre2str(t.droite) +" )" 

def writeTree(t):
    res = arbre2str(t)
    
    f = open("str.txt","w").write(res)
    f.close()
    return res

"""n1 = Tree(None, None)
n2 = Tree(None, None)
n3 = Tree(None, None)
n4 = Tree(n1, n2)
n5 = Tree(n3,n4, True)"""



def remy(n):
    tab1 = []
    cpt1 = 0
    n0 = Tree(None, None,None, True)
    tab1.append(n0)
    #print(n)
    #print(cpt1)
    while(n>cpt1):
        #print("ici ", cpt1)
        x = genInt(2*cpt1)
        noeud = tab1[x]
        e = Tree(None, None,noeud.parent)
        tab1.append(e)
        if(bit_suivant()):
            noeud.parent=e
            e.gauche = noeud
            e.droite = Tree(None, None,e)
            tab1.append(e.droite)
        else : 
            noeud.parent=e
            e.droite = noeud
            e.gauche = Tree(None, None,e)
            tab1.append(e.gauche)
        cpt1 += 1
    #print(tab1)
    return tab1
    #return tab1[j]
def findR(t):
    if (t[0].parent==None):
        return t[0]
    else:
        return findR(t[1:])
def remy2(n,t):
    tab1 = []
    cpt1 = 0
    n0 = Tree(None, None,None, True)
    tab1.append(n0)
    print(n)
    print(cpt1)
    j=0
    while(n>cpt1):
        #print("ici ", cpt1)
        #x = genInt(2*cpt1)
        x=t[0]
        t=t[1:]
        noeud = tab1[x]
        if(noeud.racine == True):
            e = Tree(None, None,None, True)
            n0=e
            j=x
            noeud.racine = False
        else:
            e = Tree(None, None)
        if(bit_suivant()):
            e.gauche = noeud
            e.droite = Tree(None, None,None)
            tab1.append(e.droite)
        else : 
            e.droite = noeud
            e.gauche = Tree(None, None,None)
            tab1.append(e.gauche)
        tab1.append(e)
        cpt1 += 1
    #print(tab1)
    return tab1[j]


print(arbre2str(findR(remy(3))))
aa=remy(2)
#print(arbre2str(findR(aa)))
#print(arbre2str(remy(4)))

print(arbre2str(findR(remy(4))))

























 
