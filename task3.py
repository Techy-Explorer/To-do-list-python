import random
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return None
def game():
    print("Welcome to the Fizz Buzz Game!")
    range_choice = input("Choose a range: 1 to 10 or 1 to 100? (Enter 10 or 100): ")
    while range_choice not in ['10', '100']:
        range_choice = input("Please enter a valid range (10 or 100): ")
    max_number = 10 if range_choice == '10' else 100
    player1_score = 0
    last_number = 0
    while True:
        player1_number = random.randint(1, max_number)
        print(f"\nPlayer 1 chose the number: {player1_number}")
        fizz_buzz_result = fizz_buzz(player1_number)
        print(f"Fizz Buzz result: {fizz_buzz_result if fizz_buzz_result else 'none'}")
        player2_guess = input("Player 2, is it 'fizz', 'buzz', or 'fizz buzz'? (or press Enter for none): ").strip().lower()        
        if fizz_buzz_result is not None and player2_guess == fizz_buzz_result:
            player1_score += 1
            print("Correct! Player 1 gets 1 point.")
        elif fizz_buzz_result is None and player2_guess == "":
            print("Correct! No points given but you guessed correctly.")
        else:
            print("Wrong guess! Game over.")
            break
        if player1_number % 3 != 0 and player1_number % 5 != 0:
            last_number += player1_number
            print(f"Current total (not displayed): {last_number}")

        print(f"Player 1's score: {player1_score}")

    print(f"Game over! Player 1's final score: {player1_score}")
game()