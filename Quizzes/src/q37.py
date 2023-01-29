class CompoundInterest:
    def __init__(self):
        self.principal, self.rate, self.numyears=0,0,0

    def calculate_interest(self):
        interest=self.principal*(1+self.rate)**self.numyears
        return interest

class AccountingProgram(CompoundInterest):
    def __init__(self):
        self.principal=0
        self.rate=0
        self.numyears=0

    def set_principal(self,principal:int):
        if principal<0:
            raise ValueError("Principal should be greater than zero")
        self.principal=principal

    def set_rate(self,rate:int):
        if rate<0:
            raise ValueError("Interest rate should be greater than zero")
        self.rate=rate

    def set_years(self,years:int):
        if years<0:
            raise ValueError("Years should be greater than zero")
        self.numyears=years

    #def calculate_interest(self):
        #gets the Compound Interest method calculate_interest


