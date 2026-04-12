# Step 1
def create_account(owner_name , initial_balance):
    if initial_balance < 0:
        raise ValueError("Initial balance cannot be negative")
    return {
        "owner_name": owner_name,
        "balance": initial_balance
    }

# Step 2
def deposit(account, amount):
    if amount <= 0:
        raise ValueError("Amount is not valid to be deposited")
    account["balance"] += amount
    return account["balance"]

# Step 3
def withdraw(account, amount):
    if amount <= 0:
        raise ValueError("Amount is not valid to be withdrawn")
    if amount > account["balance"]:
        raise ValueError("Amount cannot be greater than account's balance")

    account["balance"] -= amount
    return account["balance"]

# Step 4
def get_balance(account):
    return account["balance"]

# Step 5
def transfer(sender_account , receiver_account, amount):
    if amount <= 0:
        raise ValueError("Amount is not valid to be transferred")

    if amount > sender_account["balance"]:
        raise ValueError("Amount cannot be greater than sender's balance")

    sender_account["balance"] -= amount
    receiver_account["balance"] += amount
    return sender_account["balance"], receiver_account["balance"]






