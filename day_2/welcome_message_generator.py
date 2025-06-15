def generate_welcome_message(name):
    """
    Generates a personalized welcome message.

    Args:
        name: The name of the person to welcome (string).

    Returns:
        A personalized welcome message (string).
    """
    if name:
        return f"Hello, {name}! Welcome to our community. We're happy to have you here."
    else:
        return "Hello! Welcome to our community. We're happy to have you here."

# --- Example Usage ---
if __name__ == "__main__":
    user_name = input("Please enter your name (optional): ")
    message = generate_welcome_message(user_name)
    print(message) 