import tkinter as tk
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    update_ui(user_choice, computer_choice, result)
    update_history(user_choice, computer_choice, result)

def update_ui(user_choice, computer_choice, result):
    user_choice_label.config(text="Your Choice: " + user_choice)
    computer_choice_label.config(text="Computer's Choice: " + computer_choice)
    result_label.config(text="Result: " + ("You win!" if result == "user" else "You lose!" if result == "computer" else "It's a tie!"))

    global user_score, computer_score
    if result == "user":
        user_score += 1
    elif result == "computer":
        computer_score += 1
    score_label.config(text=f"Scores - You: {user_score}, Computer: {computer_score}")

def update_history(user_choice, computer_choice, result):
    history_text.insert(tk.END, f"You: {user_choice}, Computer: {computer_choice}, Result: {'Win' if result == 'user' else 'Lose' if result == 'computer' else 'Tie'}\n")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text=f"Scores - You: {user_score}, Computer: {computer_score}")
    history_text.delete('1.0', tk.END)

# GUI Setup
window = tk.Tk()
window.title("Rock Paper Scissors Game")

# Styling
window.configure(bg="#ddf")

# Game Buttons
button_frame = tk.Frame(window, bg="#ddf")
rock_button = tk.Button(button_frame, text="Rock", command=lambda: play("rock"))
paper_button = tk.Button(button_frame, text="Paper", command=lambda: play("paper"))
scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play("scissors"))
rock_button.pack(side=tk.LEFT)
paper_button.pack(side=tk.LEFT)
scissors_button.pack(side=tk.LEFT)
button_frame.pack(pady=10)

# Display Area
display_frame = tk.Frame(window, bg="#ddf")
user_choice_label = tk.Label(display_frame, text="Your Choice: ", bg="#ddf")
computer_choice_label = tk.Label(display_frame, text="Computer's Choice: ", bg="#ddf")
result_label = tk.Label(display_frame, text="Result: ", bg="#ddf")
user_choice_label.pack()
computer_choice_label.pack()
result_label.pack()
display_frame.pack(pady=10)

# Score
score_label = tk.Label(window, text="Scores - You: 0, Computer: 0", bg="#ddf")
score_label.pack()

# Game History
history_frame = tk.LabelFrame(window, text="Game History", bg="#ddf")
history_text = tk.Text(history_frame, height=10, width=50)
history_text.pack()
history_frame.pack(pady=10)

# Reset and Exit Buttons
reset_button = tk.Button(window, text="Reset Game", command=reset_game)
reset_button.pack(side=tk.LEFT, padx=10, pady=10)
exit_button = tk.Button(window, text="Exit Game", command=window.destroy)
exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Initialize scores
user_score, computer_score = 0, 0

# Main Loop
window.mainloop()
