import random


class ValueOutOfRange(Exception):
    """
    Exception: Value is out of the defined range
    """
    pass


def take_guess() -> int:
    """
    Funcion to take user input for a guess of the 
    target number

    Returns:
        int: guessed number
    """
    guess = int(input("Enter your guess: "))
    return guess


if __name__ == "__main__":
    # Generate a random number within a range
    minimum = 0
    maximum = 100
    target_number = random.randint(minimum, maximum)

    max_guesses = 6
    num_guesses = 0

    while True:
        # Check that we have enough guesses left
        # An example of checking a condiion using an "if" statement
        if num_guesses >= max_guesses:
            print("You've run out of guesses! Better luck next time.")
            print(f"The correct answer was: {target_number}")
            break
        try:
            guess = take_guess()
            if guess not in range(minimum, maximum + 1):
                # Example of raising a custom exception
                raise ValueOutOfRange
            num_guesses += 1
        
        # Example of handlnig an error built into python
        except ValueError:
            print("Please enter a valid integer")
        
        # Handling the custom exception
        except ValueOutOfRange:
            print(f"Value is not in the range {minimum} to {maximum}")
        
        # Example of a "catch-all" exception
        except Exception as e:
            print(e)
        
        # This code block gets executed only when no errors have been picked up
        else:
            if guess > target_number:
                print("Too high! Try again")
            elif guess < target_number:
                print("Too low! Try again")
            else:
                print(f"Woo-hoo! You got it! The number was {target_number}")
                break
        
        # This code block gets executed everytime, irrespective of errors
        finally:
            print(f"Number of guesses remaining: {max_guesses - num_guesses}")
