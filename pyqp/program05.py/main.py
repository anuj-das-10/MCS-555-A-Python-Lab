""" 5. Create an Employee module which has the following functions:
        DA = 40% of basic
        HRA = 15% of basic
        PF = 12% of basic
        Income Tax = 10% of basic

Write a python program to calculate the gross(basic + DA + HRA) and 
net(gross - PF - Income Tax) salary of an employee using the Employee module.
"""

import Employee as e

basic = 25500
print(f"Gross Salary:  {e.get_gross_salary(basic)}")
print(f"Net Salary:  {e.get_net_salary(basic)}")
