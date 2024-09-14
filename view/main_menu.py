import os

def display_menu():
    print("Welcome to Simumation coin")
    print("1. Choose crypto")
    print("2. Buy crypto")
    print("3. Sell crypto")
    print("4. Crypto per minute")
    print("5. Crypto per hour")
    print("6. Crypto per day")
    print("7. Add to wallet")
    print("8. Choose currency")
    print("9. Check account")
    print("10. Quit")
    
def get_choices():
    while True:
        try:
            choice = int(input("Enter your choice: "))    
            if 1 <= choice <= 10:
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")

def main_menu():
    display_menu()
    choice = get_choices()
    return choice;

