# -*- coding: utf-8 -*-

def rand48(n):

    a = 25214903917
    c = 11
    m = 2**48

    return (a*n+c) % m

cpt = 0
n = 123456789 + 2^40
r = 0

def bit_suivant():
    global n, cpt, r

    if cpt == 0:
        cpt = 48
        n = rand48(n)
        r = n

    bit = r % 2
    r = r // 2
    cpt = cpt-1
    return bit

def rand481(m, a, c, g, n):
    if(n==0):
        return g
    else:
        res = (a *rand481(m, a, c, g, n-1) + c)%m
        return res

tab = 123456789+2**40
btab=""
graine = 123456789+2**40
modulo = 2**48
c = 11
a = 25214903917
n = 1
cpt=0

def bit_suivants():
     global btab
     global tab,cpt,n
     if(cpt == 0):
        cpt=48
        tab = rand481(modulo, a, c, tab, n) 
        if(n==2):
            n=1
        btab = tab
        
     bit = btab%2
     btab=btab//2
     cpt-=1
     return bit

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

def remy(n):
    tab1 = []
    cpt1 = 0
    n0 = Tree(None, None,None, True)
    tab1.append(n0)
    
    while(n>cpt1):
        x = genInt(2*cpt1)
        noeud = tab1[x]
        e = Tree(None, None,noeud.parent)
       
        if(bit_suivant()):
            noeud.parent=e
            e.gauche = noeud
            e.droite = Tree(None, None,e)
            tab1.append(e)
            tab1.append(e.droite)
        else : 
            noeud.parent=e
            e.droite = noeud
            e.gauche = Tree(None, None,e)
            tab1.append(e)
            tab1.append(e.gauche)
        cpt1 += 1
        
    return tab1
    
def findR2(t,i):
    if (t[i].parent==None):
        return i
    else:
        return findR2(t,i+1)
    
def findR3(t,i):
    if (len(t)==0):
        return i
    if(t[0].gauche==None and t[0].droite==None):
        return findR3(t[1:],i+1)  
    else:
        return findR3(t[1:],i)   
    
def remy2(n,t):
    tab1 = []
    cpt1 = 0
    n0 = Tree(None, None,None, True)
    tab1.append(n0)
    
    while(n>cpt1):
        x=t[0]
        b=t[1]
        t=t[2:]
        noeud = tab1[x]
        pere =noeud.parent
        e = Tree(None, None,noeud.parent)
        
        if (b):
            e.gauche = noeud
            e.droite = Tree(None, None,e)
            tab1.append(e.droite)
        else : 
            e.droite = noeud
            e.gauche = Tree(None, None,e)
            tab1.append(e.gauche)
            
        if(pere!=None):
            if(pere.gauche==noeud):
                pere.gauche=e
            else:
                pere.droite=e
                
        noeud.parent=e
        tab1.append(e)
        cpt1 += 1
    
    return tab1

def all_list2(n,i,l):
    if (n+1==i):
        return l
    res=list()
    if(i==0):
        l.append([0,0])
        l.append([0,1])
        return all_list2(n,i+1,l)
    for e in l:
        for j in range(0,(2*i)+1):
            buff=e.copy()
            buff.append(j)
            for r in range (0,2):
                buff2=buff.copy()
                buff2.append(r)
                res.append(buff2)
        
    return all_list2(n,i+1,res)


def mot2(A):
    if (A.gauche==None and A.droite==None):
        return ""
    else:
        return "("+mot2(A.gauche)+")"+mot2(A.droite)
    
def check_uniform(l,n):
    mots=dict()
    print(len(l))
    for i in l:
        a=remy2(n,i)
        b=findR2(a,0)
        buff=mot2(a[b])
        mots[buff]=mots.get(buff,0)+1
    
    print("taille " + str(n) + " : " + str(mots))
    
    

for i in range(0,6):
    check_uniform(all_list2(i,0,list()),i)





















 
