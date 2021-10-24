import re

def validate_account(account):
    account_pattern     = '[a-zA-Z0-9\-]+'
    user_account        = re.match(account_pattern, account)
    ACCOUNT_MIN_LENGTH  = 6
    ACCOUNT_MAX_LENGTH  = 15

    if user_account and ACCOUNT_MIN_LENGTH <= len(account) <= ACCOUNT_MAX_LENGTH:
        return user_account.group()

def validate_password(password):
    password_pattern = '(?=.*[a-zA-Z0-9])(?=.*[0-9!@#\$\%\*\^])(?=.*[a-zA-Z!@#\$\%\*\^]).+'
    user_password    = re.match(password_pattern, password)
    PASSWORD_LENGTH  = 8

    if user_password and len(password) >= PASSWORD_LENGTH:
        return user_password.group()
