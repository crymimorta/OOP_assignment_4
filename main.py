from datetime import datetime
from User import User
from UserUtil import UserUtil
from UserService import UserService

if __name__ == "__main__":
    user = User(UserUtil.generate_user_id(), "Bektur", "Momunov", datetime(2005, 3, 19))
    user2 = User(UserUtil.generate_user_id(), "Bayastan", "Zamirbekov", datetime(2005, 4, 29))
    print(user.get_details())
    print(f"Age: {user.get_age()}")
    print(f"Email: {user.email}")

    UserService.add_user(user)
    UserService.add_user(user2)

    found_user = UserService.find_user(user2.user_id)
    print("Found User:", found_user.get_details() if found_user else "Not found")

    password = UserUtil.generate_password()
    print("Generated Password:", password)
    print("Password Strength:", "Strong" if UserUtil.is_strong_password(password) else "Weak")

    print("Email Valid:", "Valid" if UserUtil.validate_email(user.email) else "Invalid")
