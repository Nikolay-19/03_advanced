class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_valid_pass(self, value):
        upper = [char for char in value if char.isupper()]
        digit = [char for char in value if char.isdigit()]

        if len(upper) >= 1 and len(digit) >= 1 and len(value) >= 8:
            return True
        return False

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @username.setter
    def username(self, username):
        if len(username) < 5 or len(username) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = username

    @password.setter
    def password(self, value):
        if not self.is_valid_pass(value):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'
