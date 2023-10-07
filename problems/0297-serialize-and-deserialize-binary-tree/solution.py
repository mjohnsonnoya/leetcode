# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

  def serialize(self, root):
  
    """Encodes a tree to a single string.
    :type root: TreeNode
    :rtype: str
    """
    def preorder(root):
      if not root:
              return "#"
      return str(root.val) + "," + preorder(root.left) + "," + preorder(root.right)

    return preorder(root)

  def deserialize(self, data):
    
    def to_list(data):
      my_list = []
      value = ""
      for c in data:
          if c != ',':
              value += c  # Concatenate characters to form a number
          else:
              my_list.append(value)  # Append the number to the list
              value = ""  # Reset the value
      if value:  # Handle the last number in the string
          my_list.append(value)
      return my_list
                         
    my_list = to_list(data)
    def helper(my_list):
      val = my_list.pop(0)
      if val == "#":
        return None
      node = TreeNode(val)
      node.left = helper(my_list)
      node.right = helper(my_list)
      return node
    
    return helper(to_list(data))
                        
                
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
