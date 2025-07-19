import streamlit as st
from PIL import Image
import os

# --- Custom CSS ---
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #f9d423 0%, #ff4e50 100%) !important;
    }
    .main {
        background: none !important;
    }
    .gallery-img {
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        margin-bottom: 1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Welcome headline and confetti ---
st.balloons()
st.markdown("""
    <h1 style='text-align:center; font-size:3em; background: linear-gradient(90deg, #f9d423, #ff4e50); -webkit-background-clip: text; color: transparent;'>
        Happy Birthday! 🎉🎂
    </h1>
""", unsafe_allow_html=True)

# --- Prewritten birthday card message (fixed unicode error) ---
st.markdown("""
<div style='display:flex; justify-content:center; margin-top:2em;'>
  <div style='background: #fffbe7; border-radius: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); padding: 2em 3em; max-width: 500px; text-align: center;'>
    <h2 style='color:#ff4e50;'>Happy Birthday, Rachel!</h2>
    <p style='font-size:1.2em; color:#333;'>
        Girl, where do I even start? You’re the kind of friend who’s always there—whether I need a prayer, a pep talk, or just someone to laugh with (or at me when I’m being extra 😂). You always show up, and I appreciate you so much.<br>
        Today is all about YOU! I hope it’s filled with all the love, joy, and blessings you pour into everyone else’s lives. You deserve the world and more.<br>
        Thanks for being the realest, the kindest, and the absolute GOAT of friends. 🏆<br><br>
        Now go celebrate like the queen you are! 🥂💖<br><br>
        Love you loads! ❤️<br><br>
        P.S. Don’t worry, I got the cake (or wine, whichever you prefer 😉). Let’s turn up!<br><br>
        This app is a little messed up but I think you can manage 😂
    </p>
    <div style='font-size:2em;'>🎉🎁🍰</div>
  </div>
</div>
""", unsafe_allow_html=True)

# --- Gallery Section: Manual Slideshow ---
st.subheader("Photo Gallery 📸")
gallery_folder = "gallery"
if not os.path.exists(gallery_folder):
    os.makedirs(gallery_folder)
images = [f for f in os.listdir(gallery_folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]

if images:
    if 'gallery_idx' not in st.session_state:
        st.session_state['gallery_idx'] = 0

    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        img_path = os.path.join(gallery_folder, images[st.session_state['gallery_idx']])
        st.image(Image.open(img_path), use_column_width=True, caption=images[st.session_state['gallery_idx']], output_format="auto")

    col1, col2, col3 = st.columns([1, 6, 1])
    with col1:
        if st.button("Previous") and st.session_state['gallery_idx'] > 0:
            st.session_state['gallery_idx'] -= 1
    with col3:
        if st.button("Next") and st.session_state['gallery_idx'] < len(images) - 1:
            st.session_state['gallery_idx'] += 1
else:
    st.info("No pictures in the gallery yet. Add images to the 'gallery' folder.")

# --- Music Section: Streamlit Audio Widget ---
music_folder = "music"
if not os.path.exists(music_folder):
    os.makedirs(music_folder)
music_files = [f for f in os.listdir(music_folder) if f.lower().endswith((".mp3", ".wav"))]
if music_files:
    selected_song = music_files[0]
    audio_path = os.path.join(music_folder, selected_song)
    try:
        with open(audio_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
        file_ext = os.path.splitext(selected_song)[1].lower()
        if file_ext == ".mp3":
            st.audio(audio_bytes, format="audio/mp3")
        elif file_ext == ".wav":
            st.audio(audio_bytes, format="audio/wav")
        else:
            st.audio(audio_bytes)  # fallback
        st.info("If music does not play automatically, please click the play button above. Some browsers require user interaction to start audio.")
    except Exception as e:
        st.error(f"Error loading audio file: {e}")
else:
    st.info("No music files found in the 'music' folder. Please add .mp3 or .wav files.")
