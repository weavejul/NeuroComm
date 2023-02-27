import huffman as hm, alphabet
import networkx as nx, matplotlib.pyplot as plt
from dash import Dash, html
import dash_cytoscape as cyto

app = Dash(__name__)

alphaDict = alphabet.letterFreqs
nodes = hm.nodesFromDict(alphaDict.most_common())
nodes.append(hm.HuffNode(alphaDict.most_common()[0][1], '_'))
rootNode = hm.createTree(nodes)
#hm.printHuffNodes(rootNode)

class GraphVis:
    def __init__(self) -> None:
        self.visual = []
    
    def addEdge(self, a, b):
        self.visual.append([a, b])
    
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()
    
    def edgesFromHuff(self, node, huffCode = '.'):
        huffCode += node.huffCode
        if node.left:
            self.visual.append([huffCode, huffCode + node.left.huffCode])
            self.edgesFromHuff(node.left, huffCode)
        if node.right:
            self.visual.append([huffCode, huffCode + node.right.huffCode])
            self.edgesFromHuff(node.right, huffCode)

"""G = GraphVis()
G.edgesFromHuff(rootNode)
G.visualize()"""

class DashVis:
    def __init__(self) -> None:
        self.elements = []

    def fillElementsFromHuff(self, node, huffCode = '.'):
        self.elements.append({'data': {'id': huffCode, 'label': str(node.value)}})
        self._fillElementsHelper(node, huffCode)
    
    def _fillElementsHelper(self, node, huffCode):
        print(huffCode)
        if node.left:
            if node.left.value:
                self.elements.append({'data': {'id': huffCode + '0', 'label': str(node.left.value)}})
            else:
                self.elements.append({'data': {'id': huffCode + '0'}})
            self.elements.append({'data': {'source': huffCode, 'target': huffCode + '0'}})
            self._fillElementsHelper(node.left, huffCode + '0')
        if node.right:
            if node.right.value:
                self.elements.append({'data': {'id': huffCode + '1', 'label': str(node.right.value)}})
            else:
                self.elements.append({'data': {'id': huffCode + '1'}})
            self.elements.append({'data': {'source': huffCode, 'target': huffCode + '1'}})
            self._fillElementsHelper(node.right, huffCode + '1')
    
    def runGraph(self):
        app.layout = html.Div([
            html.P("Alphabet Hufftree:"),
            cyto.Cytoscape(
                id = 'cytoscape',
                elements = self.elements,
                layout = {'name': 'breadthfirst', 'roots': '[id = "."]'},
                style = {'width': '2000', 'height': '2000px'},
                stylesheet= [
                    #Group selectors
                    {
                        'selector': 'node',
                        'style': {
                            'content': 'data(label)'
                        }
                    },

                    #Class selectors
                    {
                        'selector': '.green',
                        'style': {
                            'background-color': 'lawngreen'
                        }
                    }
                ]
            )
        ])
        app.run_server(debug=True)

    def getLetter(self, rootNode):
        currentNode = rootNode
        currentHuff = '.'
        while True:
            leftOrRight = input("Input 1 or 0: ")
            if leftOrRight == "1":
                currentNode = currentNode.right
                if currentNode.value:
                    print(currentNode.value)
                    break
            if leftOrRight == "0":
                currentNode = currentNode.left
                if currentNode.value:
                    print(currentNode.value)
                    break

D = DashVis()
D.fillElementsFromHuff(rootNode)
D.runGraph()