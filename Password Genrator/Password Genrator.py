# Password Genarator

import secrets
import string

MIN_LENGTH = 4  

def ask_yes_no(prompt):
    
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Please enter 'yes' or 'no'.")

def ask_int(prompt, minimum=1):
    
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if value < minimum:
            print(f"Please enter a number that is at least {minimum}.")
            continue
        return value

def choose_character_sets():
    
    options = [
        ("capital letters", string.ascii_uppercase),
        ("small letters", string.ascii_lowercase),
        ("numbers", string.digits),
        ("special characters", string.punctuation),
    ]

    while True:
        print("\nWhich types of characters do you want to include?")
        pools = [chars for name, chars in options
                if ask_yes_no(f"  Include {name}? (yes/no): ")]
        if pools:
            return pools
        print("\nYou must select at least one option. Please try again.")


def generate_password(length, pools):
    
    # Guarantee one character from each selected group
    password = [secrets.choice(pool) for pool in pools]

    # Fill the remaining positions from all selected characters
    all_chars = "".join(pools)
    password += [secrets.choice(all_chars) for _ in range(length - len(pools))]

    # Shuffle so the guaranteed characters are not always at the start
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def main():
    print("---------- PASSWORD GENERATOR ----------")

    length = ask_int(f"Enter your password length (minimum {MIN_LENGTH}): ",
                    MIN_LENGTH)
    pools = choose_character_sets()

    while True:
        count = ask_int("\nHow many passwords do you want to generate? ")

        print("\n---------- GENERATED PASSWORDS ----------")
        for i in range(1, count + 1):
            print(f"Password {i}: {generate_password(length, pools)}")
        print("---------------- DONE ----------------")

        if not ask_yes_no("\nGenerate more passwords? (yes/no): "):
            break

    print("Thank you for using Password Generator!")


if __name__ == "__main__":
    main()