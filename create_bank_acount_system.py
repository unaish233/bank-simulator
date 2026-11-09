# This is program is used to open a new account which you can access in the bank_simulator after getting your customer id's

import json as js
import random as ran
import datetime as date

# LOGIN DETAIL FILE CREATING TO STORE THE INFORMATION OF THE ACCOUNT HOLDER DETAIL
def create_login_detail_file():
    try:
        with open("E:\\Programs\\python project\\bank account system\\logindetail.json", "xt") as file:
            print("Creating file")
            
    except FileExistsError:
        print("File already exits")

    finally:
        with open("E:\\Programs\\python project\\bank account system\\logindetail.json", "rt") as file:
            file.read()
            # print(file.read())
   
# CREATING THE FUNCTION TO READ TEH INFORMATION FROM THE LOGIN DETAIL JSON FILE 
      
try:
    with open("E:\\Programs\\python project\\bank account system\\logindetail.json", "rt") as file_reads:
        global data
        data = js.load(file_reads)

except Exception:
    data = {}

# FUNCTION FOR WRITING THE EDITED OR NEW ACCOUNT INFORMATION
def write_account_detail():
    with open("E:\\Programs\\python project\\bank account system\\logindetail.json", "w") as accounts_files:
        js.dump(data, accounts_files, indent=4)


# age verification function to verify the age
def age_verification(date_input):
    today_date = date.date.today()
    date_of_birth = date.date.strptime(date_input, "%d/%m/%Y" )
    if date_of_birth.year >= today_date.year:
        print("Invalid date")

    else:
        return today_date.year - date_of_birth.year

# Function for new account creation the user who do not have account
def new_account():
    name = input("Enter the full name: \n>>> ").title()
    father_name = input("Enter Father Name: \n>>> ").title()
    gender_input = input("Enter gender [M/F]: \n>>> ").capitalize()
    if gender_input == "M":
        global gender
        gender = "Male"
        
    else:
        gender = "Female"
    
    phone_number = int(input("Enter you 10 digit Phone number:\n>>> "))
    password_pin = int(input("Enter the pin:\n>>> "))
    balance = int(input("Want to add some balance in your new account:\n>>> "))
    
    # Customer id make by using random function
    global customer_id
    customer_id = ""

    for i in range(1,6):
        customer_id += str(ran.randint(1,9))
        
    # Account number make by using random function 
    account_number = ""

    for i in range(1,11):
        account_number += str(ran.randint(1,10))

    data[customer_id] = {
        "Name" : name,
        "Age" : age,
        "Father Name" : father_name,
        "Pin" : password_pin,
        "Balance" : balance,
        "Phone Number" : phone_number,
        "Account Number" : account_number ,
        "IFSC" : "SBIN001246",
        "Gender" : gender
    }

# Function for registration process
def registration_function():
    global age
    age = age_verification(
        date_input = input("Enter the date of birth:\n>>> ")
        )      # calling the function which for age verification to open bank account
    
    if age >= 18:
        
        new_account()
        write_account_detail()
        print(f"Your customer id number is {customer_id} , You can access your account using this customer id in future")
        print("Account created successfully!")
        
    else:
        print("You are not eligible for opening bank account")

# Function for editing account information for existing user
def edit_bank_information():
    customer_id = input("Enter the customer id:\n>>> ")
    enter_pin = int(input("Enter the Personal Information Number (PIN):\n>>> "))
    
    if enter_pin == data[customer_id]["Pin"]:
        print("""
                1. Name
                2. Gender
                3. Father Name
                4. Pin
                5. Phone Number""")
        
        loop = int(input("How much information do you want to edit:\n>>> "))
        n = 1
        while n <= loop:
            print("""
                    What do you want to edit
                    1. Name
                    2. Gender
                    3. Father Name
                    4. Pin
                    5. Phone Number""")
            edit_choice = input(f"Enter the Serial Number({n} Change):\n>>> ")
            
            if edit_choice == "1":
                
                edit = input("Enter the Name:\n>>> ").title()
                data[customer_id]["Name"] = edit
                write_account_detail()
                
            elif edit_choice =="2":
                
                edit = input("Enter the Gender [M/F]:\n>>> ").capitalize()
                if edit == "M":
                    data[customer_id]["Gender"] = "Male"
                    write_account_detail()
                else:
                    data[customer_id]["Gender"] = "Female"
                    write_account_detail()
            
            elif edit_choice == "3":
                
                edit = input("Enter the Father Name: \n>>> ").title()
                data[customer_id]["Father Name"] = edit
                write_account_detail()
                
            elif edit_choice == "4":
                
                pin = int(input("Enter the pin for verification:\n>>> "))
                if pin == data[customer_id]["Pin"]:
                    edit = int(input("Enter the new pin:\n>>> "))
                    data[customer_id]["Pin"] = edit
                    write_account_detail()

                else:
                    print("You enter a wrong pin. Try again!")
                    
            elif edit_choice == "5":
                
                edit = int(input("Enter the new 10 digit Phone Number: \n>>> "))
                data[customer_id]["Phone Number"] = edit
                write_account_detail()
                
            n += 1
            
        print("Change successfully")
        
    else: 
        print("Enter pin is incorrect.❌")
        

# ATM SIMULATION PROGRAM STATED FROM HERE

# function for account detail reading
def account_detail():
    with open("E:\\Programs\\python project\\bank account system\\logindetail.json" , "rt") as file_detail:
        return js.load(file_detail)
        

def write_bank_detail(account):
    with open("E:\\Programs\\python project\\bank account system\\logindetail.json" , "w") as file_detail:
        js.dump(account, file_detail,indent=4)
    

# function for check detail
def check_detail(account_input,account):
    print('''
          ====================================
                    Bank Detail
          ====================================
          ''')
    print(f"Name: {account[account_input]["Name"]}")
    print(f"Account Number: {account[account_input]["Account Number"]}")
    print(f"IFSC: {account[account_input]["IFSC"]}")
    print(f"Balance : {account[account_input]["Balance"]}")
    

# function for check balance
def check_balance(account_input,account):
    print("======================================")
    print(f" Balance : {account[account_input]["Balance"]}")
    print("======================================")
    

# function for deposit balance
def deposit_money(account_input,account):
    deposit = int(input("Enter the amount: "))
    account[account_input]["Balance"] += deposit
    return


# function for withdraw balance
def withdraw_money(account_input,account):
    print("============================================")
    
    debit = int(input("Enter the amount: "))
    
    if account[account_input]["Balance"] < debit:
        print("Insufficient Balance")
    else:
        account[account_input]["Balance"] -= debit
        return
        
    print("============================================")