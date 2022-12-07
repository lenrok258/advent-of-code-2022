import re 

# test: 
# input: too low 756542

lines = open('input.txt', 'r').read().splitlines()

nodesDict = dict()

class Node:
    type = None # DIR, FILE
    size = None
    parent = None


    def __init__(self, type, size, parent):
        self.type = type
        self.size = int(size)
        self.parent = parent


    def __str__(self):
        return f"Node[{self.type, self.size, self.parent}]"


    def increaseSize(self, sizeToAdd):
        self.size += sizeToAdd


    def updateSizes(self):
        if self.type != "FILE":
            return

        # print(f"Update size {self}, parent {self.parent}")
        currentNode = self
        while True:
            currentNode.parent.increaseSize(self.size)
            currentNode = currentNode.parent
            if currentNode.parent == None: # root
                break


rootNode = Node("DIR", 0, None)
nodesDict["/"] = rootNode

currentDir = rootNode
for l in lines:
    # print(f"Processing {l}")

    if l.startswith("dir"):
        dir_name = l.split(" ")[1]
        nodesDict[dir_name] = Node("DIR", 0, currentDir)
    elif l == "$ cd ..":
        currentDir = currentDir.parent
    elif l.startswith("$ cd"):
        dir_name = l.split(" ")[2]
        currentDir = nodesDict[dir_name] 
    elif re.search("^\d", l):
        # TODO: add full path as id (same name in multiple dirs)
        size, name = l.split(" ")
        print(f"FILE {name}")
        fileNode = Node("FILE", size, currentDir)
        nodesDict[name] = fileNode
        fileNode.updateSizes()

# for k, v in nodesDict.items():
#     print(f"{k}\t\t{v}")

summm = 0
for k, node in nodesDict.items():
    if node.type == "DIR" and node.size <= 100000:
        summm += node.size

print(summm)