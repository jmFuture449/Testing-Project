import pytest

from bank_account import BankAccount


def test_new_account_has_zero_balance():
	account = BankAccount("Alice")
	assert account.balance() == 0


def test_deposit_increases_balance():
	account = BankAccount("Alice")
	account.deposit(100)
	assert account.balance() == 100


def test_withdrawal_decreases_balance():
	account = BankAccount("Alice")
	account.deposit(100)
	account.withdraw(40)
	assert account.balance() == 60


@pytest.mark.parametrize("amount", [-1, 0])
def test_negative_or_zero_deposit_is_rejected(amount):
	account = BankAccount("Alice")
	with pytest.raises(ValueError):
		account.deposit(amount)


@pytest.mark.parametrize("amount", [-1, 0])
def test_negative_or_zero_withdrawal_is_rejected(amount):
	account = BankAccount("Alice")
	with pytest.raises(ValueError):
		account.withdraw(amount)


def test_withdrawal_over_current_balance_is_rejected():
	account = BankAccount("Alice")
	account.deposit(50)
	with pytest.raises(ValueError):
		account.withdraw(51)
	assert account.balance() == 50
