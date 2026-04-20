import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Game state
board = [""] * 9
current_player = "X"
# Stats
x_wins = 0
o_wins = 0
draws = 0
def check_winner():
    global x_wins, o_wins, draws
    win_combinations = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] != "":
            winner = board[a]
            if winner == "X":
                x_wins += 1
            else:
                o_wins += 1
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_board()
            return
    if "" not in board:
        draws += 1
        messagebox.showinfo("Game Over", "It's a Draw!")
        reset_board()
def button_click(index):
    global current_player
    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)
        check_winner()
        current_player = "O" if current_player == "X" else "X"
def reset_board():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for btn in buttons:
        btn.config(text="")
def show_graph():
    labels = ['X Wins', 'O Wins', 'Draws']
    values = [x_wins, o_wins, draws]

    plt.figure()
    plt.bar(labels, values)
    plt.title("Game Statistics")
    plt.xlabel("Outcome")
    plt.ylabel("Count")
    plt.show()
# gui
root = tk.Tk()
root.title("Tic Tac Toe")
buttons = []
frame = tk.Frame(root)
frame.pack()
for i in range(9):
    btn = tk.Button(frame, text="", font=('Arial', 20), width=5, height=2,
                    command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)
# buttons
control_frame = tk.Frame(root)
control_frame.pack()
reset_btn = tk.Button(control_frame, text="Reset Game", command=reset_board)
reset_btn.grid(row=0, column=0, padx=10)

graph_btn = tk.Button(control_frame, text="Show Stats Graph", command=show_graph)
graph_btn.grid(row=0, column=1, padx=10)

root.mainloop()
