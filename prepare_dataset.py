import os
import shutil
from pathlib import Path

def create_dataset_structure():
    """Create the directory structure for the dataset"""
    # Create main dataset directory
    os.makedirs("music_dataset", exist_ok=True)
    
    # Create mood subdirectories
    moods = ['happy', 'sad', 'energetic', 'calm']
    for mood in moods:
        os.makedirs(os.path.join("music_dataset", mood), exist_ok=True)
    
    print("Dataset directory structure created!")
    print("\nPlease place your music files in the following directories:")
    for mood in moods:
        print(f"- music_dataset/{mood}/")

def main():
    print("Welcome to the Dataset Preparation Tool!")
    print("This tool will help you organize your music files for training.")
    
    # Create directory structure
    create_dataset_structure()
    
    print("\nInstructions:")
    print("1. Place your happy songs in the 'music_dataset/happy' directory")
    print("2. Place your sad songs in the 'music_dataset/sad' directory")
    print("3. Place your energetic songs in the 'music_dataset/energetic' directory")
    print("4. Place your calm songs in the 'music_dataset/calm' directory")
    print("\nNote: Supported file formats are .mp3 and .wav")
    print("Try to have at least 5-10 songs per mood category for better results")

if __name__ == "__main__":
    main() 