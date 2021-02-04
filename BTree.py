# node class
class Node:

    def __init__(self, data):
        # left child
        self.left = None
        # right child
        self.right = None
        # node's value
        self.data = data
    #function to build the binary tree, val that are less than parent are on left 
    #value that are greater than parent are on right 
    def bld_bin_tree(self,val):
      if self.data:
        if val < self.data:
          if self.left is None:
            self.left = Node(val)
          else:
            self.left.bld_bin_tree(val)
        else:
          if self.right is None:
            self.right = Node(val)
          else:
            self.right.bld_bin_tree(val)
      else:
        self.data = val

    #find value in the tree
    def find_ele_in_bin_tree(self,val):
      if val < self.data:
        if self.left is None:
          print(str(val) + ' not found')
        else:
          self.left.find_ele_in_bin_tree(val)
      elif val > self.data:
        if self.right is None:
          print(str(val) + 'Not found')
        else:
          self.right.find_ele_in_bin_tree(val)
      else:
        print(str(self.data) + ' Found')                    

    # print function
    def PrintTree(self):
        print(self.data)

root = Node(35)
root.bld_bin_tree(14)
root.bld_bin_tree(27)
root.bld_bin_tree(10)
root.bld_bin_tree(31)
root.bld_bin_tree(8)
root.PrintTree()
root.find_ele_in_bin_tree(10)