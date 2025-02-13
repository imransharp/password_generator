import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    """Generate a random password with the given length and character options."""
    
    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits if use_digits else ""
    special = string.punctuation if use_special_chars else ""

    # Combine all character pools
    all_chars = lower + upper + digits + special

    if not all_chars:
        raise ValueError("No character set selected for password generation.")

    # Ensure at least one character from each selected category
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits) if use_digits else "",
        random.choice(special) if use_special_chars else ""
    ]

    # Fill the rest of the password length
    password += random.choices(all_chars, k=length - len(password))

    # Shuffle to randomize the order
    random.shuffle(password)

    return "".join(password)

# Example Usage
if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    use_digits = input("Include digits? (yes/no): ").strip().lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"

    generated_password = generate_password(password_length, use_digits, use_special_chars)
    print(f"Generated Password: {generated_password}")
