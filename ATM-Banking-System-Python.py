pin = 1234
a = 1000  # Initial Balance

b = int(input("Enter a pin: "))
if pin == b:
    print("valid")
    
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
  
    
    c = int(input("Choose an option (1/2/3): "))

    if c == 1:
        print("Your Balance is:", a)
        
    elif c == 2:
        deposit_amount = int(input("Enter deposit amount: "))
        a = a + deposit_amount
        print("Deposit Successful! New Balance:", a)
        
    elif c == 3:
        withdraw_amount = int(input("Enter withdraw amount: "))
        if withdraw_amount <= a:
            a = a - withdraw_amount
            print("Please collect your cash. Remaining Balance:", a)
        else:
            print("Insufficient Balance!")
            
    else:
        print("Invalid Option Selected")

else:
    print("Invalid pin")
