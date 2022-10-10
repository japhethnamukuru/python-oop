import unittest
from employee import Employee

class EmployeeTest(unittest.TestCase):
    '''A simple test case to test the employee class methods'''

    def setUp(self):
        '''General setup method'''
        self.first_name = 'John'
        self.last_name = 'Doe'
        self.salary = 5000

    def test_employee_give_rise(self):
        emp = Employee(self.first_name, self.last_name, self.salary)

        self.assertEqual(emp.give_raise(), 10000)


    def test_employee_give_rise_custom(self):
        emp1 = Employee(self.first_name, self.last_name)

        self.assertEqual(emp1.give_raise(), 5000)

unittest.main()