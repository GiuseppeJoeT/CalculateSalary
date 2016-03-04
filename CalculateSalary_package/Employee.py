class Employee():
    baseSalary = 5000

    def __init__(self, firstName, surName, yearsWorked):
        self.firstName = firstName
        self.surName = surName
        self.yearsWorked = yearsWorked

    def calculateSalary(self):
        if (self.yearsWorked < 3):
            self.baseSalary = self.baseSalary + (self.baseSalary * 0.1)
            return "The employee salary is %s" % (self.baseSalary)

        elif (self.yearsWorked <= 5):
              self.baseSalary = self.baseSalary + (self.baseSalary * 0.2)
              return "The employee salary is %s" % (self.baseSalary)

        elif (self.yearsWorked > 5):
              self.baseSalary = self.baseSalary + (self.baseSalary * 0.25)
              return "The employee salary is %s" % (self.baseSalary)




