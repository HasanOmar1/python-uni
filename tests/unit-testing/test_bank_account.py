import unittest
import bank_account

# Task A
class TestCreateAccount(unittest.TestCase):
    def test_positive_balance_account(self):
        account = bank_account.create_account("Falafel" , 400)
        self.assertEqual(account["balance"],400)

    def test_zero_balance_account(self):
        account = bank_account.create_account("Falafel", 0)
        self.assertEqual(account["balance"], 0)

    def test_negative_balance_account(self):
        with self.assertRaises(ValueError):
            bank_account.create_account("Falafel", -15)

    def test_correct_owner_name(self):
        account = bank_account.create_account("Falafel" , 200)
        self.assertEqual(account["owner_name"], "Falafel")


# Task B
class TestDepositFunction(unittest.TestCase):
    def test_deposit_valid_amount(self):
        account = bank_account.create_account("Shawarma" , 400)
        new_balance = bank_account.deposit(account , 100)
        self.assertEqual(new_balance, 500)


    def test_deposit_more_than_once(self):
        account = bank_account.create_account("Shawarma" , 400)
        new_balance = bank_account.deposit(account , 100)
        new_balance = bank_account.deposit(account , 100)
        self.assertEqual(new_balance, 600)

    def test_deposit_zero(self):
        account = bank_account.create_account("Shawarma", 400)
        with self.assertRaises(ValueError):
            bank_account.deposit(account, 0)

    def test_deposit_negative(self):
        account = bank_account.create_account("Shawarma", 400)
        with self.assertRaises(ValueError):
            bank_account.deposit(account, -10)

    # Extra 1
    def test_deposit_very_large_amount(self):
        account = bank_account.create_account("Shawarma", 400)
        new_balance = bank_account.deposit(account, 10000)
        self.assertEqual(new_balance, 10400)

    # Extra 4
    def test_deposit_floating_point_value(self):
        account = bank_account.create_account("Medium Well Steak" , 400)
        new_balance = bank_account.deposit(account , 5.5)
        self.assertEqual(new_balance, 405.5)


# Task C
class TestWithdrawFunction(unittest.TestCase):
    def test_withdraw_valid_amount(self):
        account = bank_account.create_account("Pizza", 300)
        updated_balance = bank_account.withdraw(account , 100)
        self.assertEqual(updated_balance, 200)

    def test_withdraw_all_balance(self):
        account = bank_account.create_account("Pizza", 300)
        updated_balance = bank_account.withdraw(account, 300)
        self.assertEqual(updated_balance, 0)

    def test_withdraw_more_than_balance(self):
        account = bank_account.create_account("Pizza", 300)
        with self.assertRaises(ValueError):
            bank_account.withdraw(account, 500)

    def test_withdraw_zero_balance(self):
        account = bank_account.create_account("Pizza", 300)
        with self.assertRaises(ValueError):
            bank_account.withdraw(account, 0)

    def test_withdraw_negative_balance(self):
        account = bank_account.create_account("Pizza", 300)
        with self.assertRaises(ValueError):
            bank_account.withdraw(account, -201294)

    # Extra 2
    def test_withdraw_repeated(self):
        account = bank_account.create_account("Pizza", 300)
        updated_balance = bank_account.withdraw(account , 100)
        updated_balance = bank_account.withdraw(account , 100)
        updated_balance = bank_account.withdraw(account , 100)
        self.assertEqual(updated_balance, 0)


# Task D
class TestGetBalanceFunction(unittest.TestCase):
    def test_balance_after_creation(self):
        account = bank_account.create_account("Tacos", 77)
        current_balance = bank_account.get_balance(account)
        self.assertEqual(current_balance, 77)

    def test_balance_after_deposit(self):
        account = bank_account.create_account("Tacos", 77)
        updated_balance = bank_account.deposit(account,3)
        self.assertEqual(updated_balance, 80)

    def test_balance_after_withdraw(self):
        account = bank_account.create_account("Tacos", 77)
        updated_balance = bank_account.withdraw(account,50)
        self.assertEqual(updated_balance, 27)


# Task E
class TestTransferFunction(unittest.TestCase):
    def test_transfer_valid_amount(self):
        account_one = bank_account.create_account("Burger", 85)
        account_two = bank_account.create_account("Sushi", 68)
        new_balance_one , new_balance_two = bank_account.transfer(account_one, account_two, 2)
        self.assertEqual(new_balance_two, 70)

    def test_balance_after_transfer(self):
        account_one = bank_account.create_account("Burger", 85)
        account_two = bank_account.create_account("Sushi", 68)
        new_balance_one, new_balance_two = bank_account.transfer(account_one, account_two, 2)
        self.assertEqual(new_balance_one, 83)
        self.assertEqual(new_balance_two, 70)

    def test_transfer_zero_balance(self):
        account_one = bank_account.create_account("Burger", 85)
        account_two = bank_account.create_account("Sushi", 68)
        with self.assertRaises(ValueError):
            bank_account.transfer(account_one, account_two, 0)

    def test_transfer_more_than_sender_balance(self):
        account_one = bank_account.create_account("Burger", 85)
        account_two = bank_account.create_account("Sushi", 68)
        with self.assertRaises(ValueError):
            bank_account.transfer(account_one, account_two, 100)

    def test_transfer_negative_amount(self):
        account_one = bank_account.create_account("Burger", 85)
        account_two = bank_account.create_account("Sushi", 68)
        with self.assertRaises(ValueError):
            bank_account.transfer(account_one, account_two, -128)

    # Extra 3
    def test_transfer_repeated(self):
        account_one = bank_account.create_account("Burger", 85)
        account_two = bank_account.create_account("Sushi", 68)
        new_balance_one , new_balance_two = bank_account.transfer(account_one, account_two, 2)
        new_balance_one , new_balance_two = bank_account.transfer(account_one, account_two, 3)
        new_balance_one , new_balance_two = bank_account.transfer(account_one, account_two, 10)
        self.assertEqual(new_balance_one, 70)
        self.assertEqual(new_balance_two, 83)


    # Extra 5
    def test_transfer_error_no_change(self):
            account_one = bank_account.create_account("Potato", 500)
            account_two = bank_account.create_account("Sweet Potato", 0)
            with self.assertRaises(ValueError):
                bank_account.transfer(account_one, account_two, -10)

            self.assertEqual(account_one["balance"], 500)
            self.assertEqual(account_two["balance"], 0)
