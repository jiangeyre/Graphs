islands = [
    [0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0]
]

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def island_counter(matrix):
    # Create visited data struct
    # Walk through all the nodes, elements input in the matrix
    #     if it's not visited
    #         if the value in the matrix at this position is a 1
    #             do a traversal and mark each as visited
    #             increment island counter
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    island_count = 0
    
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if not visited[row][col]:
                if matrix[row][col] == 1:
                    visited = dft(row, col, matrix, visited)
                    island_count += 1
                else:
                    visited[row][col] = True
    return island_count

def dft(row, col, matrix, visited):
    s = Stack()
    s.push((row, col))
    while s.size() > 0:
        v = s.pop()
        row, col = v
        if not visited[row][col]:
            visited[row][col] = True
            for neighbor in get_neighbors(row, col, matrix):
                s.push(neighbor)
    return visited

def get_neighbors(row, col, matrix):
    neighbors = []
    #check north
    if row > 0 and matrix[row - 1][col] == 1:
        neighbors.append((row - 1, col))
    #check south
    if row < len(matrix) - 1 and matrix[row + 1][col] == 1:
        neighbors.append((row + 1, col))
    #check west
    if col > 0  and matrix[row][col - 1] == 1:
        neighbors.append((row, col - 1))
    #check east
    if col < len(matrix) - 1 and matrix[row][col + 1] == 1:
        neighbors.append((row, col + 1))
    return neighbors

print(island_counter(islands))