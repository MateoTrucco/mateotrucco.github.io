# -------------------- IMPORTS --------------------
try:
    import sys, os, random
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
    from base_functions import enable_high_dpi, make_screen, c

    enable_high_dpi()
except ImportError:
    print("Error: base_functions module not found. Please ensure it is in the correct directory.")
    sys.exit(1)

# -------------------- CONSTANTS --------------------
FINAL_STATE = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
MOVES = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

# -------------------- GLOBAL VARIABLES --------------------
state = [[0 for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
solution = []
solution_index = 0
moves_label = None

# -------------------- FUNCTIONS --------------------
def find_blank(state):
    """Find the position of the blank tile (0) in the puzzle."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# --------------------------------------------------
def is_valid(x, y):
    """Check if the given coordinates are within the puzzle boundaries."""
    return 0 <= x < 3 and 0 <= y < 3

# --------------------------------------------------
def swap(state, x1, y1, x2, y2):
    """Swap two tiles in the puzzle and return the new state."""
    new_state = [list(row) for row in state]
    new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
    return [tuple(row) for row in new_state]

# --------------------------------------------------
def bfs_solver(initial_state):
    """Solve the sliding puzzle using Breadth-First Search (BFS)."""
    queue = [(initial_state, [])]
    visited = set()
    visited.add(tuple(tuple(row) for row in initial_state))

    while queue:
        current_state, path = queue.pop(0)
        if tuple(tuple(row) for row in current_state) == FINAL_STATE:
            return path
        x, y = find_blank(current_state)
        for move, (dx, dy) in MOVES.items():
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                new_state = swap(current_state, x, y, new_x, new_y)
                t_new_state = tuple(new_state)
                if t_new_state not in visited:
                    visited.add(t_new_state)
                    queue.append((new_state, path + [move]))
    return []

# --------------------------------------------------
def set_tile(i, j):
    """Set the value of a tile in the puzzle."""
    current_value = state[i][j]
    new_value = (current_value + 1) % 9
    state[i][j] = new_value
    update_grid()

# --------------------------------------------------
def update_grid():
    """Update the visual representation of the puzzle grid."""
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            text = str(value) if value != 0 else ""
            buttons[i][j].config(text=text)

# --------------------------------------------------
def solve_puzzle():
    """Solve the puzzle and display the solution."""
    global solution, solution_index
    initial_state = [tuple(row) for row in state]
    solution = bfs_solver(initial_state)
    solution_index = 0
    moves_label.config(text=f"Moves:\n{' '.join(solution) if solution else 'No solution found.'}")

# --------------------------------------------------
def step_solution():
    """Perform the next step in the solution."""
    global solution_index
    if solution and solution_index < len(solution):
        move = solution[solution_index]
        make_move(move)
        solution_index += 1

# --------------------------------------------------
def make_move(move):
    """Make a move in the puzzle."""
    global state
    x, y = find_blank(state)
    dx, dy = MOVES[move]
    new_x, new_y = x + dx, y + dy
    state = swap(state, x, y, new_x, new_y)
    update_grid()


# --------------------------------------------------
def randomize_state(steps=50):
    """Randomize the puzzle state by making random valid moves."""
    global state
    state = [list(row) for row in FINAL_STATE]
    last_move = None
    for _ in range(steps):
        x, y = find_blank(state)
        possible_moves = []
        for move, (dx, dy) in MOVES.items():
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                if last_move:
                    opposite = {'L':'R','R':'L','U':'D','D':'U'}[last_move]
                    if move == opposite:
                        continue
                possible_moves.append(move)
        if possible_moves:
            move = random.choice(possible_moves)
            make_move(move)
            last_move = move
    update_grid()
    moves_label.config(text="Moves:\n")


# -------------------- GUI SETUP --------------------
ui = make_screen(
    title="Sliding Puzzle Solver",
    use_title=False, use_input=False, use_button=False,
    use_loading_bar=False, use_output=False,
)

window = ui["window"]

for i in range(3):
    for j in range(3):
        btn = ui["add_element"](
            "button", row=i, col=j,
            font=("Arial", 18, "bold"), width=5, height=4,  
            command=lambda i=i, j=j: set_tile(i, j)
        )
        buttons[i][j] = btn
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)

solve_button = ui["add_element"](
    "button", text="Solve", row=0, col=4, width=8, height=2, font=("Arial", 12, "bold"), bg=c["g"],
    command=lambda: solve_puzzle()
)
step_button = ui["add_element"](
    "button", text="Step", row=1, col=4, width=8, height=2, font=("Arial", 12, "bold"), bg=c["y"],
    command=lambda: step_solution()
)
random_button = ui["add_element"](
    "button", text="Random", row=2, col=4, width=8, height=2, font=("Arial", 12, "bold"), bg=c["r"],
    command=randomize_state
)
moves_label = ui["add_element"](
    "label", text="Moves:\n", row=5, col=0, colspan="all", height=3, justify="center", anchor="n", bg=c["blu"],
)

# -------------------- MAIN LOOP --------------------
window.mainloop()
