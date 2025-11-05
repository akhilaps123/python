def customer_feedback_system():
    try:
        users = input("Enter their name:").strip()
        if not users:
            raise ValueError("Error,Name cannot be empty")
        feedback = input("Enter feedback:").strip()
        if not feedback:
            raise ValueError("Error,feedback cannot be empty")
        print(f"Thank you for your feedback!")
        print(f"users:{users}")
        print(f"feedback:{feedback}")
    except ValueError as e:
        print(e)
    finally:
        print(f"Process completed - Thank you for visiting our restaurant!") 
customer_feedback_system() 

# You are building a simple customer feedback system for a local restaurant. The system should ask users to enter their name and feedback. Your task is to:
# Ask the user to enter their name and feedback.
# If the user leaves the name or feedback empty, display an error message using exception handling.
# If all inputs are valid, print a thank-you message along with the user's name and feedback.
# Use the try, except, and finally blocks to structure your code safely.

