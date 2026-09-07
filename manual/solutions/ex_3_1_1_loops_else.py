# Write a program that displays all prime numbers between 1 and 100. Do it in
# two versions: with and without an else clause for the for.

# without `else` - a boolean variable is needed:
for nr in range(2, 100):
    is_prime = True
    for i in range(2, int(nr**0.5) + 1):
        if nr % i == 0:
            is_prime = False
            break
    if is_prime:
        print(nr, end=" ")

print()

# with `else`:
for nr in range(2, 100):
    for i in range(2, int(nr**0.5) + 1):
        if nr % i == 0:
            break
    else:
        print(nr, end=" ")


# Write an authenticate_user function that receives correct_password as
# parameter. The function should ask the user for the password, for a maximum of
# 3 attempts. If the password is correct, print Access granted. If the password
# is incorrect, display the number of attempts left. If the attempts are
# exhausted, print Access denied.

def authenticate_user_wo_else(correct_password):
    attempts = 3
    while attempts:
        password = input("Insert password: ")
        if password == correct_password:
            print("Access granted.")
            break
        else:
            attempts -= 1
            print(f"Incorrect password. Remaining attempts: {attempts}")
    if attempts == 0:
        print("Access denied.")


def authenticate_user(correct_password):
    attempts = 3
    while attempts:
        password = input("Insert password: ")
        if password == correct_password:
            print("Access granted.")
            break
        else:
            attempts -= 1
            print(f"Incorrect password. Remaining attempts: {attempts}")
    else:
        print("Access denied.")


authenticate_user("pass123")
