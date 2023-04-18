class Bank:
    customers = []
    
    def register(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        account_number = len(Bank.customers) + 1
        
        customer = Customer(name, email, password, account_number)
        Bank.customers.append(customer)
        
        print("Registration Successful!")
        print(f"Your account number is {account_number}")
        print("Please login to continue!")
    
    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        
        for customer in Bank.customers:
            if customer.email == email and customer.password == password:
                print("Login Successful!")
                self.customer = customer
                break
        else:
            print("Invalid credentials!")
            return False
        
        return True
    
    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        self.customer.balance += amount
        print("Deposit Successful!")
    
    def withdraw(self):
        amount = int(input("Enter the amount to withdraw: "))
        if self.customer.balance < amount:
            print("Insufficient balance!")
            return
        
        self.customer.balance -= amount
        print("Withdrawal Successful!")
    
    def balance(self):
        print(f"Your account balance is {self.customer.balance}")
        

class Customer:
    def __init__(self, name, email, password, account_number):
        self.name = name
        self.email = email
        self.password = password
        self.account_number = account_number
        self.balance = 0

bank = Bank()

while True:
    print("\nBank System:")
    print("1. Register")
    print("2. Login")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Balance")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        bank.register()
    
    elif choice == "2":
        if bank.login():
            print(f"Welcome {bank.customer.name}!")
    
    elif choice == "3":
        if not hasattr(bank, "customer"):
            print("Please login first!")
            continue
        bank.deposit()
        
    elif choice == "4":
        if not hasattr(bank, "customer"):
            print("Please login first!")
            continue
        bank.withdraw()
        
    elif choice == "5":
        if not hasattr(bank, "customer"):
            print("Please login first!")
            continue
        bank.balance()
    
    elif choice == "6":
        print("Thank you for using Bank System!")
        break
        
    else:
        print("Invalid choice!")
