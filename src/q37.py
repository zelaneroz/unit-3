class CompoundInterest:
    def __init__(self,principal,rate,years):
        self.interest=principal*(1+rate)**years

class AccountingProgram:
    def __init__(self):
        self.principal=0
        self.rate=0
        self.years=0

    def set_principal(self,principal):
        self.principal=principal
        return f"Principal value set to {self.principal}"

    def set_rate(self,rate):
        self.rate=rate
        return f"Rate set to {self.rate}"

    def set_years(self,years):
        self.years=years
        return f"Number of years set to {self.years}"

    def calculate_interest(self):
        self.interest=CompoundInterest(self.principal,self.rate,self.years).interest
        return f"Calculated interest is {self.interest}"


obj2=AccountingProgram()
print(obj2.set_principal(7))
print(obj2.set_years(3))
print(obj2.set_rate(4))
print(obj2.calculate_interest())