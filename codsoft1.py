import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Game logic
def determine_winner(user_choice):
    global user_score, computer_score

    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)

    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    # Update labels
    user_choice_label.config(text=f"Your choice: {user_choice}")
    comp_choice_label.config(text=f"Computer's choice: {computer_choice}")
    result_label.config(text=f"Result: {result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# GUI setup
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x300")
window.config(padx=20, pady=20)

# Labels
user_choice_label = tk.Label(window, text="Your choice:", font=("Arial", 12))
user_choice_label.pack()

comp_choice_label = tk.Label(window, text="Computer's choice:", font=("Arial", 12))
comp_choice_label.pack()

result_label = tk.Label(window, text="Result:", font=("Arial", 14, 'bold'))
result_label.pack(pady=10)

score_label = tk.Label(window, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack()

# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

tk.Button(button_frame, text="Rock", width=10, command=lambda: determine_winner("Rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=10, command=lambda: determine_winner("Paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", width=10, command=lambda: determine_winner("Scissors")).grid(row=0, column=2, padx=5)

# Run app
window.mainloop()