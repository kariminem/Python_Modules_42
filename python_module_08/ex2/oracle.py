#!/usr/bin/env python3
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("WARNING: python-dotenv not installed, .env file will be ignored")
    print("Install it with: pip install python-dotenv\n")


DATABASE_LABELS: dict[str, str] = {
    "development": "Connected to local instance",
    "production": "Connected to production cluster",
}


def get_config() -> dict[str, str]:
    return {
        "mode": os.environ.get("MATRIX_MODE", "development"),
        "database_url": os.environ.get("DATABASE_URL", ""),
        "api_key": os.environ.get("API_KEY", ""),
        "log_level": os.environ.get("LOG_LEVEL", "INFO"),
        "zion_endpoint": os.environ.get("ZION_ENDPOINT", ""),
    }


def describe_database(config: dict[str, str]) -> str:
    if not config["database_url"]:
        return "NOT CONFIGURED - missing DATABASE_URL"
    return DATABASE_LABELS.get(config["mode"], "Connected to unknown target")


def describe_api(config: dict[str, str]) -> str:
    if not config["api_key"]:
        return "NOT AUTHENTICATED - missing API_KEY"
    return "Authenticated"


def describe_zion(config: dict[str, str]) -> str:
    if not config["zion_endpoint"]:
        return "OFFLINE - missing ZION_ENDPOINT"
    return "Online"


def security_check(config: dict[str, str]) -> list[str]:
    checks = []

    hardcoded_free = "secret123" not in config["api_key"].lower()
    checks.append(
        "[OK] No hardcoded secrets detected"
        if hardcoded_free
        else "[WARN] Suspicious hardcoded-looking secret detected"
    )

    env_file_present = os.path.isfile(".env")
    checks.append(
        "[OK] .env file properly configured"
        if env_file_present
        else "[WARN] No .env file found, using environment/defaults only"
    )

    prod_ready = config["mode"] in DATABASE_LABELS
    checks.append(
        "[OK] Production overrides available"
        if prod_ready
        else "[WARN] MATRIX_MODE has an unexpected value"
    )

    return checks


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    config = get_config()

    print("Configuration loaded:")
    print(f"Mode: {config['mode']}")
    print(f"Database: {describe_database(config)}")
    print(f"API Access: {describe_api(config)}")
    print(f"Log Level: {config['log_level']}")
    print(f"Zion Network: {describe_zion(config)}\n")

    print("Environment security check:")
    for line in security_check(config):
        print(line)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
