class Account:
    def __init__(self):
        self.balance=0
        self.holder_name=""
        self.holder_email=""
        self.number=[]

    # def get_account_no(self)->str:

    def set_holder_name(self,name:str)->str:
        if not isinstance(name,str):
            raise ValueError("Error. Input must be a string.")
        self.holder_name=name
        return f"Holder's name set to {self.holder_name}"

    def set_holder_email(self,email:str)->str:
        self.holder_email=email
        return f"Holder's email set to {self.holder_email}"

    def get_balance(self)->int:
        return self.balance

    def deposit(self,amount:int)->str:
        self.balance+=amount
        return f"New balance: {self.balance} USD"

# case1 = Account()
# solution = case1.set_holder_name(["zelan@gmail.com"])
# print(solution)
