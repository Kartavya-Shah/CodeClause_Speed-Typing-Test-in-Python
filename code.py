import random
import string
import time
import os

def generate_prompt(difficulty):
    if difficulty == "easy":
        words = random.sample(["developed by guido van rossum","python is a programming language"], k=2)
        prompt = " ".join(words)
    elif difficulty == "medium":
        words = random.sample(["developed by Guido van Rossum","Python is an object-oriented, high-level and interpreted programming language"], k=2)
        prompt = " ".join(words)
        prompt = prompt.capitalize()
        prompt = prompt + random.choice(string.punctuation)
    elif difficulty == "hard":
        prompt = "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics developed by Guido van Rossum."
        prompt = prompt.capitalize()
        prompt = prompt.replace(",", ",")
    return prompt

def typing_speed_test():
    levels = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}

    text = "TYPING SPEED TEST"
    terminal_width = os.get_terminal_size().columns
    padding = (terminal_width - len(text)) // 2
    print(" " * padding + text)
    print("\n")
    print("Select a level - Easy, Medium, or Hard")
    level = input().lower()
    while level not in levels.keys():
        print("Invalid level. Please select a valid level - Easy, Medium, or Hard")
        level = input().lower()
    
    prompt = generate_prompt(level)
    print("-" * 78) 
    print(f"\nType this: {prompt}\n")
    
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    total_time = end_time - start_time
    words_per_minute = len(user_input.split()) / total_time * 60
    accuracy = sum([1 for i, j in zip(user_input, prompt) if i == j]) / len(prompt) * 100
    print("-" * 78) 
    print("\nCalculating Results.....\n")
    time.sleep(3)
    print(f"You typed {len(user_input.split())} words in {total_time:.2f} seconds.")
    print(f"Your typing speed is {words_per_minute:.2f} words per minute.")
    print(f"Your typing accuracy is {accuracy:.2f}%.")
    print("\n.........Great job! Keep practicing to improve your speed and accuracy.........")

typing_speed_test()
