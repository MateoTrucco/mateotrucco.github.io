import tkinter as tk
from collections import deque
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from base_functions import enable_high_dpi, colors
enable_high_dpi()

FINAL_STATE = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
MOVES = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

state = [[0 for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
solution = None
solution_index = 0
moves_label = None

bg_body = colors["++"]
bg_int = colors["-"]
fg_int = colors["b"]
bg_button = colors["+"]
fg_button = colors["w"]
active_bg_button = colors["-"]
active_fg_button = colors["++"]

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
    
    return None

def create_grid(root):
    global buttons
    for i in range(3):
        for j in range(3):
            button = tk.Button(
                root, text="", font=("Arial", 18, "bold"), width=8, height=4,
                bg=bg_button, fg=fg_button, activebackground=active_bg_button, activeforeground=active_fg_button,
                command=lambda i=i, j=j: set_tile(i, j)
            )
            button.grid(row=i, column=j, padx=5, pady=5)
            buttons[i][j] = button

def create_controls(root):
    global moves_label
    control_frame = tk.Frame(root, bg=bg_int)
    control_frame.grid(row=3, column=0, columnspan=3, pady=10)

    solve_button = tk.Button(
        control_frame, text="Solve", font=("Arial", 14, "bold"),
        bg=bg_body, fg=fg_button, activebackground=fg_button, activeforeground=active_fg_button,
        command=solve_puzzle
    )
    solve_button.pack(side=tk.LEFT, padx=10)

    step_button = tk.Button(
        control_frame, text="Step", font=("Arial", 14, "bold"),
        bg=bg_body, fg=fg_button, activebackground=fg_button, activeforeground=active_fg_button,
        command=step_solution
    )
    step_button.pack(side=tk.LEFT, padx=10)

    moves_label = tk.Label(
        root, text="Moves: ", font=("Arial", 14, "bold"),
        bg=bg_int, fg=fg_int, wraplength=250, justify="center"
    )
    moves_label.grid(row=4, column=0, columnspan=3, pady=10)

def set_tile(i, j):
    global state
    current_value = state[i][j]
    new_value = (current_value + 1) % 9
    state[i][j] = new_value
    update_grid()

def update_grid():
    global state, buttons
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            text = str(value) if value != 0 else ""
            buttons[i][j].config(text=text)

def solve_puzzle():
    global state, solution, solution_index, moves_label
    initial_state = tuple(tuple(row) for row in state)
    solution = bfs_solver(initial_state)
    solution_index = 0
    if solution:
        moves_label.config(text=f"Moves:\n{' '.join(solution)}")
    else:
        moves_label.config(text="No solution found.")

def step_solution():
    global solution, solution_index
    if solution and solution_index < len(solution):
        move = solution[solution_index]
        make_move(move)
        solution_index += 1

def make_move(move):
    global state
    x, y = find_blank(state)
    dx, dy = MOVES[move]
    new_x, new_y = x + dx, y + dy
    state = swap(state, x, y, new_x, new_y)
    update_grid()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sliding Puzzle Solver")
    root.configure(bg=bg_int)
    create_grid(root)
    create_controls(root)
    root.mainloop()