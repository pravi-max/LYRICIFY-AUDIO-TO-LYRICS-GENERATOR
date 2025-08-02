
import streamlit as st
from utils.audio_analysis import analyze_audio
from utils.lyric_generator import generate_lyrics
from utils.file_utils import save_uploaded_file

st.title("🎵 Lyricify: Audio to Lyrics Generator")

uploaded_file = st.file_uploader("Upload an audio or video file", type=["mp3", "wav", "mp4", "m4a"])
if uploaded_file is not None:
    file_path = save_uploaded_file(uploaded_file)
    mood, tempo = analyze_audio(file_path)
    lyrics = generate_lyrics(mood, tempo)
    st.subheader("🎤 Generated Lyrics")
    st.text(lyrics)
              