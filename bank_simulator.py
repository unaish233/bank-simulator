# Here is the program of the bank simulator

import create_bank_acount_system


create_bank_acount_system.create_login_detail_file()


# account detail of the account holder
choice = input("Enter [N] for new registration and [O] for editing information and [A] for ATM simulation\n>>> ").upper()


if choice == "N":   
     
    create_bank_acount_system.registration_function()
    
elif choice == "O":
    
    create_bank_acount_system.edit_bank_information()
    
elif  choice == "A":
    account = create_bank_acount_system.account_detail()
    account_input = input("Enter the Customer ID: \n>>> ")

    if account_input in account:
        
        pin = int(input("Enter the pin of your account:\n>>> "))
        
        if account[account_input]["Pin"] == pin:

        # loop for running again an again main menu multiple times till the condition become false
            condition = True
            while condition:
                
                create_bank_acount_system.account_detail()
    
                print('''
                    1. Check balance
                    2. Deposit money
                    3. Withdraw money
                    4. Account Detail
                    5. Exit
                    ''')
                choice = int(input("Select the option: "))

                if choice == 1:
                    create_bank_acount_system.check_balance(account_input = account_input, account = account)     #calling the function 

                elif choice == 2:
                    create_bank_acount_system.deposit_money(account_input = account_input, account=account)     #calling the function
                    create_bank_acount_system.write_bank_detail(account)

                    print("Amount deposit successfully")

                elif choice == 3:
                    create_bank_acount_system.withdraw_money(account_input = account_input,account=account)    #calling the function
                    create_bank_acount_system.write_bank_detail(account)
                        
                    print("Amount withdraw successfully")

                elif choice == 4:
                    create_bank_acount_system.check_detail(account_input= account_input, account = account)      #calling the function
                        
                elif choice == 5:
                    condition = False
                    
                else:
                    print("You enter an invalid option")
                
        else:
            print(f"You enter a wrong pin")
            
    else:
        print("Account detail not found❌")

else:
    print("Invalid Input Enter")

print("Thank you! For banking with us.😊")