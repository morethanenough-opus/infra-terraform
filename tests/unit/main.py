import os
import argparse
import logging
from pathlib import Path
from terraform import Terraform

def configure_logging(log_level):
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )

def parse_args():
    parser = argparse.ArgumentParser(description='Infra-Terraform CLI Tool')
    parser.add_argument('--env', required=True, help='Environment name (e.g., dev, prod)')
    parser.add_argument('--plan', action='store_true', help='Generate Terraform plan')
    parser.add_argument('--apply', action='store_true', help='Apply Terraform changes')
    parser.add_argument('--destroy', action='store_true', help='Destroy Terraform resources')
    parser.add_argument('--log-level', default='INFO', help='Set logging level')
    return parser.parse_args()

def validate_env(env):
    valid_envs = ['dev', 'staging', 'prod']
    if env not in valid_envs:
        raise ValueError(f"Invalid environment '{env}'. Valid options: {valid_envs}")

def main():
    args = parse_args()
    configure_logging(args.log_level.upper())
    logger = logging.getLogger(__name__)

    try:
        validate_env(args.env)
        tf = Terraform(working_dir=Path(f"environments/{args.env}"))

        if args.plan:
            logger.info("Generating Terraform plan...")
            tf.plan()
        elif args.apply:
            logger.info("Applying Terraform changes...")
            tf.apply()
        elif args.destroy:
            logger.info("Destroying Terraform resources...")
            tf.destroy()
        else:
            logger.warning("No action specified. Use --plan, --apply, or --destroy.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()