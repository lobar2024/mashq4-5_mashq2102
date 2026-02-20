
#4
# class Worker:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def info(self):
#         print(f'{self.name} {self.salary} million som maosh oladi')
#
# class Driver(Worker):
#     def __init__(self, name, salary, car_type):
#         super().__init__(name, salary)
#         self.car_type = car_type
#
#     def info(self):
#         super().info()
#         print(f'U {self.car_type} rusumli mashina haydaydi')
#
# d = Driver('Eleven', 40, 'Mercedes')
# d.info()

#5
# class Phone:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def call(self):
#         print('Qongiroq qilinmoqda...')
#
# class Smartphone(Phone):
#     def __init__(self, brand, model, os):
#         super().__init__(brand, model)
#         self.os = os
#
#     def call(self):
#         super().call()
#         print(f'Sizga {self.os} orqali internet qongirogi amalga oshirildi')
#
# phone = Smartphone('iPhone', 12, 'Mobiuz')
# phone.call()
