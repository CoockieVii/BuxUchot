from User import User


class Expenditure:
    def __init__(self, user: User, sum):
        self.user = user
        self.sum = sum
