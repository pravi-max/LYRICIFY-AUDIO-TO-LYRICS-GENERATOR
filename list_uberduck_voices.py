import requests
from requests.auth import HTTPBasicAuth
import os

api_key = "pub_tlvwacgreszuarxdoc"
api_secret = "pk_afd82824-694c-4559-b896-2ce3b566f46b"

auth = HTTPBasicAuth(api_key, api_secret)

# Add this at the start of your script to ensure temp directory permissions
os.makedirs("temp", exist_ok=True)
os.chmod("temp", 0o777)  # Give full permissions to the temp directory

response = requests.get("https://api.uberduck.ai/voices", auth=auth)

if response.status_code == 200:
    voices = response.json()
    singing_voices = [v["name"] for v in voices if v.get("category") == "singing"]
    print("✅ Singing voices:", singing_voices)
else:
    print("❌ Failed to fetch voices:", response.status_code, response.text) 