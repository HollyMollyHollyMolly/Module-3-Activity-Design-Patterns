"""This module defines the PaymentStrategy class."""

__author__ = "Nguyen Dang Thai Ha"
__version__ = "10.08.2025"

from abc import ABC, abstractmethod
from payee.payee import Payee

class PaymentStrategy(ABC):
    """Abstract base class for payment strategies."""

    @abstractmethod
    def pay(self, amount: float, payee: Payee) -> None:
        """Process a payment of the specified amount to the given payee."""
        pass
