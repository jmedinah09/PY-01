class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last  = last
		self.pay = pay
		self.email = f'{self.first}.{self.last}@company.com' 
		self.fullname = f'{self.first} {self.last}'

DATOS_1 = ['Nombre: ', 'Apellido: ', 'Sueldo: ']
emp     = []
m = int(input('Indique el numero de empleados que desea agregar: '))

for j in range(m):
    DATOS_2 = []
    for i in range(3):
        print(f'Por favor escriba el {DATOS_1[i]}: ')
        dato = input(' -> ')
        if i == 2:
            DATOS_2.append(int(dato))
        else:
            DATOS_2.append(dato)
    emp.append(Employee(DATOS_2[0], DATOS_2[1], DATOS_2[2]))
    
for i in range(m):
    print('-Nombre: ' + emp[i].fullname + ' \t\t-Email: ' + emp[i].email)


#class Student:
#        def __init__(self, rollno, name, age):
#                self.rollno = rollno
#                self.name = name
#                self.age = age
#        def Display(self):
#                print(self.rollno, end = '\t\t')
#                print(self.name, end =  '\t\t')
#                print(self.age)
#st = []
#n  = int(input('Enter no. of students: '))
#print('Students details entry...')
#for i in range(n):
#        print('Students: ', i+1)
#        rollno = input('\tRollno: ')
#        name   = input('\tName: ')
#        age    = int(input('\tAge: '))
#        st.append(Student(rollno, name, age))
#
#for i in range(n):
#    for j in range(i+1,n):
#        if st[i].name > st[j].name:
#            st[i], st[j] = st[j], st[i]
#print('Student Info: ')
#print('Rollno\t\tName\t\tAge')
#for i in range(n):
#        st[i].Display()























        
