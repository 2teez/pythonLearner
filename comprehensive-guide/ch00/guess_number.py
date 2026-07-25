#!/usr/bin/env python3


def user_input(msg: str) -> int:
    return int(input(msg).strip())


def main() -> None:
    guess_number = 2337
    counter = 0
    user_guessed_number = -1
    while user_guessed_number != guess_number:
        user_guessed_number = user_input("Guess the number: ")
        if user_guessed_number < guess_number:
            print("Too low!")
        elif user_guessed_number > guess_number:
            print("Too high!")
        counter += 1
    print(f"You guessed the number in {counter} tries!")


if __name__ == "__main__":
    main()
