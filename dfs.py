"""
@author         Roxana Anabel Lafuente
@description    Depth First Search (DFS) algorithm implementation.
"""

def dfs(root, graph):
    # Inorder
    stack = []
    stack.append(root)
    while len(stack):
        current = stack.pop()
        print(current, end=" ")
        for node in graph[current][::-1]:
            stack.append(node)

# Note: Check the README file for a graphic representation of the tree
dfs(100, {
    100: [50, 150],
    50: [40, 70],
    150: [120, 160],
    40: [],
    70: [60, 79],
    120: [109],
    160: [],
    60: [],
    79: [80],
    109: [],
    80: []
})