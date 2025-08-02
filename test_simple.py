import os
from dotenv import load_dotenv

def test_env():
    # Load environment variables
    load_dotenv()
    
    # Print current working directory
    print(f"Current working directory: {os.getcwd()}")
    
    # Check if .env file exists
    env_path = os.path.join(os.getcwd(), '.env')
    print(f"Looking for .env file at: {env_path}")
    print(f".env file exists: {os.path.exists(env_path)}")
    
    # Try to get API credentials
    api_key = os.getenv('pub_tlvwacgreszuarxdoc')
    api_secret = os.getenv('pk_afd82824-694c-4559-b896-2ce3b566f46b')
    
    print("\nAPI Credentials:")
    print(f"API Key: {api_key}")
    print(f"API Secret: {api_secret}")

if __name__ == "__main__":
    test_env() 