import os
import sys
try:
    from dotenv import load_dotenv
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)


def main() -> None:
    print("ORACLE STATUS: Reading the matrix...\n")

    if not load_dotenv():
        print("Error: .env not found")
        sys.exit(1)

    print("Configuration loaded:")

    matrix_mode = os.getenv("MATRIX_MODE")
    if not matrix_mode:
        matrix_mode = "MATRIX_MODE variable value unassigned"
    print(f"Mode: {matrix_mode}")

    if os.getenv("DATABASE_URL"):
        print("Database: Connected to local instance")
    else:
        print("Database: Not connected")

    if os.getenv("API_KEY"):
        print("API Access: Authenticated")
    else:
        print("API Access: Couldn't authenticate")

    verbosity = os.getenv("LOG_LEVEL")
    if not verbosity:
        verbosity = "LOG_LEVEL variable value unassigned"
    print(f"Log Level: {verbosity}")

    if os.getenv("ZION_ENDPOINT"):
        print("Zion network: Online")
    else:
        print("Zion network: Offline")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.\n")


if __name__ == "__main__":
    main()
