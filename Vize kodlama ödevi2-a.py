class BinaryTree:
    def __init__(self,rootobj):
        self.key=rootobj
        self.left=None
        self.right=None
    def insertLeft(self,newNode):
        if self.left==None:
            self.left=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.left=self.left
            self.left=t
    def insertRight(self,newNode):
        if self.right==None:
            self.right=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.right=self.right
            self.right=t
    def En_sol_dip(root):
        while root.left!=None:
            root=root.left
        return root
