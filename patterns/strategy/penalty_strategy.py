"""This module defines the PenaltyStrategy class."""

__author__ = "Nguyen Dang Thai Ha"
__version__ = "10.15.2025"

from .payment_strategy import PaymentStrategy

class PennaltyStrategy(PaymentStrategy):
    """Concrete strategy that applies a penalty fee for insufficient payments."""
    def process_payment(self, account, payee, amount: float) -> str:
        account.deduct_balance(payee, amount)
        balance = account.get_balance(payee)

        if balance <= 0:
            return f"Processed payment of ${amount:.2f}. New balance: ${balance:.2f}."
        
        account.add_balance(payee, 10.00)
        balance = account.get_balance(payee)
        return f"Insufficient payment. Added penalty fee of $10.00. New balance: ${balance:.2f}."     