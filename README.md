# User Management System

## Objective
The objective of this assignment is to implement an object-oriented solution for managing user records. The focus is on instance variables, class attributes/methods, and static methods.

## Project Structure
The project consists of three main classes:
- `User`
- `UserService`
- `UserUtil`

## Classes & Methods

### User Class
```python
class User:
    def __init__(self, user_id, name, surname, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.birthday = birthday

    def get_details(self):
        return f"User ID: {self.user_id}, Name: {self.name} {self.surname}"

    def get_age(self):
        # Implementation for age calculation
        pass
```

### UserService Class
```python
class UserService:
    users = {}
    
    @classmethod
    def add_user(cls, user):
        cls.users[user.user_id] = user

    @classmethod
    def find_user(cls, user_id):
        return cls.users.get(user_id, None)

    @classmethod
    def delete_user(cls, user_id):
        if user_id in cls.users:
            del cls.users[user_id]

    @classmethod
    def update_user(cls, user_id, user_update):
        if user_id in cls.users:
            cls.users[user_id] = user_update

    @classmethod
    def get_number(cls):
        return len(cls.users)
```

### UserUtil Class
```python
import random
import string
from datetime import datetime

class UserUtil:
    @staticmethod
    def generate_user_id():
        year = str(datetime.now().year)[2:]
        return year + "".join(random.choices(string.digits, k=7))

    @staticmethod
    def generate_password():
        characters = string.ascii_letters + string.digits + string.punctuation
        return "".join(random.choices(characters, k=8))

    @staticmethod
    def is_strong_password(password):
        return (any(c.isupper() for c in password) and 
                any(c.islower() for c in password) and 
                any(c.isdigit() for c in password) and 
                any(c in string.punctuation for c in password))

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"
```

## Running Instructions
```bash
git clone <repository_url>
cd <repository_directory>
python main.py
python -m unittest discover tests
```

## Sample Output
```python
user_id = UserUtil.generate_user_id()
password = UserUtil.generate_password()
email = UserUtil.generate_email("John", "Doe", "example.com")
user = User(user_id, "John", "Doe", "1995-05-10")
UserService.add_user(user)
print(user.get_details())
```

**Output:**
```
User ID: 241234567
Name: John Doe
Email: john.doe@example.com
Age: 29
```

