import random

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


def mot(A):
    if (A.left==None and A.right==None):
        return ""
    else :
        return "("+mot(A.left)+")"+"("+mot(A.right)+")"
    
def all_list(n,i,l):
    if (n+1==i):
        return l
    res=list()
    if(i==0):
        l.append([0])
        return all_list(n,i+1,l)
    for e in l:
        for j in range(0,i+1):
            print(e)
            print(j)
            buff=e.copy()
            buff.append(j)
            res.append(buff)
        
    return all_list(n,i+1,res)

#print(all_list(2,0,list()))
print(growing_tree(5))