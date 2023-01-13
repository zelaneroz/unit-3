class Account:
    def __init__(self,balance:int,holder_name:str,holder_email:str,number:list):
        self.balance=balance
        self.holder_name=holder_name
        self.holder_email=holder_email
        self.number=number
    def get_account_no(self)->str:

    def set_holder_name(self)->str:
        #When called, the attribute name must be filled
        #Then return string f"Holder's name set to {name}"
        #If holder_name is a list???? Value Error
        #If holder name is not a string, Type Error
    def set_holder_email(selfs)->str:
        # When called, the attribute email must be filled
        # Then return string f"Holder's email set to {email}"
    def get_balance(self)->int:
        #return self.balance

    def deposit(self)->str:
        #Add number to self.balance.
        #Output f"New balance: {balance} USD"



