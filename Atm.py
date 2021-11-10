class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin
    def balanceinquiry(self):
        print("Your Balance Is $100")
    def cashwithdrawal(self, amount):
        new_amount = 100-amount
        print("You Withdrawed: " + str(amount) +"Your Remaning Balance Is: " + str(new_amount))
def main():
        name = input("Hello What Is Your Name ?")
        print("Hello, " + name)
        cardnumber = input("Insert Your Card Number: ")
        pin = input("Enter Your Pin: ")
        new_user = Atm(cardnumber, pin)

        print("Choose Your Activity")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        activity = int(input("Enter Activity Choice: "))

        if (activity == 1):
            new_user.balanceinquiry()
        elif (activity == 2):
            amount = int(input("Enter The Amount: "))
            new_user.cashwithdrawal(amount)
        else:
            print("Enter A Valid Number")  

if __name__ == "__main__":
    main()                          