class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance  # Приватное поле для хранения текущего баланса
        self._transactions = []  # Логируем каждую операцию здесь

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной!")

        self._balance += amount
        self._log_transaction(f"Внесено: +{amount:.2f}")  # Запись операции в журнал

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счете!")

        if amount <= 0:
            raise ValueError("Сумма должна быть положительной!")

        self._balance -= amount
        self._log_transaction(f"Снято: -{amount:.2f}")  # Запись операции в журнал

    @property
    def balance(self):
        return self._balance

    def show_transactions(self):
        for transaction in self._transactions:
            print(transaction)

    def _log_transaction(self, message):
        self._transactions.append(message)


# Примеры использования:
account = BankAccount(initial_balance=1000)

try:
    account.deposit(500)
    account.withdraw(800)
except ValueError as e:
    print(e)

print("Баланс:", account.balance)
account.show_transactions()