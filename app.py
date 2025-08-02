import streamlit as st
import os
import time
from utils.audio_analysis import analyze_audio, text_to_speech, mix_audio, calculate_matching_accuracy
from utils.lyric_generator import generate_lyrics
from utils.file_utils import save_uploaded_file

# Page settings
st.set_page_config(page_title="Lyricify 🎶", page_icon="🎵", layout="wide")

def safe_remove_file(file_path):
    """Safely remove a file if it exists"""
    try:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Error removing file: {str(e)}")

st.title("🎵 Lyricify - Music to Lyrics Generator")

# Create temp directory if it doesn't exist
os.makedirs("temp", exist_ok=True)

# Create two columns for the layout
col1, col2 = st.columns(2)

with col1:
    st.write("### 🎵 Upload Your Music")
    uploaded_file = st.file_uploader("📁 Upload an audio or video file", type=["mp3", "wav", "mp4", "m4a"])

    if uploaded_file is not None:
        # Initialize variables
        file_path = None
        lyrics_audio_path = None
        mixed_audio_path = None
        
        try:
            # Save the uploaded file
            file_path = save_uploaded_file(uploaded_file)
            if not file_path:
                st.error("Failed to save uploaded file")
                st.stop()
            
            # Analyze the audio
            mood, tempo = analyze_audio(file_path)
            
            st.write(f"🎭 Detected Mood: {mood}")
            st.write(f"🎵 Detected Tempo: {tempo} BPM")
            
            # Add this in app.py after mood detection
            st.write("### 🎨 Mood Visualization")
            mood_colors = {
                "energetic": "#FF4500",  # Orange Red
                "chill": "#4169E1",      # Royal Blue
                "sad": "#483D8B",        # Dark Slate Blue
                "happy": "#FFD700"       # Gold
            }

            # Create a color-coded mood indicator
            st.markdown(f"""
            <div style='background-color: {mood_colors[mood]}; padding: 20px; border-radius: 10px; text-align: center;'>
                <h2 style='color: white;'>{mood.upper()}</h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Generate lyrics
            lyrics = generate_lyrics(mood, tempo)
            st.write("📝 Generated Lyrics:")
            st.text_area("Generated Lyrics", lyrics, height=200)
            
            # Voice selection
            voice_options = ["default", "female", "male"]
            selected_voice = st.selectbox("Select a voice:", voice_options)
            
            # Tempo control
            tempo_control = st.slider("Adjust Tempo", min_value=0.5, max_value=2.0, value=1.0, step=0.1)
            
            # Generate singing button
            if st.button("Generate Singing"):
                with st.spinner("Generating singing audio..."):
                    # Convert lyrics to singing
                    lyrics_audio_path = text_to_speech(lyrics, "temp/lyrics.wav", voice_name=selected_voice, tempo=tempo_control)
                    if not lyrics_audio_path:
                        st.error("Failed to generate singing voice")
                        st.stop()
                    
                    # Mix audio
                    mixed_audio_path = mix_audio(file_path, lyrics_audio_path, "temp/mixed.wav")
                    if not mixed_audio_path:
                        st.error("Failed to mix audio")
                        st.stop()
                    
                    # Calculate matching accuracy
                    accuracy = calculate_matching_accuracy(file_path, lyrics_audio_path)
                    if not accuracy:
                        st.error("Failed to calculate accuracy")
                        st.stop()
                    
                    # Display results with progress bars
                    st.write("🎯 Matching Accuracy:")
                    
                    # Rhythm Match
                    st.write("Rhythm Match:")
                    st.progress(float(accuracy['rhythm_match']) / 100)
                    st.write(f"{float(accuracy['rhythm_match']):.1f}%")
                    
                    # Tempo Match
                    st.write("Tempo Match:")
                    st.progress(float(accuracy['tempo_match']) / 100)
                    st.write(f"{float(accuracy['tempo_match']):.1f}%")
                    
                    # Energy Match
                    st.write("Energy Match:")
                    st.progress(float(accuracy['energy_match']) / 100)
                    st.write(f"{float(accuracy['energy_match']):.1f}%")
                    
                    # Overall Score
                    st.write("Overall Score:")
                    st.progress(float(accuracy['overall_score']) / 100)
                    st.write(f"{float(accuracy['overall_score']):.1f}%")
                    
                    # Display combined audio
                    st.write("### 🎧 Combined Audio")
                    st.write("🎵 Original Music")
                    st.audio(file_path)
                    
                    st.write("🎤 Generated Lyrics")
                    st.audio(lyrics_audio_path)
                    
                    st.write("🎼 Final Mix")
                    st.audio(mixed_audio_path)
                    
                    # Clean up temporary files
                    files_to_cleanup = [file_path, lyrics_audio_path, mixed_audio_path]
                    for file in files_to_cleanup:
                        if file:  # Only remove if file exists
                            safe_remove_file(file)
                        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            # Clean up any files that might have been created
            for file in [file_path, lyrics_audio_path, mixed_audio_path]:
                if file:  # Only remove if file exists
                    safe_remove_file(file)

with col2:
    # Instructions and examples
    st.subheader("How to Use")
    st.markdown("""
    1. Upload your music file (MP3, WAV, MP4, or M4A)
    2. The app will analyze the mood and tempo
    3. Lyrics will be generated based on the mood and tempo
    4. Select a voice for the singing
    5. Adjust the tempo if needed
    6. Click 'Generate Singing' to create the final mix
    
    **Tips:**
    - Keep your music file under 10MB
    - Try different voices for different styles
    - Adjust tempo to match your desired speed
    - The generated lyrics will match the mood of your music
    """)
    
    # Example moods and tempos
    st.subheader("Example Moods and Tempos")
    st.markdown("""
    - **Energetic**: Fast tempo, high energy
    - **Chill**: Slow tempo, relaxed vibe
    - **Sad**: Slow tempo, emotional
    - **Happy**: Medium tempo, upbeat
    """)

if uploaded_file is None:
    st.info("👆 Please upload a file to get started!") 