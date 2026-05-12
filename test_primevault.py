# test_primevault.py
"""
Tests for PrimeVault module.
"""

import unittest
from primevault import PrimeVault

class TestPrimeVault(unittest.TestCase):
    """Test cases for PrimeVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrimeVault()
        self.assertIsInstance(instance, PrimeVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrimeVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
