"""This module defines the PartialPaymentStrategy class."""

__author__ = "Nguyen Dang Thai Ha"
__version__ = "10.08.2025"

from .payment_strategy import PaymentStrategy

class PartialPaymentStrategy(PaymentStrategy):
    def process_payment(self, account, payee, amount: float) -> str:
        account.deduct_balance(payee, amount)
        balance = account.get_balance(payee)

        if balance <=0:
            return f"Processed payment of ${amount:.2f}. New balance: ${balance:.2f}."
        else:
            return f"Partial payment of ${amount:.2f} accepted. New balance: ${balance:.2f}."