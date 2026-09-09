"""
Data model:

client:
    name
    email_address
    bank_accounts

account:
    id
    overdraft # cât poate să extragă pe minus
    balance

transaction:
    account_id
    type
    amount

"""

"""
Exercițiul:

1. o clasă BankAccount, cu atributele:
   id, overdraft, balance

2. implementați metodele withdraw() și deposit()
   (adică transaction type: debit respectiv credit)

3. o clasă Client cu atributele:
    name, email, accounts

4. încărcăm clients.json și populăm (creăm) atât
   clienții cât și conturile

Atenție: avem nevoie de o legătură de la fiecare client la conturile sale


===
x. (mai târziu) o facilitate de alertă
   dacă un withdrawal ar trece peste overdraft

y. procesăm transactions.csv


Facilități:

să am un obiect AccountCollection, în care să fac lookup după id-ul contului

"""

import csv
import json


class OverdraftError(ValueError):
    pass


class Client:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def __repr__(self):
        return f"Client(name={self.name!r}, email={self.email!r}, accounts={self.accounts!r}"


class BankAccount:
    def __init__(self, id, overdraft=0):
        self.id = id
        self.overdraft = overdraft
        self.balance = 0

    def __repr__(self):
        # vreau să găsesc toate atributele care nu sunt metodă
        # ale obiectului, după nume, și valoarea lor
        return 'BankAccount(%s)' % ", ".join(
            f"{attr}={getattr(self, attr)!r}" for attr in self.__dict__
        )

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft:
            raise OverdraftError("Amount withdrawal exceeds overdraft")
        else:
            self.balance -= amount

# vrem ca atunci când facem setattr pe balance,
# să treacă prin logica de OverdraftError protection:

# v.1: folosim @property pt. a implementa getter/setter,
#      backed by a "hidden" attribute.

class BankAccount:
    def __init__(self, id, client, overdraft=0):
        self.id = id
        self.client = client
        self.overdraft = overdraft
        self.__balance = 0

    def __repr__(self):
        # vreau să găsesc toate atributele care nu sunt metodă
        # ale obiectului, după nume, și valoarea lor
        return 'BankAccount(%s)' % ", ".join(
            f"{attr}={getattr(self, attr)!r}"
            for attr in self.__dict__
            if not attr.startswith('_')
        )

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < -self.overdraft:
            raise OverdraftError("Amount withdrawal exceeds overdraft")
        else:
            self.__balance = value

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


# v.2: interceptăm low-level getattr și setattr

class BankAccount:
    def __new__(cls, id, *args, **kwargs):
        obj = super().__new__(cls)

        # we captured the id here
        obj.id = id
        # so that it's already available
        # when appending to the collection
        AccountCollection().append(obj)

        return obj

    def __init__(self, id, client, overdraft=0):
        # nu mai facem nimic cu id-ul, că l-am setat în __new__
        #self.id = id
        self.client = client
        self.overdraft = overdraft
        self.__balance = 0

    def __repr__(self):
        return f'BankAccount(id={self.id}, client={self.client.name!r}, balance={self.balance}, overdraft={self.overdraft})'

    def __getattr__(self, name):
        match name:
            case "balance":
                return self.__balance
            # case... case... etc.
            case _:
                raise AttributeError(f"{self} has no attribute '{name}'")

    def __setattr__(self, name, value):
        if name != "balance":
            super().__setattr__(name, value)
            return

        if value < -self.overdraft:
            raise OverdraftError("Amount withdrawal exceeds overdraft")
        else:
            self.__balance = value

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


# Cerință:
# să avem un obiect cu data type AccountCollection
# care să fie singleton.
#
# și la fiecare creare de account,
# acesta să fie introdus în colecție.
#
# și să avem item access după id:
# AccountCollection()[55] --> Account
#
# și să iterăm în acest obiect după Account-uri

class AccountCollection:
    __single_object = None
    __accounts = {}

    # atenție. __new__ este un staticmethod!
    # (automat, conform specificației)
    def __new__(cls, *args, **kwargs):
        if not cls.__single_object:
            cls.__single_object = super().__new__(cls)

        return cls.__single_object

    def append(self, account):
        self.__accounts[account.id] = account

    def __getitem__(self, key):
        return self.__accounts[key]

    def __iter__(self):
        return iter(self.__accounts.values())


# în loc să scriem un class Transaction,
# folosim un namedtuple
from collections import namedtuple

Transaction = namedtuple('Transaction', ('id', 'type', 'amount'))

# sau, alternativ, versiunea nouă:

from typing import NamedTuple

class Transaction(NamedTuple):
    id: int
    type: str
    amount: int

# sau, alternativ, altă versiune:
# (cu writable attributes)

from dataclasses import dataclass

@dataclass
class Transaction:
    id: int
    type: str
    amount: int

############
# procesăm #
############

def main():
    CLIENTS_JSON = "data/clients.json"
    TRABSACTIONS_CSV = "data/transactions.csv"

    with open(CLIENTS_JSON) as f:
        data = json.load(f)

        for elem in data:
            client = Client(
                name=elem['name'],
                email=elem['email_address'],
            )

            for acc in elem['bank_accounts']:
                # creăm conturile
                account = BankAccount(
                    id=acc['id'],
                    client=client,
                    overdraft=acc['overdraft']
                )
                # le asociem clientului

                client.accounts.append(account)

    with open(TRABSACTIONS_CSV) as f:
        reader = csv.DictReader(f)

        accounts = AccountCollection()

        for row in reader:
            transaction = Transaction(
                id=int(row['account_id']),
                type=row['transaction_type'],
                amount=float(row['amount'])
            )

            # găsim contul cu acest transaction.id
            account = accounts[transaction.id]

            # și operăm tranzacția

            # așa ar face ar face un om normal
            """
            if transaction.type == "debit":
                account.withdraw(transaction.amount)

            elif transaction.type == "credit":
                account.deposit(transaction.amount)

            else:
                raise Exception("Bad transaction type")
            """

            # așa ar face cineva care vrea ca nimeni
            # din echipă să-i înțeleagă codul
            ACCOUNT_METHODS = {
                "debit": "withdraw",
                "credit": "deposit"
            }

            mname = ACCOUNT_METHODS[transaction.type]
            method = getattr(account, mname)

            method(transaction.amount)


# strategie de a face un modul
# care este în acel timp "un library"
# și un executabil main-level.
#
# având grijă ca atunci când se face
# from module import stuff
#
# să nu se execute main-level code.
if __name__ == "__main__":
    print("» sunt main")
    main()
    print("» am rulat fără output")
