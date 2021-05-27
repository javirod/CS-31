import Employee
def main():
    emp1 = Employee.Employee('Susan Myers', '47899', 'Accounting',\
         'Vice President')
    emp2 = Employee.Employee('Mark Jones', '39119', 'IT', 'Programmer')
    emp3 = Employee.Employee(' ', ' ', ' ', ' ')
    emp3.setName('Joy Rogers')
    emp3.setID('81774')
    emp3.setDept('Manufacturing')
    emp3.setTitle('Engineer')
    print(emp1)
    print(emp2)
    print(emp3)
    changes(emp1)
    print('Updated data for Employee #1:')
    print(emp1)
def changes(emp):
    print('Name:', emp.getName())
    edit = input('Wanna change this? (y/n)')
    if edit == 'y' or edit == 'Y':
        newname = input('Enter new name: ')
        emp.setName(newname)    
    print('ID:', emp.getID())
    edit = input('Wanna change this? (y/n)')
    if edit == 'y' or edit == 'Y':
        newID = input('Enter new ID: ')
        emp.setID(newID)
    print('Dept:', emp.getDept())
    edit = input('Wanna change this? (y/n)')
    if edit == 'y' or edit == 'Y':
        newDept = input('Enter new dept: ')
        emp.setDept(newDept)
    print('Title:', emp.getTitle())
    edit = input('Wanna change this? (y/n)')
    if edit == 'y' or edit == 'Y':
        newTitle = input('Enter new title: ')
        emp.setDept(newTitle)

main()