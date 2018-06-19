class Expenditure:
    def __init__(self, savings, expenditure):
        self.savings = savings
        self.expenditure = expenditure

    def display_expense(self):
        print(self.expenditure)
        print(self.savings)

    def cal_salary(self):
        total = self.savings + self.expenditure
        print("The total salary is", total)


savings = input("Enter savings: ")
expen = input("Enter expenditure: ")
exp = Expenditure(savings, expen)
exp.display_expense()
exp.cal_salary()
