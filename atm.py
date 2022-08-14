class atm:
    def __init__(self,atm_card_number,pin_number):
        self.atm_card_number= atm_card_number
        self.pin_number= pin_number
        print("atm card number and pin number has been taken")

    def CashWithdrawl(self):
        print("you have withdrawed your cash")

    def BalanceEnquiry (self):
        print("to know balance amount please check app")

    

cash = atm(12345678,3456)
print(cash.atm_card_number)
print(cash.pin_number)
print(cash.CashWithdrawl())
print(cash.BalanceEnquiry())