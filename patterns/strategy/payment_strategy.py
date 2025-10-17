"""This module defines the PaymentStrategy class."""

__author__ = "Nguyen Dang Thai Ha"
__version__ = "10.08.2025"

from abc import ABC, abstractmethod
from billing_account.billing_account import BillingAccount
from payee.payee import Payee

class PaymentStrategy(ABC):
    """Abstract base class for payment strategies.
    
    Raises: None"""

    @abstractmethod
    def process_payment(self, account: BillingAccount, payee: Payee, amount: float) -> str:
        """Process a payment according to the strategy.
        Args:
            account (BillingAccount): The billing account to process the payment on.
            payee (Payee): The payee for which the payment is being made.
            amount (float): The amount of the payment."""
        pass
