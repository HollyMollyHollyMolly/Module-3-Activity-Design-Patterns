"""This module defines the PartialPaymentStrategy class."""
 
__author__ = "Nguyen Dang Thai Ha"
__version__ = "10.08.2025"
 
from .payment_strategy import PaymentStrategy
 
class PartialPaymentStrategy(PaymentStrategy):
    """
    Initialize a PartialPaymentStrategy instance.
 
    Raises: None
    """
    def process_payment(self, account, payee, amount: float) -> str:
        """Apply the amount paid to the payee with Partial payment strategy.
       
        Args:
            account: Account object
            payee(Enum): Type of payee
            amount(float): The amount of payment
           
        Returns:
            str: A string with anoucement when use process_payment of partial payment strategy
        """
        account.deduct_balance(payee, amount)
        balance = account.get_balance(payee)
 
        if balance <=0:
            return f"Processed payment of ${amount:.2f}. New balance: ${balance:.2f}."
        else:
            return f"Partial payment of ${amount:.2f} accepted. New balance: ${balance:.2f}."