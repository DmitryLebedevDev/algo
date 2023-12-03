from anytree import Node

def calcTreeExp(tree: Node):
  if tree.is_leaf:
    return int(tree.name)
  c1 = calcTreeExp(tree.children[0])
  c2 = calcTreeExp(tree.children[1])
  if tree.name == '+':
    return c1+c2
  if tree.name == '-':
    return c1-c2
  if tree.name == '*':
    return c1*c2
  return c1/c2