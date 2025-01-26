"""
test_tee.py

Basic unit tests for the TEE-based AI and aggregator.
"""

import unittest
from mind_tee.tee_manager.enclave_manager import EnclaveManager

class TestTEEIntegration(unittest.TestCase):
    def setUp(self):
        self.manager = EnclaveManager()

    def test_perform_secure_tasks(self):
        data_input = {"test_key": "test_value"}
        result = self.manager.perform_secure_tasks(data_input)
        self.assertIn("inference_output", result)
        self.assertIn("aggregated_output", result)

if __name__ == "__main__":
    unittest.main()
