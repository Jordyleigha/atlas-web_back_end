from db import DB

if __name__ == "__main__":
    db = DB()
    user = db.add_user("eggmin@eggsample.com", "hashedpwd")
    
    # Check if the user was added successfully
    if user:
        print("DB.add_user returns a user object: True")
    else:
        print("DB.add_user returns a user object: False")
