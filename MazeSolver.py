import random
import time
import tkinter as tk

# ======================
# CONFIG
# ======================
N = int(input("Masukkan ukuran maze (misal 6): "))

# ======================
# GENERATE MAZE (PASTI ADA JALAN)
# ======================
def generate_maze(n):
    maze = [[1 for _ in range(n)] for _ in range(n)]

    x, y = 0, 0
    maze[x][y] = 0

    # bikin jalur random ke goal
    while (x, y) != (n-1, n-1):
        directions = []
        if x < n-1: directions.append((x+1, y))  # bawah
        if y < n-1: directions.append((x, y+1))  # kanan

        nx, ny = random.choice(directions)
        maze[nx][ny] = 0
        x, y = nx, ny

    # buka jalan lain biar ga terlalu lurus
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 1 and random.random() < 0.3:
                maze[i][j] = 0

    return maze

maze = generate_maze(N)
path = [[0]*N for _ in range(N)]

# ======================
# TERMINAL VISUAL
# ======================
def print_maze():
    print("\n")
    for i in range(N):
        for j in range(N):
            if path[i][j] == 1:
                print("🟩", end=" ")
            elif maze[i][j] == 1:
                print("⬛", end=" ")
            else:
                print("⬜", end=" ")
        print()
    time.sleep(0.05)

# ======================
# GUI
# ======================
root = tk.Tk()
root.title("Maze Solver AI")

canvas = tk.Canvas(root, width=N*40, height=N*40)
canvas.pack()

def draw():
    canvas.delete("all")
    for i in range(N):
        for j in range(N):
            color = "white"

            if maze[i][j] == 1:
                color = "black"
            if path[i][j] == 1:
                color = "green"

            canvas.create_rectangle(
                j*40, i*40,
                j*40+40, i*40+40,
                fill=color
            )

# ======================
# SOLVER (BACKTRACKING)
# ======================
def is_safe(x, y):
    return 0 <= x < N and 0 <= y < N and maze[x][y] == 0

def solve(x, y):

    if x == N-1 and y == N-1:
        path[x][y] = 1
        print("🎉 JALAN DITEMUKAN!")
        print_maze()
        draw()
        return True

    if is_safe(x, y):

        path[x][y] = 1
        print_maze()
        draw()
        root.update()
        root.after(50)

        if solve(x, y+1): return True
        if solve(x+1, y): return True
        if solve(x, y-1): return True
        if solve(x-1, y): return True

        path[x][y] = 0
        print_maze()
        draw()
        root.update()
        root.after(50)

    return False

# ======================
# RUN
# ======================
solve(0, 0)
root.mainloop()
