# List to store both users
users = []

# Capture information for 2 users
for i in range(2):
    print(f"\nEnter information for User {i + 1}:")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    height = float(input("Enter height in cm: "))

    user = {
        "name": name,
        "age": age,
        "height": height
    }

    users.append(user)

# Function to calculate total combined height
def calculate_total_height(users):
    total = users[0]["height"] + users[1]["height"]
    return total

# Display each user's information using a loop
print("\n--- User Information ---")
for user in users:
    print(f"{user['name']} is {user['age']} years old and is {user['height']} cm tall.")

# Calculate and display total combined height
total = calculate_total_height(users)
print(f"\nThe total combined height of both users is {total} cm.")