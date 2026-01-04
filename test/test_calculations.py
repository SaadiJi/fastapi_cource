import pytest
from app.calculations import add, subtract, multiply, deivide, BankAccount


@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)


# @pytest.mark.parametrize("num1, num2, expected", [
#     (3,2,5),
#     (7,8,15),
#     (12,4,16)
# ]) 
# def test_add(num1,num2,expected):
#     assert add(num1,num2) == expected
    
# def test_subtract():
#     assert subtract(6,3) == 3
    
# def test_multiply():
#     assert multiply(6,3) == 18
    
# def test_divide():
#     assert deivide(6,3) == 2
    
    
    
# def test_bank_set_initial_amount(bank_account):
#     #bank_account = BankAccount(50)
#     assert bank_account.balance == 50
    
# def test_bank_default_amount(zero_bank_account):
#     # bank_account = BankAccount()
#     assert zero_bank_account.balance ==0
    
# def test_withdraw():
#     bank_account = BankAccount(50)
#     bank_account.withdraw(20)
#     assert bank_account.balance == 30


@pytest.mark.parametrize("deposited, withdraw, expected", [
    (200,100,100),
    (10.5,1.5,9.0),
    (14.48,4.48,10.00)
]) 
def test_bank_transaction(zero_bank_account,deposited,withdraw,expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.balance == expected
    