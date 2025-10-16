"""This module defines the PaymentStrategy class."""

__author__ = "Nguyen Dang Thai Ha"
__version__ = "10.08.2025"

from abc import ABC, abstractmethod
from billing_account.billing_account import BillingAccount
from payee.payee import Payee

class PaymentStrategy(ABC):
    """Abstract base class for payment strategies."""

    @abstractmethod
    def process_payment(self, account: BillingAccount, payee: Payee, amount: float) -> str:
        pass
