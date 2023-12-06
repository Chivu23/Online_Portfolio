import uuid

from db.crud.users_crud import UsersDb


class User:

    def __init__(
            self,
            email,
            password,
            user_id=None,
            username=None,
            confirm_password=None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.user_db = UsersDb()

    def validate_create(self):
        """
        1. check if all inputs are received to create a new user
        2. check password ===> self._validate_password()
        3. check if the passwords is match
        """
        self._check_fields()
        self._validate_username()
        self._validate_password()
        self._check_password()

    def _check_fields(self):
        if not self.email or not self.password or not self.username or not self.confirm_password:
            raise Exception("u miss some values dear-beer!")

    def _validate_username(self):
        pass

    def _validate_password(self):
        if len(self.password) < 8:
            raise Exception("more words to password")

    def _check_password(self):
        if self.password != self.confirm_password:
            raise Exception("Sorry! The pass not match! Try again.")

    def add(self):
        self.validate_create()
        get_by_username = self.user_db.read(username=self.username)
        get_by_email = self.user_db.read(email=self.email)
        print(f"BY USERNAME {get_by_username}")
        print(f"BY EMAIL {get_by_email}")

        if get_by_email or get_by_username:
            raise Exception("Username or email already joined, so bring new one!")
        self.user_db.create(self._to_dict_create())

    def check_in_db(self):
        users = self.user_db.read(email=self.email)
        if not users:
            raise Exception("This user, my friend, is not found with this email")
        user = users[0]
        if user["password"] != self.password:
            raise Exception("Ooops! Invalid pass")
        return True

    def _to_dict_create(self):
        return {
            'id': str(uuid.uuid4()),
            'username': self.username,
            'password': self.password,
            'email': self.email
        }
