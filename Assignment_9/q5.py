class Expenditure:

    def __init__(self, expenditure, savings):
        self.expenditure = expenditure
        self.savings = savings

    def display_expense_savings(self):
        print("Expenditure is: ", self.expenditure)
        print("Savings are: ", self.savings)

    def total_salary(self):
        print("The total salary is", (self.savings + self.expenditure))


expen = int(input("Enter expenditure: "))

savings = int(input("Enter savings: "))

exp = Expenditure(expen, savings)

exp.display_expense_savings()

exp.total_salary()
