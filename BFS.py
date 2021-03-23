"""
@author: Equipo Dinamita
"""

graph = {
  'H' : ['P','D', 'M'],
  'P' : ['N'],
  'N' : ['I', 'K', 'O'],
  'I' : [],
  'K' : ['F','B'],
  'O' : [],
  'F' : [],
  'B' : [],
  'D' : ['L','E'],
  'L' : ['Q','R','G'],
  'Q' : ['A'],
  'A' : [],
  'R' : [],
  'G' : [],
  'E' : [],
  'M' : ['J', 'C'],
  'J' : [],
  'C' : []
}


def BFS(graph, start, find):
    visited = []
    queue = [start]

    while queue:
        current = queue.pop()
        for neighbor in graph[current]:
            if not neighbor in visited:
                queue.insert(0,neighbor)
        visited.append(current)
        if(current == find):
            break
        
    return visited


print(BFS(graph, 'H', 'J'))