def check_password_strength(password):
    string = ""
    if len(password) < 14:
        string += "Password must be at least 12 characters long.\n"
    if not any(char.isupper() for char in password):
        string += "Password must contain at least one uppercase letter.\n"
    if not any(char.islower() for char in password):
        string += "Password must contain at least one lowercase letter.\n"
    if not any(char.isdigit() for char in password):
        string += "Password must contain at least one digit.\n"
    if not any(char in "!@^&#~`$%*()[]{}<>|;:+-_=\"',.?/" for char in password):
        string += "Password must contain at least one special character.\n"

    if not string:
        print("Password is strong.")
    elif len(string.splitlines()) <= 2:
        print("Password is weak. " + string)
    else:       
        print("Password is very weak. " + string)
    

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    check_password_strength(password)   


