users = {}

def signUp(username, password):
    if users.get(username) is not None:
        print("A user with this username already exists. Please choose a new username")
        return False

    users[username] = hash(password)

def logIn(username, password): 
    if users.get(username) is None:
        print("Username or password is incorrect.")
        return False
    
    if hash(password) == users[username]:
        print("Logged in!")
        return True
    else:
        print("Username or password is incorrect.")
        return False

if __name__ == "__main__":
    signUp("omari", "weak-password")

    if logIn("omari", "weak-password"):
        print("access granted")
    else:
        print("access denied")