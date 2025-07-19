import streamlit as st
from PIL import Image
import os
import random
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
    
    /* Confetti effect */
    .confetti {
        position: fixed;
        width: 10px;
        height: 10px;
        background-color: #f00;
        opacity: 0.7;
        animation: confetti 5s ease-in-out infinite;
    }
    
    @keyframes confetti {
        0% { transform: translateY(0) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(720deg); opacity: 0; }
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
if "balloons_shown" not in st.session_state:
    st.session_state.balloons_shown = True
    st.balloons()

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


# --- Initialize Session State ---
if 'gallery_idx' not in st.session_state:
    st.session_state.gallery_idx = 0
    st.session_state.last_update = time.time()
    st.session_state.initialized = True

# --- Gallery Section ---
gallery_folder = "gallery"
if not os.path.exists(gallery_folder):
    os.makedirs(gallery_folder)
    
images = [f for f in os.listdir(gallery_folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
captions = [
    "Smile  ✨",
    "Queen of hearts 👑",
    "Beautiful inside and out 🌸",
    "Today's all yours 💞",
    "So blessed to have you in my life 🙏",
    "The star of today's show 🌟",
    "Age? Just a number! You're forever young 💃",
    "Unstoppable force 🌈",
    "God's masterpiece 🎨"
]

if images:
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 6, 1])
    with col1:
        if st.button("⬅️ Previous"):
            st.session_state.gallery_idx = (st.session_state.gallery_idx - 1) % len(images)
            st.session_state.last_update = time.time()
    with col3:
        if st.button("Next ➡️"):
            st.session_state.gallery_idx = (st.session_state.gallery_idx + 1) % len(images)
            st.session_state.last_update = time.time()
    
    # Display current image and caption
    current_idx = st.session_state.gallery_idx % len(images)
    img_path = os.path.join(gallery_folder, images[current_idx])
    caption = captions[current_idx % len(captions)]
    
    st.image(
        Image.open(img_path),
        use_container_width=True,
        caption=caption
    )
    
    # Auto-advance logic
    if time.time() - st.session_state.last_update > 3:
        st.session_state.gallery_idx = (st.session_state.gallery_idx + 1) % len(images)
        st.session_state.last_update = time.time()
        time.sleep(0.1)  # Small delay to prevent rapid updates
        st.rerun()
else:
    st.info("✨ Photos coming soon! Add images to the 'gallery' folder to see them here!")

# --- Music Player Section ---
st.subheader("🎵 Birthday Music")
music_folder = "music"
if not os.path.exists(music_folder):
    os.makedirs(music_folder)
    
music_files = [f for f in os.listdir(music_folder) if f.lower().endswith((".mp3", ".wav"))]

if music_files:
    selected_song = st.selectbox("Choose a song:", music_files)
    audio_file = open(os.path.join(music_folder, selected_song), "rb")
    audio_bytes = audio_file.read()
    
    st.audio(audio_bytes, format="audio/mp3")
    st.info("Click the play button to start the music!")
else:
    st.info("🎶 Add some MP3 or WAV files to the 'music' folder for birthday tunes!")
