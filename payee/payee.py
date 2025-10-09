"""This module defines the Payee enumeration."""

__author__ = "ACE Faculty"
__version__ = "10.8git.2025"
__credits__ = "Nguyen Dang Thai Ha"

from enum import Enum

class Payee(Enum):
    """Represents the receiver of a payment."""

    ELECTRICITY = 1
    """The electricity payee."""
    
    INTERNET = 2 
    """The internet payee."""
    
    TELEPHONE = 3
    """The telephone payee."""
