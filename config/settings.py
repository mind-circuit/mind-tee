"""
settings.py

Example placeholders for environment variables (e.g. TEE driver paths).
"""

import os
import logging

logger = logging.getLogger(__name__)

TEE_MODE = os.getenv("TEE_MODE", "Simulated")  # e.g. "Intel_SGX", "AMD_SEV"
TEE_DRIVER_PATH = os.getenv("TEE_DRIVER_PATH", "/dev/sgx_enclave")

logger.info(f"TEE_MODE={TEE_MODE}, TEE_DRIVER_PATH={TEE_DRIVER_PATH}")
