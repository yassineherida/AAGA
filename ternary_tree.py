#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 12:42:34 2020

@author: 3873896
"""

import random
from hypothesis.strategies import integers,lists,texts
from hypothesis import given

NB = 0

class Arbre:
    def __init__(self, cle, val, F):
        global NB
        self.id = NB
        NB += 1
        self.cle = cle
        self.val = val
        self.fils = F

    def affiche(self):
        if self.cle=='':
            return ' . '
        g = '( ' + self.cle + (', '+str(self.val) if self.val !=None else '') + ' '
        for f in self.fils:
            g += f.affiche() + ' '
        g += ')'
        return g


#Genere un arbre a 1 feuille
def gener_feuille():
    return Arbre('', None, [])

#Genere un arbre a 1 noeud
def gener_noeud(cle, val, F):
    return Arbre(cle, val, F)

#Genere un arbre a partir d'un mot
def cons(mot):
    if mot == '':
        return gener_feuille()
    else:
        if len(mot)==1:
            return gener_noeud(mot[0], 0, [gener_feuille(), gener_feuille(), gener_feuille()])
        else:
            return gener_noeud(mot[0], None, [gener_feuille(), cons(mot[1:]), gener_feuille()])

#Insere un mot dans l'arbre
def insert(A, mot):
    if mot == '':
        return A
    if A.cle == '':
        return cons(mot)
    if A.cle > mot[0]:
        return gener_noeud(A.cle, A.val, [insert(A.fils[0], mot), A.fils[1], A.fils[2]])
    elif A.cle == mot[0]:
        val = A.val
        if len(mot)==1:
            val = 0
        return gener_noeud(A.cle, val, [A.fils[0], insert(A.fils[1], mot[1:]),  A.fils[2]])
    else:
        val = A.val
        return gener_noeud(A.cle, val, [A.fils[0], A.fils[1], insert(A.fils[2], mot)])

#Fusionne 2 arbres
def fusion(A, B):
    if A.cle == '':
        return B
    if B.cle == '':
        return A

    if A.cle < B.cle:
        return gener_noeud(A.cle, A.val,  [A.fils[0], A.fils[1], fusion(A.fils[2], B)])
    if A.cle > B.cle:
        return gener_noeud(A.cle, A.val,  [fusion(A.fils[0], B), A.fils[1], A.fils[2]])

    if A.val != None:
        val = A.val
    else:
        val = B.val
    return gener_noeud(A.cle, val,  [fusion(A.fils[0], B.fils[0]), fusion(A.fils[1], B.fils[1]), fusion(A.fils[2], B.fils[2])])

#Fusionne 2 arbres 
def fusion2(A, B):
    if A.cle == '':
        return B
    if B.cle == '':
        return A

    if A.cle < B.cle:
        return gener_noeud(A.cle, A.val,  [A.fils[0], A.fils[1], fusion(A.fils[2], B)])
    if A.cle > B.cle:
        return gener_noeud(A.cle, A.val,  [fusion(A.fils[0], B), A.fils[1], A.fils[2]])

    if A.val != None:
        val = A.val
    else:
        val = B.val
    return gener_noeud(A.cle, val,  [fusion(A.fils[0], B.fils[0]), fusion(A.fils[1], B.fils[1]), fusion(A.fils[2], B.fils[2])])

#Recherche un mot dans l'arbre
def get(A, mot):
	if(mot == "") :
		return False	
	if(A.cle == mot):
		if(A.val == 0):
			return True
		else:
			return False
	
	if(mot[0] < A.cle):
		return get(A.fils[0], mot)
	if(mot[0] == A.cle and len(A.fils) >= 2):
		return get(A.fils[1], mot[1:])
	if(mot[0] > A.cle and len(A.fils) >= 3):
		return get(A.fils[2], mot)
	
	return False

#Construit un arbre a partir de nb mots aleatoires d'un fichier
#en effectuant des insertions
def buildTreeBook(fichier, nb):
	contenu_fichier = open(fichier, "r").read().split()
	arbre = gener_feuille()
	mots = []
	for i in range(nb):
		if(len(contenu_fichier) == 0):
			return arbre
		n = random.randint(0, len(contenu_fichier)-1)
		arbre = insert(arbre,contenu_fichier[n])
		mots.append(contenu_fichier[n])
		contenu_fichier.remove(contenu_fichier[n])
	
	return arbre, mots

#Construit un arbre a partir de nb mots aleatoires d'un fichier
#en effectuant des fusions 
def buildTreeBookFusion(fichier, nb):
	contenu_fichier = open(fichier, "r").read().split()
	arbre = gener_feuille()
	for i in range(nb):
		if(len(contenu_fichier) == 0):
			return arbre
		n = random.randint(0, len(contenu_fichier)-1)
		buff=cons(contenu_fichier[n])
		arbre = fusion(arbre,buff)
		contenu_fichier.remove(contenu_fichier[n])
	
	return arbre

# A SUPPRIMER DANS LE CODE FINAL ???
def buildTreeBookFusion2(mots, nb):
    arbre = gener_feuille()
    for i in range(nb):
        if(i >= len(mots)):
            return arbre
        print(arbre.affiche())
        arbre = fusion(cons(mots[i]),arbre)
    return arbre

#Fonction auxiliaire de checkpropi(A)
#Verifie si un noeud de l'arbre verifie bien les proprietes
def checkcroissant(fils, a):
    if(len(fils) == 1 or len(fils) == 0):
        return True
    if (len(fils) == 2):
        if(fils[0].cle == a):
            if(fils[1] <= a):
                return False
        if (fils[1].cle == a):
            if(fils[0].cle >= a):
                return False
        if(fils[0].cle == fils[1].cle):
            return False
    if (len(fils) == 3 and fils[0].cle != "" and fils[1].cle != "" and fils[2].cle != ""):
        if (fils[0].cle >= a or fils[2].cle <= a ):
            return False

#Verifie si l'ensemble de l'arbre respecte bien les proprietes         
def checkpropri(A):
    if (checkcroissant(A.fils,A.cle)==False):
        return False
    for i in A.fils:
        if (checkpropri(i) == False):
            return False
    return True




chemin = "Shakespeare/Shakespeare/"
nb = 3
b, mots = buildTreeBook(chemin + "john.txt", nb)

ze=['o', 'brings', 'i']
c = buildTreeBookFusion2(ze, nb)
print(c.affiche())


for m in ze :
    if(not get(b, m)) :
        print(m + " : non trouve dans insertion")

print(checkpropri(b))
print(checkpropri(c))

@given(lists(texts),integers)
def checkfusion(mots, nb):
    c = buildTreeBookFusion2(mots, nb)
    m2=[]
    for m in mots :
        if(get(c, m)) :
            m2.append(m)
    assert mots == m2
    
      
