# ============================================================
# LAB 5 - WEEK 5 : The VibeCheck Bug Hunt
# ============================================================
# Name: Esera Alarqaban
# ============================================================


# ------------------------------------------------------------
# PART 1 - A function that greets a user
# ------------------------------------------------------------

# BUG 1 fixed: added :
def send_vibe():
    print("VibeCheck says: good energy only")


# BUG 2 fixed: added indentation
def welcome_user():
    print("Welcome to VibeCheck!")


# ------------------------------------------------------------
# PART 2 - A function that uses a variable
# ------------------------------------------------------------

def show_mood():
    mood = "hyped"
    # BUG 3 fixed: changed mod to mood
    print(f"Today's mood is {mood}")


# ------------------------------------------------------------
# PART 3 - A function with parameters
# ------------------------------------------------------------

def make_shoutout(name, mood):
    return f"{name} is feeling {mood} today!"


# ------------------------------------------------------------
# PART 4 - A function that counts hype points
# ------------------------------------------------------------

def count_hype(likes, shares):
    # BUG 4 fixed: changed - to +
    total = likes + shares
    return total


# BUG 5 fixed: moved final_message function above the call
def final_message():
    print("Thanks for using VibeCheck!")


# ============================================================
# RUNNING THE CODE
# ============================================================

final_message()

send_vibe()
welcome_user()
show_mood()


# BUG 6 fixed: added print()
print(make_shoutout("Jordan", "creative"))


# BUG 7 fixed: added second argument
print(make_shoutout("Alex", "chill"))


# BUG 8 fixed: changed "ten" to 10
print(count_hype(10, 5))