import random
import string


def generate_password(
    length=12, use_uppercase=True, use_numbers=True, use_symbols=True
):
    # Base character set
    char_set = list(string.ascii_lowercase)

    if use_uppercase:
        char_set += list(string.ascii_uppercase)
    if use_numbers:
        char_set += list(string.digits)
    if use_symbols:
        char_set += list("!@#$%^&*()-_=+[]{};:,.<>?")

    # Ensure at least one character from each selected type is included
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice("!@#$%^&*()-_=+[]{};:,.<>?"))

    # Fill the rest of the password with a random mix of the char_set
    while len(password) < length:
        password.append(random.choice(char_set))

    random.shuffle(password)  # Shuffle for randomness
    return "".join(password)  # Convert list to string and return it


if __name__ == "__main__":
    # Example usage
    length = int(input("Enter password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_nums = input("Include numbers? (y/n): ").lower() == "y"
    use_syms = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(length, use_upper, use_nums, use_syms)
    print("Generated Password:", password)
