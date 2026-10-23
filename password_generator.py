
import secrets
import string
import random


def generate_password(length=16):
    if length < 12:
        raise ValueError("Password must be at least 12 characters.")

    categories = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        "!@#$%^&*"
    ]

    # Guarantee one character from each category
    password = [
        secrets.choice(category)
        for category in categories
    ]

    # Fill remaining positions securely
    all_characters = "".join(categories)

    password.extend(
        secrets.choice(all_characters)
        for _ in range(length - len(password))
    )

    # Shuffle using cryptographically secure randomness
    secure_random = random.SystemRandom()
    secure_random.shuffle(password)

    return "".join(password)
