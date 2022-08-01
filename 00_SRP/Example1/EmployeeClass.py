# Naive implementation
class Employee:
    def __init__(self, name):
        """
        Employee Data is stored here
        """
        self.name = name
    
    def _regular_hours(self):
        print("A way to calculate non-overtime hours.")

    def calculate_pay(self):
        x = self._regular_hours()
        print("Calculating the pay using x.")

    def report_hours(self):
        x = self._regular_hours()
        print("Reporting the hours using x.")

    def save(self):
        print("Save employee data in database.")


# Changing the code in the regular_hours() function based on the requirements of one actor,
# e.g accounting, will result in wrong numbers in the report_hours() function. However, a sufficient
# test suite might catch the error early on but you still have to fix it while not creating 
# a mess. So you have to apply changes to the Employee class to change how employees are
# defined AND to adjust the way regular hours are calcuated. So there would be an additional
# reason to change the class. 

# Solution: facade implementation pattern

class Employee:
    def __init__(self, name):
        """
        Employee Data is stored here
        """
        self.name = name

    def calculate_pay(self):
        pc = PayCaculator()
        print("Calculating the pay using pc.")

    def report_hours(self):
        hr = HourReporter()
        print("Reporting the hours using hr.")

    def save(self):
        es = EmployeeSaver()
        print("Save employee data in database.")


class HourReporter:
    def report_hours(self):
        rh = RegularHoursCalculator()

class PayCaculator:
    def calculate_pay(self):
        rh = RegularHoursCalculator()
        pass

class EmployeeSaver:
    def save_employee(self):
        pass

class RegularHoursCalculator:
    def regular_hours(self):
        print("A way to calculate non-overtime hours.")

# While this solution looks more complicated than the original approach, we have to keep in 
# mind that a lot more functions will be used inside the classes. You probably need a few more
# functions to calculate the pay for an employee. Now there's only one single reason to change
# a class and therefore to recompile it when using other programming languages like Rust or Java.