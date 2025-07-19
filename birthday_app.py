import streamlit as st
from PIL import Image
import os
import time

# --- Happy Birthday CSS Styling ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Comic+Neue:wght@400;700&display=swap');
    
    /* Main background with animated gradient */
    .stApp {
        background: linear-gradient(316deg, #ff9a9e, #fad0c4, #fad0c4, #ffecd2, #ff9a9e);
        background-size: 300% 300%;
        animation: gradient 15s ease infinite;
        font-family: 'Comic Neue', cursive;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50% }
        50% { background-position: 100% 50% }
        100% { background-position: 0% 50% }
    }
    
    /* Header styling */
    .birthday-header {
        font-family: 'Dancing Script', cursive;
        font-size: 3.5rem !important;
        color: #d83f87;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 0.5rem;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    /* Card styling */
    .birthday-card {
        background: rgba(255, 255, 255, 0.9) !important;
        border-radius: 20px !important;
        padding: 2rem !important;
        box-shadow: 0 10px 30px rgba(216, 63, 135, 0.2) !important;
        border: 2px dashed #d83f87;
        margin: 1.5rem 0;
    }
    
    /* Message text */
    .birthday-message {
        font-size: 1.2rem !important;
        line-height: 1.8 !important;
        color: #5a5a5a !important;
    }
    
    /* Gallery image styling */
    .gallery-img {
        border-radius: 15px !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.15) !important;
        transition: transform 0.3s ease !important;
        border: 3px solid white !important;
    }
    
    .gallery-img:hover {
        transform: scale(1.02) !important;
    }
    
    /* Button styling */
    .stButton>button {
        background-color: #d83f87 !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 0.5rem 1.5rem !important;
        font-weight: bold !important;
        border: none !important;
        box-shadow: 0 4px 8px rgba(216, 63, 135, 0.3) !important;
        transition: all 0.3s !important;
    }
    
    .stButton>button:hover {
        background-color: #c72c76 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(216, 63, 135, 0.4) !important;
    }
    
    /* Section headers */
    .section-header {
        font-family: 'Dancing Script', cursive !important;
        color: #d83f87 !important;
        font-size: 2rem !important;
        text-align: center;
        margin: 1.5rem 0 !important;
    }
    
    /* Floating balloons animation */
    .balloons {
        position: fixed;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    }
    
    .image-caption {
        font-size: 1.2em !important;
        font-weight: 600 !important;
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7) !important;
        background: linear-gradient(135deg, #ff4e50aa 0%, #d83f87aa 100%) !important;
        padding: 8px 15px !important;
        border-radius: 20px !important;
        margin-top: 10px !important;
        text-align: center !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2) !important;
    }
    
    .balloon {
        position: absolute;
        width: 50px;
        height: 60px;
        background: #ff6b6b;
        border-radius: 50%;
        animation: float 15s linear infinite;
        opacity: 0.7;
    }
    
    .balloon:before {
        content: "";
        position: absolute;
        width: 2px;
        height: 40px;
        background: #ff6b6b;
        top: 60px;
        left: 24px;
    }
    
    .balloon:nth-child(2) {
        left: 20%;
        background: #4ecdc4;
        animation-delay: 2s;
        animation-duration: 12s;
    }
    
    .balloon:nth-child(3) {
        left: 40%;
        background: #ffbe76;
        animation-delay: 4s;
        animation-duration: 18s;
    }
    
    .balloon:nth-child(4) {
        left: 60%;
        background: #a55eea;
        animation-delay: 1s;
        animation-duration: 14s;
    }
    
    .balloon:nth-child(5) {
        left: 80%;
        background: #78e08f;
        animation-delay: 3s;
        animation-duration: 16s;
    }
    
    @keyframes float {
        0% { transform: translateY(100vh) scale(0.6); }
        100% { transform: translateY(-100vh) scale(1); }
    }
</style>
""", unsafe_allow_html=True)

# --- Floating Balloons Background ---
st.markdown("""
<div class="balloons">
    <div class="balloon"></div>
    <div class="balloon"></div>
    <div class="balloon"></div>
    <div class="balloon"></div>
    <div class="balloon"></div>
</div>
""", unsafe_allow_html=True)

# --- Initialize Session State ---
if 'gallery_index' not in st.session_state:
    st.session_state.gallery_index = 0
    st.balloons()  # Show balloons on first load

# --- Birthday Header ---
st.markdown('<h1 class="birthday-header">Happy Birthday Rachel! 🎉</h1>', unsafe_allow_html=True)

# --- Birthday Card ---
st.markdown("""
<div class="birthday-card">
    <p class="birthday-message">
        Wishing you a wonderful year ahead filled with happiness and success.<br><br>
        I wanted to take a moment to sincerely thank you for all your support - whether it's been your thoughtful advice, practical help, or just being someone I can count on. Your generosity and reliability have made such a difference, and I'm truly grateful to have you in my life.<br><br>
        May this birthday bring you as much joy as you bring to others. Hope you have a relaxing day and get to enjoy all your favorite things!<br><br>
        Best,<br>
        Akyengo_Jr.
    </p>
    <div style="text-align: center; font-size: 2rem;">🎈🎁🎊</div>
</div>
""", unsafe_allow_html=True)

# --- Photo Gallery Section ---
gallery_folder = "gallery"
if not os.path.exists(gallery_folder):
    os.makedirs(gallery_folder, exist_ok=True)

# Load valid images
valid_images = []
for f in os.listdir(gallery_folder):
    try:
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            with Image.open(os.path.join(gallery_folder, f)) as img:
                img.verify()
            valid_images.append(f)
    except (IOError, SyntaxError, Exception) as e:
        st.warning(f"Skipping invalid image file: {f}")

captions = [
    "Birthday Girl 🎀✨", "Queen of the Day 👑", "Shine Bright! ✨",
    "It's Your Moment! 🎉", "Slaying Another Year 💃", "The Star of the Show 🌟",
    "Age is Just a Number 😉", "Unwrap the Fun! 🎁", "Glow Getter 💖", "Born to Sparkle ✨"
]

if valid_images:
    st.markdown('<h2 class="section-header">Photo Gallery</h2>', unsafe_allow_html=True)
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 6, 1])
    with col1:
        if st.button("⬅️ Previous"):
            st.session_state.gallery_index = (st.session_state.gallery_index - 1) % len(valid_images)
            st.balloons()
    with col3:
        if st.button("Next ➡️"):
            st.session_state.gallery_index = (st.session_state.gallery_index + 1) % len(valid_images)
            st.balloons()
    
    # Display current image
    current_idx = st.session_state.gallery_index % len(valid_images)
    img_path = os.path.join(gallery_folder, valid_images[current_idx])
    caption = captions[current_idx % len(captions)]
    
    try:
        img = Image.open(img_path)
        st.image(
            img,
            use_container_width=True,
            caption=st.markdown('<div class="image-caption">{caption}</div>', unsafe_allow_html=True)
            output_format="PNG"
        )
    except Exception as e:
        st.error(f"Error displaying image: {e}")
        st.session_state.gallery_index = 0  # Reset to first image
        st.experimental_rerun()
else:
    st.info("✨ No valid images found in the 'gallery' folder. Please add some images!")

# --- Music Player Section ---
st.markdown('<h2 class="section-header">🎵 Birthday Music</h2>', unsafe_allow_html=True)
music_folder = "music"
if not os.path.exists(music_folder):
    os.makedirs(music_folder, exist_ok=True)

# Initialize music player
if 'current_song' not in st.session_state:
    st.session_state.current_song = None

music_files = [f for f in os.listdir(music_folder) if f.lower().endswith((".mp3", ".wav"))]

if music_files:
    # Create audio placeholder that won't reset on reruns
    audio_placeholder = st.empty()
    
    selected_song = st.selectbox(
        "Choose a song:", 
        music_files,
        key="song_selector"
    )
    
    # Only reload if song changed
    if selected_song != st.session_state.current_song:
        try:
            with open(os.path.join(music_folder, selected_song), "rb") as audio_file:
                audio_bytes = audio_file.read()
            st.session_state.current_song = selected_song
            st.session_state.audio_bytes = audio_bytes
        except Exception as e:
            st.error(f"Error loading audio file: {e}")
    
    # Display audio player
    if hasattr(st.session_state, 'audio_bytes'):
        audio_placeholder.audio(
            st.session_state.audio_bytes,
            format="audio/mp3"
        )
else:
    st.info("🎶 No music files found. Add MP3 or WAV files to the 'music' folder.")

# --- Final Celebration ---
st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <h3 style="color: #d83f87;">Wishing you the happiest of birthdays!</h3>
    <div style="font-size: 2rem; margin: 1rem 0;">🎂 🥳 🎊 🎁 🎈</div>
</div>
""", unsafe_allow_html=True)
