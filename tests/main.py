from employee import Employee

active = True

while active:
    print("press q to quit\n")
    first_name = input("First name: ")

    if first_name:
        if first_name == 'q':
            active = False
        else:
            last_name = input("Last name: ")

            if last_name:
                if last_name == 'q':
                    active == False
                else:
                    try:
                        salary = float(input("Enter Salary: "))
                    except ValueError:
                        print("invalid salary")
                        continue
                    else:
                        employee = Employee(first_name, last_name, salary)
                        # print(employee.salary)
            else:
                print("Last name needed!")
                continue
    else:
        print("First name needed!")
        continue


user_data = Employee.all

for data in user_data:
    print(data)