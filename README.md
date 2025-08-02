# Lyricify 🎶
An AI-powered music analysis and lyrics generation app that creates custom lyrics for your music based on mood and tempo.

## Features
- 🎵 Upload and analyze audio/video files
- 🎭 Detect mood and tempo automatically
- 📝 Generate custom lyrics using AI
- 🎤 Convert lyrics to singing voice
- 🎼 Mix vocals with original music
- 📊 View matching accuracy metrics

## Prerequisites
- Python 3.8 or higher
- FFmpeg installed on your system
- CUDA-capable GPU (optional, but recommended for faster processing)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/lyricify.git
cd lyricify
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install FFmpeg:
- Windows: Download from https://ffmpeg.org/download.html
- macOS: `brew install ffmpeg`
- Linux: `sudo apt-get install ffmpeg`

## Usage

1. Start the app:
```bash
streamlit run main.py
```

2. Open your browser and go to `http://localhost:8501`

3. Upload your audio/video file (supported formats: mp3, wav, mp4, m4a)

4. Wait for the analysis and lyrics generation

5. Listen to the generated vocals and mixed version

## How It Works

1. **Audio Analysis**: The app analyzes your music to detect:
   - Mood (energetic, chill, sad, happy)
   - Tempo (BPM)
   - Energy levels
   - Rhythm patterns

2. **Lyrics Generation**: Using AI to create lyrics that match:
   - The detected mood
   - The song's tempo
   - Musical structure
   - Natural flow

3. **Voice Synthesis**: Converts lyrics to singing voice with:
   - Natural pitch variations
   - Musical expression
   - Professional audio effects

4. **Audio Mixing**: Combines the generated vocals with original music:
   - Dynamic balance
   - Professional effects
   - High-quality output

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
