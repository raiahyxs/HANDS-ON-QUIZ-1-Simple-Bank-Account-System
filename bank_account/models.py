#Part 1

from django.db import models

class Account(models.Model):
    #Model Fields
    name = models.CharField(max_length=100)
    _balance = models.FloatField(default=0.0) #Protected Attribute

    #1. Instance Method
    def display_info(self):
        return f"Account of {self.name} has a balance of ${self._balance}"
    
    #2. Behavior Method
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.save()
            return f"Deposited ${amount}. New balance is ${self._balance}"
        else:
            return "Deposit amount must be greater than 0."
        
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            self.save()
            return f"Withdrew ${amount}. New balance is ${self._balance}"
        else:
            return "Invalid withdrawal amount. Check amount or insufficient balance."
        
    #3. Getter and Setter
    def get_balance(self):
        return self._balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
            self.save()
            return f"Balance set to ${self._balance}"
        else:
            return "Balance cannot be negative."