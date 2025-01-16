from employee import Employee

def test_give_default_raise():
    employee = Employee('carlos', 'lopez', 255000)
    employee.give_raise()
    assert employee.salary == 260000

def test_give_custom_raise():
    employee = Employee('carlos', 'lopez', 255000)
    employee.give_raise(50)
    assert employee.salary == 255050