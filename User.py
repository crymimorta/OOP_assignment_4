from datetime import datetime
from UserUtil import UserUtil

class User:
    def __init__(self, user_id: int, name: str, surname: str, birthday: datetime):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.email = UserUtil.generate_email(name, surname, "alatoo.edu.kg")

    def get_details(self):
        return f"User's ID: {self.user_id}, Name: {self.name}, Surname: {self.surname}, Birthday: {self.birthday.strftime('%Y-%m-%d')}"
    
    def get_age(self, year=None):
        if year is None:
            year = datetime.today().year
        return year - self.birthday.year
