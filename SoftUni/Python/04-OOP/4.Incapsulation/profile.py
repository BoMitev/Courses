import re


def validate(password):
    if 8 > len(password) or re.search('[A-Z]', password) is None or re.search('[0-9]', password) is None:
        return False
    return True


class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) not in range(5, 16):
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, value):
        if not validate(value):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
