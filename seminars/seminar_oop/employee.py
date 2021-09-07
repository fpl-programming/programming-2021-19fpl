from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def drink(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def work(self):
        pass


class Employee(Human):
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age)
        self.salary = salary

    def drink(self):
        print('drinking')

    def eat(self):
        print('eating')

    def work(self):
        print('working')

    def write(self):
        print('writing')


class Programmer(Employee):
    def __init__(self, name: str, age: int, salary: int, computer: str):
        super().__init__(name, age, salary)
        self.computer = computer

    def code(self):
        print('coding on', self.computer)


employee_1 = Employee('Ivan', 25, 40000)
employee_1.eat()
employee_1.drink()
employee_1.work()
employee_1.write()

programmer_1 = Programmer('Boris', 30, 10000000, 'mac')
programmer_1.eat()
programmer_1.drink()
programmer_1.work()
programmer_1.write()
programmer_1.code()

