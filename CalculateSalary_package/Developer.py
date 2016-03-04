from CalculateSalary_package.Employee import Employee


class Developer(Employee):
    def __init__(self, firstName, surName, yearsWorked, program_lang):
        self.program_lang = program_lang
        super(Developer, self).__init__(firstName, surName, yearsWorked)

    def developerDetails(self):
        return super(Developer,
                     self).CalculateSalary() + "\n" + "And the %s favourites programming language is %s  " % self.program_lang
