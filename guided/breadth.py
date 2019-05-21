from resources import Queue
from resources import Stack

def bft(self, starting_vertex_id):
    # Create an empty queue and enqueue the starting vertex_id
    q = Queue()
    q.enqueue(starting_vertex_id)
    # Create a Set to store visited vertices
    visited = set()
    # While the queue is not empty:
    while q.size() > 0:
    #   Dequeue the first vertex
        v = q.dequeue()
    #   If that vertex has not been visited:
        if v not in visited:
    #       Mark it as visited
            print(v)
    #       Then add all of its neighbors to the back of the queue
            for next_vert in self.vertices[v]:
                q.enqueue(next_vert)

def bfs(self, starting_vertex_id, target):
    q = Queue()
    q.enqueue([starting_vertex_id])
    visited = set()
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            if v == target:
                return path
            visited.add(v)
            for next_vert in self.vertices[v]:
                new_path = list(path)
                new_path.append(next_vert)
                q.enqueue(new_path)
    return None

def dft(self, starting_vertex_id):
    # Create an empty stack and push the starting vertex ID
    s = Stack()
    s.push(starting_vertex_id)
    # Create a Set to store visited vertices
    visited = set()
    # While the stack is not empty...
    while s.size() > 0:
        # Pop the first vertex
        v = s.pop()
        # If that vertex has not been visited...
        if v not in visited:
            # Mark it as visited...
            print(v)
            visited.add(v)
            # Then add all of its neighbors to the top of the stack
            for next_vert in self.vertices[v]:
                s.push(next_vert)

def dfs(self, starting_vertex_id, target_value):
    s = Stack()
    s.push([starting_vertex_id])
    visited = set()
    while s.size() > 0:
        path = s.pop()
        v = path[-1]
        if v not in visited:
            if v == target_value:
                return path
            visited.add(v)
            for next_vert in self.vertices[v]:
                new_path = list(path)
                new_path.append(next_vert)
                s.push(new_path)
    return None