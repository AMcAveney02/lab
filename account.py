class Account:

    def __init__(self, name: str) -> None:

        '''
        Sets the default state of an account's name & balance.
        :param name: Account's name
        '''

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:

        '''
        This allows the user to deposit money into an account.
        :param amount: The amount sent to desposit into account.
        :return: True only if the deposit can occur, and False if not.
        '''

        if amount > 0:
            self.__account_balance += amount
            return True
        elif amount <= 0:
            return False

    def withdraw(self, amount: float) -> bool:

        '''
        This allows the user to withdraw money from an account.
        :param amount: The amount sent to withdraw from an account.
        :return: True only if the withdrawl can occur, and False if not.
        '''

        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:

        '''
        This retrieves the account balance for the user.
        :return: The account balance.
        '''

        return self.__account_balance

    def get_name(self) -> str:

        '''
        This retreives the name of the account for the user.
        :return: The name of the account.
        '''
        
        return self.__account_name
