class Employee:
    def __init__(self, id, first, last, profession, pay, car_id):
        self.id = id
        self.first = first
        self.last = last
        self.profession = profession
        self.pay = pay
        self.car_id = None

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'.lower()

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def __repr__(self):
        return f'First name: {self.first} \nLast name: {self.last} \nProfession: {self.profession} \nPay rate: {self.pay}'


class Car:
    def __init__(self, car_id, make, model):
        self.car_id = car_id
        self.make = make
        self.model = model

    def __repr__(self):
        return f'Make: {self.make} \nModel: {self.model}'

