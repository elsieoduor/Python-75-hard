import random

def number_guessing_game():
  print("Welcome to the number guessing game")
  secret_number = random.randint(1, 100)
  attempts = 0
  max_attempts = 10

  while True:
    guess = input("Enter your guess(between 1 and 100): ")

    if not guess.isdigit():
      print("Enter a valid number.")
      continue
    guess = int(guess)
    attempts += 1

    if guess < secret_number:
      print("Too low!")
    elif guess > secret_number:
      print("Too high!")
    else:
      print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
      break

    if attempts >= max_attempts:
      print(f"Sorry, you've used all your attempts. The number was {secret_number}.")
      break

if __name__ == "__main__":
  number_guessing_game()