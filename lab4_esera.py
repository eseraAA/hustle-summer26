# Esera Alarqaban | Lab 4 | Intro to Python



# Ticket 1
ages = [17, 11, 25, 13, 9]

# PREDICT: 17, 25, and 13 will get Access granted. 11 and 9 will get Too young.

for age in ages:
    if age >= 13:
        print(f"{age} — Access granted ✅")
    else:
        print(f"{age} — Too young ❌")

# EXPLAIN: The variable age holds the current age value from the list each time the loop runs.



# Ticket 2
keep_checking = "yes"

while keep_checking == "yes":
    age = int(input("Enter your age: "))

    if age >= 13:
        print("Access granted ✅")
    else:
        print("Too young ❌")

    keep_checking = input("Check another age? yes/no: ")

# PREDICT: If the user types no first, the loop stops after the first check.
# EXPLAIN: A while loop works better because we do not know how many times the user wants to enter an age.



# Ticket 3
while True:
    user_age = input("Enter your age or type stop: ")

    if user_age == "stop":
        break

    user_age = int(user_age)

    if user_age >= 13:
        print("Access granted ✅")
    else:
        print("Too young ❌")

# PREDICT: Without break, the loop would continue forever.
# EXPLAIN: Ticket 2 stops based on a yes/no answer, while this loop stops when the user types stop.



# Ticket 4
def can_access(age):
    if age >= 13:
        return True
    else:
        return False


for age in ages:
    if can_access(age):
        print(f"{age} — Access granted ✅")
    else:
        print(f"{age} — Too young ❌")

# PREDICT: The output looks the same as Ticket 1.
# EXPLAIN: A function is better because the code can be reused instead of rewriting the same check.



# Ticket 5
def signup_report(signups):
    approved = 0

    print("--- StreamPass Signup Report ---")

    for number, age in enumerate(signups, start=1):
        if can_access(age):
            print(f"Signup #{number} | Age {age} — Access granted ✅")
            approved += 1
        else:
            print(f"Signup #{number} | Age {age} — Too young ❌")

    print(f"Approved: {approved} out of {len(signups)}")


signups = [22, 10, 15, 8, 19, 13]

signup_report(signups)

# PREDICT: 4 people will be approved out of 6.
# EXPLAIN: I used functions, for loops, enumerate(), if/else statements, lists, variables, and counters.