class InsufficientFundException(Exception):
    def __init__(self, message="Insufficient funds in account."):
        super().__init__(message)

class InvalidAccountException(Exception):
    def __init__(self, message="Invalid account number."):
        super().__init__(message)

class OverDraftLimitExceededException(Exception):
    def __init__(self, message="Overdraft limit exceeded for current account."):
        super().__init__(message)
