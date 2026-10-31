pin = 1234
a = 1000  # Initial Balance

# Step 1: PIN Verification
b = int(input("Enter a pin: "))
if pin == b:
    print("valid")
    
    # Step 2: Menu Options
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
  
    
    # Step 3: Taking Option Input
    c = int(input("Choose an option (1/2/3): "))
    
    # Step 4: if-elif-else conditions for operations
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