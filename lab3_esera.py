# Esera Alarqaban | Lab 3 | Intro to Python
# Esera Alarqaban | Lab 3 | Intro to Python

# Ticket 1
username = "esera2026"

# PREDICT: 9
print(len(username))

# EXPLAIN: len() counts every character, including numbers and symbols.


# Ticket 2
# PREDICT: The first and last letters will print.
print(username[0])
print(username[len(username)-1])

# EXPLAIN: The last index is length minus 1 because indexes start counting at 0.


# Ticket 3
# PREDICT: Both lines will look identical.
print("Welcome to Loop, @" + username + "!")
print(f"Welcome to Loop, @{username}!")

# EXPLAIN: f-strings feel easier because they are cleaner to write.


# Ticket 4
# PREDICT: The program will crash because strings cannot be changed.
# TypeError: 'str' object does not support item assignment

# username[0] = "X"

print(username.upper())

# EXPLAIN: Immutable means a string cannot have individual characters changed.


# Ticket 5
feed = [
    "Learning Python today",
    "Finished my homework",
    "Building my first app"
]

# PREDICT: 3 and the first caption will print.
print(len(feed))
print(feed[0])

# EXPLAIN: I used index 0 because lists start counting from zero.


# Ticket 6
feed.append("Coding is fun")

# PREDICT: The new post will have index 3.
print(feed)

# EXPLAIN: The fourth post is index 3 because counting starts at 0.


# Ticket 7
feed.pop(0)
feed.sort()

# PREDICT: The oldest post is removed and the rest are alphabetized.
print(feed)

# EXPLAIN: pop removes an item and sort puts items in alphabetical order.


# Ticket 8
profile = {
    "username": username,
    "followers": 200,
    "verified": False
}

# PREDICT: 200 will print.
print(profile["followers"])

# profile[0]

# EXPLAIN: Dictionaries use keys instead of numbers because values are stored by names.


# Ticket 9
profile["followers"] = profile["followers"] + 50
profile["bio"] = "Python student learning new skills"

print(profile)

print(profile.get("age"))

# PREDICT: None will print.
# EXPLAIN: get() is safer because it does not crash when a key is missing.


# Ticket 10
print(f"@{profile['username']} has {profile['followers']} followers and {len(feed)} posts. Top post: {feed[0]}")

# PREDICT: The profile summary line will print.
# EXPLAIN: I used a string, list, and dictionary to create this line.