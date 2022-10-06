"""Mock Wordle!"""
__author__ = "Ayah Abdul-Haqq"


def contains_char(searched_string: str, single_character: str) -> bool:
    """Returns True if character is found at any index of first string, False if otherwise."""
    assert len(single_character) == 1
    index_of_word: int = 0
    while index_of_word < len(searched_string):
        if searched_string[index_of_word] == single_character:
            return True
        else:
            index_of_word += 1
    return False


def emojified(guessed_word: str, secret_word: str) -> str:
    """Returns color coded boxes depending on whether a character in a secret word matches a character in a guess word."""
    assert len(guessed_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    resulting_emoji: str = ""
    counter: int = 0
    while counter < len(guessed_word):
        if guessed_word[counter] == secret_word[counter]:
            resulting_emoji += GREEN_BOX
        elif contains_char(secret_word, guessed_word[counter]): 
            resulting_emoji += YELLOW_BOX
        else:
            resulting_emoji += WHITE_BOX
        counter += 1
    return resulting_emoji


def input_guess(expected_length: int) -> str:
    """Given a guess not of expected length, will prompt the user until their guess is of correct length."""
    user_guess: str = input(f"Enter a {expected_length} character word: ")

    while len(user_guess) != expected_length:
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turns_spent: int = 1
    player_win: bool = False
    
    while turns_spent < 7 and not player_win:
        print(f"=== Turn {turns_spent}/6 ===")
        user_guess = input_guess(len(secret_word))
        print(emojified(user_guess, secret_word))
        if user_guess == secret_word:
            player_win = True
        else:
            turns_spent += 1
    if player_win:
        print(f"You won in {turns_spent}/6 turns!")
    else: 
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()