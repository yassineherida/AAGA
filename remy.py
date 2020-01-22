import random
from hypothesis.strategies import integers,lists,texts
from hypothesis import given

class Node : 
	def __init__(self, id, left, right, parent):
		self.id = id
		self.left = left
		self.right = right
		self.parent = parent


def change_leaves(tree, a, b):
    
    parenta = tree[a].parent
    parentb = tree[b].parent
	
    if(tree[parenta].right == a):
        tree[parenta].right = b
    else:
        tree[parenta].left = b

    tree[a].parent = parentb

    if(tree[parentb].right == b):
        tree[parentb].right = a
    else:
        tree[parentb].left = a

    tree[b].parent = parenta

    return tree


def growing_tree(n):
    tree=[]
    for i in range(0,(2*n)+1):
        tree.append(Node(None, -1, -1, -1))
    tree[0]=Node(1, 1, 2, 0)
    tree[1]=Node(None, -1, -1, 0)
    tree[2]=Node(None, -1, -1, 0)
    for i in range (2, n+1):
        number = random.randint(0,i-1)
        tree = change_leaves(tree, i-1, number+i-1)
        tree[i-1].right = 2*i-1
        tree[i-1].left = 2*i
        tree[i-1].id = i
        tree[2*i-1].parent = i-1
        tree[2*i].parent = i-1
        tree[2*i-1].right = -1
        tree[2*i-1].left = -1
        tree[2*i].right = -1
        tree[2*i].left = -1
    return tree

def growing_tree_deter(n,t):
    tree = []
    for i in range(0,(2*n)+1):
        tree.append(Node(None, -1, -1, -1))
    tree[0]=Node(1, 1, 2, 0)
    tree[1]=Node(None, -1, -1, 0)
    tree[2]=Node(None, -1, -1, 0)
    for i in range (2, n+1):
        number = t[0]
        t=t[1:]
        tree = change_leaves(tree, i-1, number+i-1)
        tree[i-1].right = 2*i-1
        tree[i-1].left = 2*i
        tree[i-1].id = i
        tree[2*i-1].parent = i-1
        tree[2*i].parent = i-1
        tree[2*i-1].right = -1
        tree[2*i-1].left = -1
        tree[2*i].right = -1
        tree[2*i].left = -1
    return tree

def mot(A, i):
    if (A[i].left==-1 and A[i].right==-1):
        return ""
    else:
        return "("+mot(A, A[i].left)+")"+mot(A, A[i].right)
    
def all_list(n,i,l):
    if (n+1==i):
        return l
    res=list()
    if(i==0):
        l.append([0])
        return all_list(n,i+1,l)
    for e in l:
        for j in range(0,i+1):
            buff=e.copy()
            buff.append(j)
            res.append(buff)
        
    return all_list(n,i+1,res)

print(all_list(3,0,list()))
T = [1]
def enum(n):
    global T

    if len(T)<n:
        for i in range(len(T),n+1):
            T.append( sum([T[k]*T[i-1-k] for k in range(0,i)]) )
    return T[n]


@given(list(list(integers)),integers)
def check_uniform(l,n):
    mots=dict()
    for i in l:
        buff=mot(growing_tree_deter(n,i),0)
        mots[buff]=mots.get(buff,0)+1
    #t=float(enum(n))
    print("taille " + str(n) + " : " + str(mots))
    #assert mots[next(iter(mots))]/len(l) ==1/t
    

for i in range(2,5):
    check_uniform(all_list(i,0,list()),i)

def printTree(tab):
    for t in tab:
        print(t.id, tab[t.left].id, tab[t.right].id, tab[t.parent].id)
    print("------------------------")
    for t in tab:
        print(t.id, t.left, t.right, t.parent)
    print()
        
tab = growing_tree_deter(5,[0,1,2,3,4])


    
