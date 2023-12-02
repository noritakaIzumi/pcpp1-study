import unittest
from typing import Optional

from support.logger import ILogger, get_default_logger, ArrayLogger


class AccountException(Exception):
    pass


class BankAccount:
    def __init__(self, number: int, balance: float, *, logger: Optional[ILogger] = None) -> None:
        self.__number = number
        self.__balance = balance
        self.__logger = logger or get_default_logger()

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, value: int) -> None:
        raise AccountException('you cannot change the account number')

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float) -> None:
        if value < 0:
            raise AccountException('you cannot set a negative balance')

    def deposit(self, amount: float) -> None:
        if amount >= 100.000:
            self.__logger.log('bank operation above 100.000 is occurred')
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount >= 100.000:
            self.__logger.log('bank operation above 100.000 is occurred')
        self.balance -= amount

    @balance.deleter
    def balance(self) -> None:
        if self.balance != 0:
            raise AccountException('you cannot delete an account as long as the balance is not zero')


class TestBankAccount(unittest.TestCase):
    def setUp(self) -> None:
        self.logger = ArrayLogger()

    def test(self) -> None:
        bank_account = BankAccount(1, 1000, logger=self.logger)
        self.assertEqual(1000, bank_account.balance)

        with self.assertRaises(AccountException):
            bank_account.balance = -200

        with self.assertRaises(AccountException):
            bank_account.number = 2

        bank_account.deposit(1_000.000)
        self.assertEqual(self.logger.buffer[-1], 'bank operation above 100.000 is occurred')

        with self.assertRaises(AccountException):
            del bank_account.balance


if __name__ == '__main__':
    unittest.main()
