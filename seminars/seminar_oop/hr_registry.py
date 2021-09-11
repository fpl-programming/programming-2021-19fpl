# pylint: skip-file
from seminars.seminar_oop.employee import Employee


class HRRegistry:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.registry = {}
        self.counter = 1

    def add_employee(self, employee: Employee):
        self.registry[self.counter] = employee
        self.counter += 1


employee_1 = Employee('Ivan', 25, 40000)
employee_2 = Employee('Boris', 30, 10000000)

hr_registry = HRRegistry('HSE', 'Kostina')
print(hr_registry.registry)
hr_registry.add_employee(employee_1)
print(hr_registry.registry)
hr_registry.add_employee(employee_2)
print(hr_registry.registry)
