#!/usr/bin/env python
# coding: utf-8

# # TREES

# # FIRST WE WILL LEARN ABOUT HOW TO BUILD A TREE
# 1.TREES CAN BE BUILD USING RECURSION AND JUST LOOK AT WHAT WE HAVE DONE
# 
# 2.EITHER FIRST WE HAVE SOLVE A SIMPLER PROBLEM,AND THEN USING RECURSION
# 
# 3.LET US FIRST BUID A TREE 
#  
#  MAKING TREE IS TWO PROCESS THING
#   
#   1. WE CAN MAKE IT BY TAKING LEVEL WISE INPUT 
#   2. WE CAN DO IT BY FIRST TAKING LEFT INPUT AND THEN TAKING RIGHT INPUT
#   

# # WHAT IS A BINARY TREE?
# 
# ANSWER:
# 
# A BINARY TREE IS A TREE WHICH IS HAVING EITHER 0 OR 1 OR 2 CHILD

# # BUILD TREE INTO THE LEFT

# In[40]:


#IN THIS FIRST WE HAVE CREATED A CLASS BINARY TREE THAT GIVES US BASIC KNOWLEDGE THAT HEY, WE HAVE CREATE A NODE HAVING DATA
#AND POINITNG TOWARS TWO ADDRESSES THAT CORRESPONDS TO LEFT AND RIGHT CHILD OF A ASUBTREE
class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
#HERE WE HAVE BUILT A TREE HAT TAKE FIRST INPUT OF LEFT AND THEN GOES INTO THE RIGHT OF IT 
def Buildtreeleft():
    rootdata=int(input())
    if(rootdata==-1):
        return None
    root=BinaryTree(rootdata)
    leftpart=Buildtreeleft()
    rightpart=Buildtreeleft()
    root.left=leftpart
    root.right=rightpart
    return root
#HERE WE HAVE PRINTED THAT TREE
def printtreeleft(root):
    if(root==None):
        return 
    if(root.data!=-1):
        print(root.data,end=":")
    if(root.left!=None):
        print(root.left.data,end=",")
    else:
        print("-1",end=",")
    if(root.right!=None):
        print(root.right.data,end="")
    else:
        print("-1",end="")
    print()
    printtreeleft(root.left)
    printtreeleft(root.right)
#IMPLEMENTATION OF THAT TREE USING RECURSION ,
root=Buildtreeleft()
printtreeleft(root)    
    


# # IMPLEMENTATION OF THE ABOVE TREE
# 
# 1.HEY MY WORK IS TO CHECK WHETHER THE DATA THAT WE ADDED IS -1 OR NOT IF IT IS-1 THEN RETURN SIMPLY , IF  IT NOT THEN 
# CREATE A NODE AND LET RECURSION TOCREATE IT'S SUBTREE , OUUR WORK IS TO JOIN THAT SUBTREES CREATED BY RECURSION WITH THAT OF ROOT CORRESPONDINGLY
# 
# 2.PRINTIND GOES SAME AS WELL WE WILL THINK FOR ROOT AND IT'S RIGHT AND LEFT CHILD , REST OF THE WORK WILL BE DOE MY RECURSION ITSELF
# 

# # TIME COMPLEXITY OF THE ABOVE TREE

# # TIME COMPLEXITY OF BINARY TREE
# 
# 1.HENCE WE ARE DISTRIBUTING, OUR TREE INTO N/2 EVERYTIME AND CORRESPONDINGLY , WE ARE JUST DOING SOMETHING CONSTANT K WORK AND HENCE WE CAN MAKE RECRRANCE RELATION OF IT ACCORDINGLY.
# 2.
# 
# 
# 

# # COUNT NUMBER OF NODES IN A TREE
# 
# 1.HERE RECURSION IS DOING ALL OF THE WORK OUR WORK IS TO JUST ADD ONE MORE TO THE FINAL EVALUATION OF THE TREE CORRESOPONDINGLY

# In[10]:


def count(root):
    if(root==None):
        return 0
    v=count(root.left)
    b=count(root.right)
    return v+b+1
v=count(root)
v


# # TRAVERSAL IN A TREE
# 
# 1.IN A TREE THERE ARE THREE TYPES OF TRAVERSAL:
# 
# A.PRE ORDER
# B.INORDER
# C.POSTORDER
# 
# IN A
# 
# ITERATION IS LIKE THIS 
# FIRST DATA THEN LEFT THEN RIGHT
# 
# IN B
# 
# FIRST LEFT DATA RIGHT
# 
# IN C
# 
# FIRST LEFT RIGHT DATA

# In[21]:


#PRE ORDER
def preorder(root):
    if(root==None):
        return 
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
    return
preorder(root)


# In[24]:


#inorder
def inorder(root):
    if(root==None):
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
    return
inorder(root)


# In[27]:


#postorder
def postorder(root):
    if(root==None):
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")
    return
postorder(root)


# # WHAT IS A HEIGHT OF A TREE?
# 
# 1.height of a tree tells us the height pf the corresponding tree, if only root is present then height of the tree will be 1 only, if the next nodes arre also there in the below level then height will be raised , so how can we do it 
# 

# In[29]:


def height(root):
    if(root==None):
        return 0
    leftsubheight=height(root.left)
    rightsubheight=height(root.right)
    if(leftsubheight>rightsubheight):
        return leftsubheight+1
    else:
        return rightsubheight+1
v=height(root)
v


# # DIFFERENCE BETWEEN HEIGHT AND DEPTH 
# 
# 
# hey root node is having oth depth , it is the distance of the particular node from the root node of the tree.
# 
# hence it will tell us how much is the depth of that particular node from the root node
# 
# example of the node at particular depth is 5 so 5 represents here the depth of the node from the root node
# 
# If there is only root node then depth is equal to 0

# # PRINTING AT DEPTH K 
# 
# ONE OF THE BEST PROBLEM TO UNDERSTAND , LET US SEE INTO IT

# In[32]:


def printingAtDepthK(root,k):
    if(root==None):
        return
    if(k==0):
        print(root.data)
    printingAtDepthK(root.left,k-1)
    printingAtDepthK(root.right,k-1)
    return
#here k is 2
printingAtDepthK(root,2)
    


#  # REPLACE NODES WITH DEPTH

# In[36]:


def replaceNodeWithDepthK(root,count):
    if(root==None):
        return
    if(root.left==None and root.right==None):
        root.data=count
        return root
    else:
        root.data=count
    replaceNodeWithDepthK(root.left,count+1)
    replaceNodeWithDepthK(root.right,count+1)
replaceNodeWithDepthK(root,0)
printtreeleft(root)


# # REMOVE LEAVES NODE IN BINARY TREE

# In[38]:


def removeleaves(root):
    if(root==None):
        return
    if(root.left==None and root.right==None):
        return None
    root.left=removeleaves(root.left)
    root.right=removeleaves(root.right)
    return root


# # MIRROR TREE

# In[46]:


def mirror(root):
    if(root==None):
        return
    if(root.left!=None and root.right!=None):
        temp=root.left
        root.left=root.right
        root.right=temp
    mirror(root.left)
    mirror(root.right)
    return root
root1=mirror(root)
printtreeleft(root1) 


# # TREES IN LEVEL INPUT AND PRINTING LEVEL WISE
# AT THIS POINT WE ARE FIRST TAKING INPUT OF LEFT SUBTREE AND COMPARITIVEELY FIRST ALL THE LEFT AND THEN BUT WHAT WE WANT IS TO DO THAT,OUR TREE SHOULFD TAKE INPUT LEVEL WISE AND PRINT ALSO LEVEL WISE ACCORDINGLY
# 
# HENCE FOR THIS WE NEED TO MAKE A QUEUE AS IN 
# 
# Q=[1,2,3,4,5]
# 
# FIRST WE INSERTED 1 IN THE QUEUE MEANING NOW WE WANT THE CHIDREN OF 1 CORRESNPONDINGLY THAT IS 2 AND 3 SO WE WILL INSERT THEM 
# 
# IN THE QUEUE AND MAKE CONNECTION WITH THAT OF THE ROOT NODE AND AFTEER THAT THE FRONT ELEMENT OF THE QUEUE WILL ASK ABOUT THE 
# 
# 2ND ELEMENT OF THE QUEUE AND IT WILL ASK THE CHILDREN OF 2 TO BE INSERTED IN THE QUEUE AND MAKE CONNECTIONS WITH THEM AND THIS 
# 
# PROCESS GOES OIN UNTILL WE COME ACROSS -1 

# In[5]:


class binary2:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
import queue
q=queue.Queue()
def takeinputlevelwise():
    rootdata=int(input())
    if(rootdata==-1 or rootdata<0):
        return None
    root=binary2(rootdata)
    q.put(root)
    while(not(q.empty())):
        current=q.get()
        
        print("enter the left child of :",current.data)
        left=int(input())
        if(left!=-1):
            leftchild=binary2(left)
            current.left=leftchild
            q.put(leftchild)
        print("enter the right child of :",current.data)
        right=int(input())
        if(right!=-1): 
            rightchild=binary2(right)
            current.right=rightchild
            q.put(rightchild)
    return root
def printlevelwise(root):
    if(root==None):
        return None
    q.put(root)
    while(not(q.empty())):
        current=q.get()
        print(current.data,end=":")
        if(current.left!=None):
            print(current.left.data,end=",")
            q.put(current.left)
        if(current.right!=None):
            print(current.right.data,end="")
            q.put(current.right)
        print()
        
            
        
    
root=takeinputlevelwise()
printlevelwise(root)
    
    


# # TREE BUILDING USING (POSTORDER AND INORDER) OR (INORDER AND PREORDER)

# # TREE USING POST ORDER AND INORDER

# In[6]:


#HERE LI2 WILL BE IN INORDER AND LI1 WILL BE IN POST ORDER

def postin(post,inor):
    if(len(post)==0):
        return None
    rootdata=post[len(post)-1]
    post.pop()
    root=binary2(rootdata)
    index=-1
    for i in range(0,len(inor)):
        if(inor[i]==root):
            index=i
            break
    inorl=inor[0:index]
    inorr=inor[index+1:]
    postl=post[0:len(inorl)]
    postr=post[len(inorl):]
    left=postin(postl,inorl)
    right=postin(postr,inorr)
    root.left=left
    root.right=right
    return root


# # DIAMETER OF A BINARY TREE

# In[ ]:


def diameter(root,m,n):
    if(root==None):
        return None
    

