#static method 
print("static method=Used to define a method that does not operate on an instance or class.")
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")
MyClass.static_method()

print()
print("class method= Used to define a method that operates on the class itself rather than on instances.")
class MyClass:
    count = 0
    @classmethod
    def increment_count(cls):
        cls.count += 1
MyClass.increment_count()
print(MyClass.count)

print()
print("property method=Used to define a method as a property, allowing it to be accessed like an attribute.")
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

obj = MyClass(10)
print(obj.value)

print()


# django transaction decorator 
# from django.db import transaction
# from django.db import models

# class Account(models.Model):
#     balance = models.DecimalField(max_digits=10, decimal_places=2)

# def transfer_money(from_account, to_account, amount):
#     if from_account.balance < amount:
#         raise ValueError("Insufficient funds")
#     from_account.balance -= amount
#     to_account.balance += amount
#     from_account.save()
#     to_account.save()

# @transaction.atomic
# def perform_transaction(from_account_id, to_account_id, amount):
#     from_account = Account.objects.get(id=from_account_id)
#     to_account = Account.objects.get(id=to_account_id)
#     transfer_money(from_account, to_account, amount)
