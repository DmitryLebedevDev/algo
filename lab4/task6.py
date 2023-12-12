from anytree import Node,RenderTree
from calcTreeExp import calcTreeExp

priorities = {
  "+": 0,
  "-": 0,
  "*": 1,
  "/": 1
}

msg = input('Введите выражение\n')

currentNode = None
num = ''
try:
  charsWithPriority = []
  bracketsPriority = max(*priorities.values())
  opens = 0
  for i in range(len(msg)):
    char = msg[i]

    if char == '(':
      opens += 1
    elif char == ')':
      if opens == 0:
        raise BaseException("Недопустимое выражение")
      opens -= 1
    elif char in priorities:
      currentPriority = priorities[char]+opens
      if opens > 0:
        currentPriority += bracketsPriority
      charsWithPriority.append((
        char,
        currentPriority
      ))
    else:
      charsWithPriority.append((char, 0))
  if opens > 0:
    raise BaseException("Недопустимое выражение")

  for i in range(len(charsWithPriority)):
    (char, priority) = charsWithPriority[i]
    
    if str.isnumeric(char):
      num += char
    elif char in priorities:
      if num == '':
        raise BaseException("Недопустимое выражение")
      if currentNode == None:
        currentNode = Node(char,priority=priority)
        Node(num, parent=currentNode)
      else:
        if currentNode.priority < priority:
          currentNode = Node(char, parent=currentNode, priority=priority)
          Node(num, parent=currentNode)
        else:
          Node(num, parent=currentNode)
          while (not currentNode.is_root) and currentNode.priority >= priority:
            currentNode = currentNode.parent
          if currentNode.is_root:
            currentNode = Node(char, children=[currentNode], priority=priority)
          else:
            currentNode = Node(char, parent=currentNode, priority=priority)
      num = ''
    else:
      raise BaseException("Недопустимое выражение")
    
  if num == '' or currentNode == None:
    raise BaseException("Недопустимое выражение")
  else:
    root = currentNode
    while not root.is_root:
      root = root.parent
    Node(num, parent=currentNode)
    print(RenderTree(root).by_attr())
    print(f'Ответ: {msg}={calcTreeExp(root)}')
except BaseException as e:
  print(e)