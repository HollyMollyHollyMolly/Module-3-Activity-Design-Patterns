"""This module defines the PenaltyStrategy class."""

__author__ = "Nguyen Dang Thai Ha"
__version__ = "10.15.2025"

from .payment_strategy import PaymentStrategy

class PenaltyStrategy(PaymentStrategy):
    """Concrete strategy that applies a penalty fee for insufficient payments.
    
        Raises: None
    """
    def process_payment(self, account, payee, amount: float) -> str:
        """Apply the amount paid to the payee with Penalty payment strategy.
        Args:
            account: Account object
            payee(Enum): Type of payee
            amount(float): The amount of payment"""
        account.deduct_balance(payee, amount)
        balance = account.get_balance(payee)

        if balance <= 0:
            return f"Processed payment of ${amount:.2f}. New balance: ${balance:.2f}."
        
        account.add_balance(payee, 10.00)
        balance = account.get_balance(payee)
        return f"Insufficient payment. Added penalty fee of $10.00. New balance: ${balance:.2f}."     