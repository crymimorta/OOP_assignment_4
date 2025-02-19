import random 
import string
from datetime import datetime
import re

class UserUtil:
    @staticmethod
    def generate_user_id():
        year_prefix = str(datetime.now().year % 100)
        random_digits = ''.join(random.choices(string.digits, k=7))  
        return int(year_prefix + random_digits)

    @staticmethod
    def generate_password():
        while True:
            password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=8))
            if UserUtil.is_strong_password(password):
                return password

    @staticmethod
    def is_strong_password(password):
        return (
            len(password) >= 8 and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)
        )

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain.lower()}"

    @staticmethod
    def validate_email(email):
        pattern = r'^[a-z]+\.[a-z]+@[a-z]+\.(edu\.kg)$'
        return bool(re.match(pattern, email))
