"""This module defines the Payment class."""

__author__ = "Nguyen Dang Thai Ha"
__version__ = "10.15.2025"

from billing_account.billing_account import BillingAccount
from patterns.strategy.payment_strategy import PaymentStrategy
from payee.payee import Payee

class Payment:
    """Handles payment processing using a specified strategy.
    
        Raises: None
    """
    def __init__(self, strategy):
        """Initializes a Payment instance with a given strategy.
        Args:
            strategy (PaymentStrategy): The payment strategy to use.
        """
        if isinstance(strategy, PaymentStrategy):
            self.__strategy = strategy
        else:
            raise ValueError("Invalid Strategy")
    def pay_bill(self, account: BillingAccount, payee: Payee, amount: float) -> str:
        """Processes a payment using the selected strategy.
        Args:
            account (BillingAccount): The billing account to process the payment on.
            payee (Payee): The payee for which the payment is being made.
            amount (float): The amount of the payment."""
        return self.__strategy.process_payment(account, payee, amount)
    