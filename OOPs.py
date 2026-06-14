# class EncapsulationDemo:

#     def __init__(self, value):
#         self.__private_value = value

#     def get_value(self):
#         return self.__private_value

#     def set_value(self, new_value):
#         if new_value >= 0:
#             self.__private_value = new_value

# demo = EncapsulationDemo(10)

# print(demo.get_value())

# demo.set_value(20)

# print(demo.get_value())






# class Calculator:  (abstraction)

#     def add(self, x, y):
#         return x + y

#     def subtract(self, x, y):
#         return x - y

#     def multiply(self, x, y):
#         return x * y

#     def divide(self, x, y):
#         if y != 0:
#             return x / y
#         else:
#             return "Cannot divide by zero"




#ABSTRACT METHOD
# from abc import ABC, abstractmethod

# class Vehicle(ABC):

#     @abstractmethod
#     def start_engine(self):
#         pass

# class Car(Vehicle):

#     def start_engine(self):
#         return "Car engine started"

# class Bike(Vehicle):

#     def start_engine(self):
#         return "Bike engine started"

# toyota = Car()
# honda = Bike()

# print(toyota.start_engine())
# print(honda.start_engine())






#Polymorphism
# class Animal:

#     def sound(self):
#         print("Animal sound")

# class Dog(Animal):

#     def sound(self):
#         print("Bark")

# class Cat(Animal):

#     def sound(self):
#         print("Meow")

# d = Dog()
# c = Cat()

# d.sound()
# c.sound()
















    


