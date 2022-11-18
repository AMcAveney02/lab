import pytest
from account import *

class Test:
    def setup_method(self):
        self.first_account = Account("001 - Henry Cavill")

    def teardown_method(self):
        del self.first_account

    def test_init(self):
        assert self.first_account.get_name() == "001 - Henry Cavill"
        assert self.first_account.get_balance() == 0

    def test_deposit(self):
        assert self.first_account.deposit(40000) is True
        assert self.first_account.get_balance() == 40000
        assert self.first_account.deposit(-10000) is False
        assert self.first_account.get_balance() == 40000
        assert self.first_account.deposit(0) is False
        assert self.first_account.get_balance() == 40000
        assert self.first_account.deposit(200.7) is True
        assert self.first_account.get_balance() == pytest.approx(40200.7, abs = 0.001)

    def test_withdraw(self):
        assert self.first_account.withdraw(40000) is False
        assert self.first_account.get_balance() == 0
        assert self.first_account.withdraw(-10000) is False
        assert self.first_account.get_balance() == 0
        assert self.first_account.withdraw(0) is False
        assert self.first_account.get_balance() == 0

        self.first_account.deposit(25000)
        assert self.first_account.withdraw(200.5) is True
        assert self.first_account.get_balance() == pytest.approx(24799.5, abs = 0.001)