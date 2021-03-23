"""
@author         Roxana Anabel Lafuente
@description    Breath First Search (BFS) algorithm implementation.
"""

def bfs(root, graph):
    queue = []
    queue.append(root)
    while len(queue):
        current = queue.pop()
        print(current, end=" ")
        for node in graph[current]:
            queue.insert(0, node)

# Note: Check the README file for a graphic representation of the tree
bfs(100, {
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