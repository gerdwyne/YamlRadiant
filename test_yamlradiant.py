# test_yamlradiant.py
"""
Tests for YamlRadiant module.
"""

import unittest
from yamlradiant import YamlRadiant

class TestYamlRadiant(unittest.TestCase):
    """Test cases for YamlRadiant class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = YamlRadiant()
        self.assertIsInstance(instance, YamlRadiant)
        
    def test_run_method(self):
        """Test the run method."""
        instance = YamlRadiant()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
