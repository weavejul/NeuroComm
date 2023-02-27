class HuffNode():
    def __init__(self, freq, value, left=None, right=None, huffCode='') -> None:
        self.freq = freq
        self.value = value
        self.left = left
        self.right = right
        self.huffCode = huffCode

def printHuffNodes(node, thisHuffCode=''):
    nodeCode = '' + thisHuffCode
    if not node.left and not node.right:
        print(node.value, nodeCode)
    else:
        if node.left:
            printHuffNodes(node.left, nodeCode + '0')
        if node.right:
            printHuffNodes(node.right, nodeCode + '1')

def nodesFromDict(nodeInfo):
    nodes = []
    for value, freq in nodeInfo:
        nodes.append(HuffNode(freq, value))
    return nodes

def createTree(nodes):
    if len(nodes) == 1:
        return nodes[0]
    
    nodes = sorted(nodes, key= lambda x : x.freq)
    left = nodes[0]
    left.huffCode = '0'
    right = nodes[1]
    right.huffCode = '1'
    nodes.append(HuffNode(left.freq + right.freq, None, left, right))
    nodes.remove(left)
    nodes.remove(right)
    return createTree(nodes)
