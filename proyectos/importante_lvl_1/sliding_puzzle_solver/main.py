from collections import deque

# Representación del estado final
FINAL_STATE = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

# Movimientos posibles: izquierda, derecha, arriba, abajo
MOVES = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def swap(state, x1, y1, x2, y2):
    new_state = [list(row) for row in state]
    new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
    return tuple(tuple(row) for row in new_state)

def bfs_solver(initial_state):
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == FINAL_STATE:
            return path
        
        x, y = find_blank(current_state)
        
        for move, (dx, dy) in MOVES.items():
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                new_state = swap(current_state, x, y, new_x, new_y)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [move]))
    
    return None  # No solución encontrada

# Estado inicial del usuario
initial_state = ((1, 7, 3), (4, 2, 0), (8, 6, 5))

solution = bfs_solver(initial_state)
if solution:
    print("Solución encontrada:", " -> ".join(solution))
else:
    print("No se encontró solución.")