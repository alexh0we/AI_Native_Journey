def generate_welcome_message(name, mood):
    """
    Generates a personalized welcome message based on name and mood.

    Args:
        name: The name of the person to welcome (string).
        mood: The person's mood (string).

    Returns:
        A personalized welcome message (string).
    """
    # Handle empty name case
    if not name:
        return "Hello! Welcome to our community. We're happy to have you here."
    
    # Convert mood to lowercase for consistent comparison
    mood = mood.lower() if mood else ""
    
    # Special greeting for Alex Howe with mood
    if name.lower() == "alex howe":
        base_message = f"Hey, it's the awesome AI Director, {name}!"
        return add_mood_to_message(base_message, mood)
    
    # VIP/Admin Recognition with mood
    vip_users = ["alex howe", "sarah admin", "john manager", "emma vip"]
    if name.lower() in vip_users:
        base_message = f"Welcome back, {name}! Your VIP status is active. 🎉"
        return add_mood_to_message(base_message, mood)
    
    # Regular greeting with mood
    base_message = f"Hello, {name}! Welcome to our community. We're happy to have you here."
    return add_mood_to_message(base_message, mood)

def add_mood_to_message(base_message, mood):
    """
    Adds mood-based enhancement to a base message.
    
    Args:
        base_message: The base welcome message (string).
        mood: The person's mood (string).
        
    Returns:
        Enhanced message with mood consideration (string).
    """
    if not mood:
        return base_message
    
    if mood == "happy":
        return f"{base_message} Great to see you're happy - your positive energy is contagious! 😊"
    elif mood == "sad":
        return f"{base_message} We're here for you and hope our community can brighten your day! 🌟"
    elif mood == "excited":
        return f"{base_message} Your excitement is infectious - let's make amazing things happen! 🚀"
    elif mood == "tired":
        return f"{base_message} Take it easy - we're here to support you! 💤"
    else:
        return base_message

# --- Example Usage ---
if __name__ == "__main__":
    print("Welcome Message Generator")
    print("=" * 30)
    
    # Get user's name
    user_name = input("Please enter your name (optional): ")
    
    # Get user's mood
    mood = input("How are you feeling today? (happy/sad/excited/tired/other): ")
    
    # Generate and display the personalized greeting
    message = generate_welcome_message(user_name, mood)
    print("\n" + message) 