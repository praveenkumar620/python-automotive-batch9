class BankAccount:

    def __init__(self, principal, time, age):
        self.principal = principal
        self.time = time
        self.age = age
        self.rate = 8   # 8% interest for senior citizens

    def calculate_ci(self):
        try:
            # Check senior citizen condition
            if self.age < 60:
                print("Interest is applicable only for senior citizens.")
            else:
                # Compound Interest formula
                ci = self.principal + (self.principal * self.rate * self.time) / 100
                print("Compound Interest Amount:", ci)

        except Exception as e:
            print("Invalid input. Please enter correct values.")

# Taking input from user
p = float(input("Enter principal amount: "))
t = float(input("Enter time (in years): "))
a = int(input("Enter age: "))

account = BankAccount(p, t, a)
account.calculate_ci()