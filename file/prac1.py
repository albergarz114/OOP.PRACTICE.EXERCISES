#username = input("What is your username? ")
#password = input(f"Type the password for the username {username}:")
#valid = {"username": "admin", "password": "admin"}

#if (username == 'admin' and password == 'admin'):
#    print("Welcome dude")

#else:
#    print("Not correct")

users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan"
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]

def get_user(username, password):
    for user in users:
        if user["name"] == username and user["password"] == password:
            return user
    return None

def show_offer(username, password):
    user = get_user(username, password)

    if not user or user["type"] == "Student":
        print("We have great courses to offer for you!")

username = input("What is your username? ").strip()
password = input(f"Type the password for the username {username}: ").strip()
show_offer(username, password)

