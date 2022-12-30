import unittest
from bank_account import BankAccount, InsufficientFund

class TestBankAccount(unittest.TestCase):
    def setUp(self) -> None:
        # self.account = BankAccount(10)
        return super().setUp()

    def test_balance(self):
        account = BankAccount(10)
        self.assertEqual(account.balance, 10)

    def test_deposit(self):
        account = BankAccount(10)
        account.deposit(5)
        self.assertEqual(account.balance, 15)

    def test_withdraw(self):
        account = BankAccount(10)
        account.withdraw(5)
        self.assertEqual(account.balance, 5)

    def test_deposit_raises_exception(self):
        account = BankAccount(10)
        with self.assertRaises(ValueError): 
            account.deposit(-5)

    def test_withdraw_raises_exception(self):
        account = BankAccount(10)
        with self.assertRaises(ValueError):
            account.withdraw(-15)

    def test_withdraw_raises_exception_with_message(self):
        account = BankAccount(10)
        with self.assertRaises(InsufficientFund) as context:
            account.withdraw(15)
        self.assertEqual(str(context.exception), 'Insufficient fund!')

    def tearDown(self) -> None:
        # self.account = None
        return super().tearDown()