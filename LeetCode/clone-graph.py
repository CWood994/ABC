# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    mapping = {}
    def cloneGraph(self, node):
        self.mapping = {}
        return self.clone(node)
    
    def clone(self, node):
        if not node:
            return None
        
        if node.label in self.mapping:
            root = self.mapping[node.label]
            return root
        else:
            root = UndirectedGraphNode(node.label)        
            self.mapping[node.label] = root
            
        for n in node.neighbors:
            nc = self.clone(n)   
            root.neighbors.append(nc)
            
        return root
        