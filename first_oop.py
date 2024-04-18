from datetime import datetime
import csv

class Vehicle:
    color = 'white'
    catalog = []

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.__capacity = {}
        Vehicle.catalog.append({'name': self.name, 'max_speed': self.max_speed, 'mileage': self.mileage})

    # @property
    # def capacity(self):
    #     return self.__capacity


    def seating_capacity(self, capacity=0):
        self.__capacity[self.name] = int(capacity)
        return f'{self.name} is able to carry {capacity} passengers.'


    def category(self):
        if self.__capacity[self.name] <= 10:
            return 'passenger car'
        elif 10 < self.__capacity[self.name] <= 20:
            return 'minibus'
        elif self.__capacity[self.name] > 20:
            return 'passenger bus'
        return 'Capacity is not identified.'


    def __repr__(self):
        return self.name

    @classmethod
    def upload_data_from_csv(cls):
        with open('cars.csv', 'r') as f:
            data = csv.DictReader(f)
            data_converted = list(data)

        for item in data_converted:
            Vehicle(name=item['name'], max_speed=item['max_speed'], mileage=item['mileage'])
        print(f'{len(cls.catalog)} of data has been uploaded.')


class Bus(Vehicle):
    color = 'green'
    def __init__(self, name, max_speed, mileage, assembled_date):
        assert type(assembled_date) == str, 'Input date as string in compliance with YYYY-MM-DD format'
        super().__init__(name, max_speed, mileage)
        assembled_date = assembled_date.split('-')
        self.assembled_date = datetime(int(assembled_date[0]), int(assembled_date[1]), int(assembled_date[2]))


    def age(self):
        age = datetime.now() - self.assembled_date
        return f'{age.days} days have passed since its first assembly.'



v = Vehicle('Audi', 220, 150000)
b = Bus('Kia', 180, 75000, '2024-1-1')
v.upload_data_from_csv()