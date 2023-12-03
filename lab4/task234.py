from anytree.importer import JsonImporter
from anytree import RenderTree, Node
importer = JsonImporter()

data = '''
{
  "v": "1",
  "children": [
    {
      "v": "2",
      "children": [
        {
          "v": "4"
        },
        {
          "v": "5"
        }
      ]
    },
    {
      "v": "3",
      "children": [
        {
          "v": "6"
        },
        {
          "v": "7"
        }
      ]
    }
  ]
}'''

root = importer.import_(data)
print(RenderTree(root).by_attr('v'))

print('Обход дерева в глубину')
path = []
stack = [root]
while len(stack) > 0:
  while not stack[-1].is_leaf:
    stack.append(stack[-1].children[0])
  path.append(stack.pop().v)
  if len(stack) > 0:
    node = stack.pop()
    path.append(node.v)
    if len(node.children) > 1:
      stack.append(node.children[1])
print(path)

print('Обход девера в ширину')
path = []
line = [root]
while len(line):
  node = line.pop(0)
  for c in node.children:
    line.append(c)
  path.append(node.v)
print(path)