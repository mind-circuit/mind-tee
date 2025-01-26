"""
enclave_manager.py

Illustrates a manager that controls TEE enclaves, bridging AI and aggregator functionality.
"""

import logging
from mind_tee.tee_ai.secure_agent import SecureAIAgent
from mind_tee.tee_aggregator.secure_aggregator import SecureAggregator

logger = logging.getLogger(__name__)

class EnclaveManager:
    """
    Coordinates TEE-based AI and aggregator components, simulating
    how sensitive tasks might be assigned and executed within enclaves.
    """

    def __init__(self):
        logger.info("EnclaveManager initialized")
        self.ai_agent = SecureAIAgent(agent_id="EnclaveAI")
        self.aggregator = SecureAggregator(aggregator_id="EnclaveAggregator")

    def perform_secure_tasks(self, data_input: dict) -> dict:
        """
        Runs a confidential AI inference, then aggregates the result
        inside the TEE environment.
        """
        logger.info("Performing secure tasks in TEE environment")

        # 1) Secure AI inference
        inference_output = self.ai_agent.private_inference(data_input)

        # 2) Aggregation (with multiple data fragments, for demonstration)
        aggregator_input = [data_input, inference_output]
        aggregated_output = self.aggregator.aggregate(aggregator_input)

        combined_result = {
            "inference_output": inference_output,
            "aggregated_output": aggregated_output,
            "notes": "All tasks performed in TEE enclaves"
        }
        logger.debug(f"Combined TEE result: {combined_result}")
        return combined_result
