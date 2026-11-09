# Bank Simulator

This is a simple bank account and ATM simulator made in Python. You can open a new account, edit your information and use an ATM menu to check balance, deposit and withdraw money.

I made this project while learning Python as a BCA 1st year student.

## Features

- Open a new bank account (only for age 18 and above)
- A 5 digit Customer ID and a 10 digit account number are generated automatically
- Edit account information (name, gender, father name, PIN and phone number)
- ATM simulation with PIN login
  - Check balance
  - Deposit money
  - Withdraw money
  - See account details (name, account number, IFSC, balance)
- All account data is saved in a JSON file, so it is not lost when the program closes

## What I Used

- Python
- `json` module to store and read data
- `random` module to make customer ID and account number
- `datetime` module to check age
- Functions, loops, dictionaries and `if`/`else` conditions
- File handling and exception handling (`try`/`except`)

## Project Files

```
bank-simulator/
├── bank_simulator.py             # main program (run this file)
├── create_bank_acount_system.py  # all the functions (registration, edit, ATM)
├── logindetail.json              # account data (created automatically)
└── README.md
```

## How to Run

1. Install Python on your computer.
2. Download both `.py` files and keep them in the same folder.
3. In `create_bank_acount_system.py`, change the file path of `logindetail.json` to a folder on your own computer (I used a path on my E: drive).
4. Open the terminal in the folder and run:

```
python bank_simulator.py
```

## How to Use

When the program starts it asks:

```
Enter [N] for new registration and [O] for editing information and [A] for ATM simulation
```

- **N** - Register a new account. You will get a Customer ID, save it.
- **O** - Edit your information using Customer ID and PIN.
- **A** - ATM simulation. Enter Customer ID and PIN, then choose from the menu:

```
1. Check balance
2. Deposit money
3. Withdraw money
4. Account Detail
5. Exit
```

## Things I Want to Improve

- Add error handling for wrong inputs (like letters instead of numbers)
- Hide the PIN while typing and store it safely
- Add transaction history
- Make the path of the JSON file work on any computer
- Make a GUI version

## Author

Mohammad Unaish
BCA 1st Year, United University
