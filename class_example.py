class Employee:
    def __init__(self,name,salary,company):
        self.name =name
        self.salary =salary
        self.company =company
    def show_stats(self):
        print(self.name,self.salary,self.company)

class Electrical_Employee(Employee):
    def __init__(self,name,salary,company,dep):
        super().__init__(name,salary,company)
        self.department =dep

if __name__ == "__main__":
    john = Electrical_Employee("John",2000,"JJ",'EE')
    john.show_stats()
    print(john.department)


