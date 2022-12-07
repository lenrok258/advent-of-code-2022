import re 

# test: 
# input: 5649896

lines = open('input.txt', 'r').read().splitlines()[1::]

nodesDict = dict()

class Node:
    type = None # DIR, FILE
    size = None
    parent = None
    path = "/"

    def __init__(self, type, size, name, parent):
        self.type = type
        self.size = int(size)
        self.parent = parent
        if (self.parent != None):
            self.path = self.parent.path + "/" + name

    def __str__(self):
        return f"Node[{self.type, self.size, self.path, self.parent}]"

    def increaseSize(self, sizeToAdd):
        self.size += sizeToAdd

    def updateSizes(self):
        currentNode = self
        while True:
            currentNode.parent.increaseSize(self.size)
            currentNode = currentNode.parent
            if currentNode.parent == None: # root
                break


rootNode = Node("DIR", 0, "", None)
nodesDict[rootNode.path] = rootNode

currentDir = rootNode
for l in lines:
    if l.startswith("dir"):
        dir_name = l.split(" ")[1]
        node = Node("DIR", 0, dir_name, currentDir)
        nodesDict[node.path] = node
    elif l == "$ cd ..":
        currentDir = currentDir.parent
    elif l.startswith("$ cd"):
        dir_name = l.split(" ")[2]
        path = currentDir.path + "/" + dir_name
        currentDir = nodesDict[path] 
    elif re.search("^\d", l):
        size, name = l.split(" ")
        node = Node("FILE", size, name, currentDir)
        nodesDict[node.path] = node
        node.updateSizes()

freeSpace = 70000000 - rootNode.size
needed = 30000000 - freeSpace

sorted_dirs = sorted([n.size for n in nodesDict.values() if n.type == "DIR"])
for d in sorted_dirs:
    if d > needed:
        print(d)
        break