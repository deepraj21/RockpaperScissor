import tkinter as tk
import random

# Create a window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("540x400")

# Create labels and buttons
title_label = tk.Label(text="Rock Paper Scissors", font=("Arial", 20))
title_label.pack(pady=10)

player_choice_label = tk.Label(text="Choose your move:", font=("Arial", 16))
player_choice_label.pack(pady=10)

rock_button = tk.Button(text="Rock", width=10, font=("Arial", 14))
rock_button.pack(pady=5)

paper_button = tk.Button(text="Paper", width=10, font=("Arial", 14))
paper_button.pack(pady=5)

scissors_button = tk.Button(text="Scissors", width=10, font=("Arial", 14))
scissors_button.pack(pady=5)

result_label = tk.Label(text="", font=("Arial", 16))
result_label.pack(pady=10)

# Define the game logic


def play_game(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "Tie!"
    elif player_choice == "Rock" and computer_choice == "Scissors":
        result = "You win!"
    elif player_choice == "Paper" and computer_choice == "Rock":
        result = "You win!"
    elif player_choice == "Scissors" and computer_choice == "Paper":
        result = "You win!"
    else:
        result = "You lose!"

    result_label.config(
        text=f"You chose {player_choice}. Computer chose {computer_choice}. {result}")


# Bind the buttons to the game logic
rock_button.config(command=lambda: play_game("Rock"))
paper_button.config(command=lambda: play_game("Paper"))
scissors_button.config(command=lambda: play_game("Scissors"))

# Run the window
window.mainloop()
