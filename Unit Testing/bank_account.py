class InsufficientFund(Exception):
    pass

class BankAccount:
    def __init__(self, balance: float) -> None:
        if balance < 0:
            raise ValueError('Balance cannot be negative!')
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError('Amount cannot be negative!')
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError('Amount cannot be negative!')

        if amount > self._balance:
            raise InsufficientFund('Insufficient fund!')

        self._balance -= amount


