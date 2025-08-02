from utils.uberduck_api import UberduckAPI
import os
from dotenv import load_dotenv

def test_uberduck():
    try:
        # Initialize API
        api = UberduckAPI()
        
        # Test getting voices
        print("Testing voice list...")
        voices = api.get_available_voices()
        print(f"Available voices: {voices}")
        
        # Test generating singing with a simple lyric
        print("\nTesting singing generation...")
        test_lyrics = "This is a test lyric"
        audio_url = api.generate_singing(test_lyrics, voice_name="laura", tempo=1.0)
        print(f"Generated audio URL: {audio_url}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_uberduck() 