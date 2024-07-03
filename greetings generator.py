def generate_greeting(first_name, last_name):
    """Generate a greeting message for a person with the given first and last name."""
    return f"Hello, {first_name} {last_name}! You just developed Python"

def main():
    """Run the program and print the greeting message."""
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    greeting = generate_greeting(first_name, last_name)
    print(greeting)

if __name__=="__main__":
    main()

    
