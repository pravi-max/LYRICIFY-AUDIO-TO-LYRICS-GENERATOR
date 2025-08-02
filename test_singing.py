from utils.uberduck_api import UberduckAPI

def test_singing():
    print("🎵 Starting Uberduck API test...")
    
    # Initialize API
    uberduck = UberduckAPI()
    
    # Test getting voices first
    print("\n🎤 Testing available voices...")
    try:
        voices = uberduck.get_available_voices()
        print(f"✅ Available voices: {voices}")
    except Exception as e:
        print(f"❌ Failed to get voices: {e}")
        return
    
    # Test with a simple lyric
    print("\n🎵 Testing singing generation...")
    test_lyrics = "This is a test of singing voice"
    try:
        # Try with emily voice instead of laura
        path = uberduck.generate_singing(test_lyrics, voice_name="emily", tempo=1.0)
        if path:
            print(f"✅ File saved at: {path}")
        else:
            print("❌ No file path returned")
    except Exception as e:
        print(f"❌ Uberduck failed: {e}")

if __name__ == "__main__":
    test_singing() 