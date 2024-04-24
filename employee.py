class Employee:
    def __init__(self, first, last, profession, pay):
        self.first = first
        self.last = last
        self.profession = profession
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'.lower()

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def __repr__(self):
        return f'First name: {self.first} \nLast name: {self.last} \nProfession: {self.profession} \nPay rate: {self.pay}'
