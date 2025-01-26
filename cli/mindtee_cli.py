"""
mindtee_cli.py

A simple CLI for demonstrating TEE-based AI and aggregator flows.
"""
import argparse
import logging
import sys

from mind_tee.tee_manager.enclave_manager import EnclaveManager

def main():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    parser = argparse.ArgumentParser(description="Mind TEE CLI - Demonstrate TEE-based tasks.")
    parser.add_argument("--input-data", type=str, default="sensitive_info",
                        help="Data to pass to the TEE AI agent.")
    args = parser.parse_args()

    manager = EnclaveManager()
    result = manager.perform_secure_tasks({"user_data": args.input_data})
    print("TEE Operation Result:", result)

if __name__ == "__main__":
    main()
