# Simple Guessing Game AI Program 



def simple_ai_guessing_game(low, high):
    attempts = 0
    print(f"Think of a number between {low} and {high} for the AI to guess.")

    while low <= high:
        guess = (low + high) // 2  # The AI guesses the middle number
        attempts += 1
        user_feedback = input(f"Is the number {guess}? Type 'high', 'low', or 'correct': ").strip().lower()

        if user_feedback == 'high':
            high = guess - 1  # The guess was too high, adjust the search range
        elif user_feedback == 'low':
            low = guess + 1   # The guess was too low, adjust the search range
        elif user_feedback == 'correct':
            print(f"The AI guessed your number {guess} in {attempts} attempts!")
            return
        else:
            print("Please type 'high', 'low', or 'correct'.")

    print("It seems there was a mistake. Let's try again.")

simple_ai_guessing_game(1, 100)
