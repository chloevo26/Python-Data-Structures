def BinaryTree(r):
    return [r,[],[]]

def insertLeft(r, newBranch):
    t = r.pop(1)
    if len(t) > 1:
        r.insert(1, [newBranch, t, []])
    else:
        r.insert(1, [newBranch, [], []])
    return r


def insertRight(r, newBranch):
    t = r.pop(2)
    if len(t) > 1:
        r.insert(2, [newBranch, [], t])
    else:
        r.insert(2, [newBranch, [], []])
    return r

def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(3)
print(insertLeft(r,4))
print(insertLeft(r,5))
print(insertRight(r,6))
print(insertRight(r,7))