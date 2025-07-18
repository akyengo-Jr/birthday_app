import streamlit as st
from streamlit_extras.animated_headline import animated_headline
from streamlit_extras.let_it_rain import rain
from PIL import Image
import os
import json


st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f9d423 0%, #ff4e50 100%);
        color: #fff;
    }
    .stButton>button {
        background-color: #ff4e50;
        color: white;
        border-radius: 20px;
        font-size: 18px;
        padding: 0.5em 2em;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #f9d423;
        font-size: 18px;
    }
    .stSlider>div>div>div {
        background: #f9d423;
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

# Welcome animation
animated_headline(
    "Happy Birthday! 🎉🎂",
    animation="rainbow",
    font_size="60px"
)

# Input for name and age
if 'name' not in st.session_state:
    st.session_state['name'] = ''
if 'age' not in st.session_state:
    st.session_state['age'] = 0

with st.form("birthday_form"):
    name = st.text_input("What's your name?")
    age = st.number_input("How old are you today?", min_value=1, max_value=120, step=1)
    submitted = st.form_submit_button("Enter")
    if submitted and name and age:
        st.session_state['name'] = name
        st.session_state['age'] = age

if st.session_state['name'] and st.session_state['age']:
    # Balloons and cakes animation
    rain(
        emoji="🎈",
        font_size=54,
        falling_speed=5,
        animation_length="infinite"
    )
    rain(
        emoji="🎂",
        font_size=54,
        falling_speed=7,
        animation_length="infinite"
    )
    st.markdown(f"<h2 style='text-align:center;'>Happy {st.session_state['age']}th Birthday, {st.session_state['name']}! 🎉</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center;'>Wishing you a day filled with love, laughter, and cake! 🍰</h4>", unsafe_allow_html=True)

    # --- Customizable Themes ---
    theme = st.selectbox("Choose a theme:", ["Sunshine", "Party", "Ocean", "Classic"])
    theme_colors = {
        "Sunshine": ("#f9d423", "#ff4e50"),
        "Party": ("#ff6f61", "#6a0572"),
        "Ocean": ("#43cea2", "#185a9d"),
        "Classic": ("#fff", "#333")
    }
    bg1, bg2 = theme_colors[theme]
    st.markdown(f"""
        <style>
        .main {{background: linear-gradient(135deg, {bg1} 0%, {bg2} 100%);}}
        </style>
    """, unsafe_allow_html=True)

    # --- Music Player ---
    st.subheader("🎵 Birthday Music")
    music_folder = "music"
    if not os.path.exists(music_folder):
        os.makedirs(music_folder)
    music_files = [f for f in os.listdir(music_folder) if f.lower().endswith((".mp3", ".wav"))]
    if music_files:
        selected_song = st.selectbox("Pick a song to play:", music_files)
        audio_bytes = open(os.path.join(music_folder, selected_song), 'rb').read()
        st.audio(audio_bytes, format='audio/mp3')
    else:
        st.info("Add mp3 or wav files to the 'music' folder to play birthday songs!")

    # --- Confetti Animation ---
    if st.button("🎊 Celebrate with Confetti!"):
        st.balloons()
        st.snow()

    # --- Photo Upload ---
    st.subheader("Upload a Photo to the Gallery")
    gallery_folder = "gallery"  # Ensure gallery_folder is defined here
    if not os.path.exists(gallery_folder):
        os.makedirs(gallery_folder)
    uploaded_img = st.file_uploader("Choose an image to upload", type=["jpg", "jpeg", "png", "gif"])
    if uploaded_img is not None:
        img_path = os.path.join(gallery_folder, uploaded_img.name)
        with open(img_path, "wb") as f:
            f.write(uploaded_img.getbuffer())
        st.success(f"Uploaded {uploaded_img.name} to the gallery!")

    # --- Voice Wishes ---
    st.subheader("🎤 Record or Upload a Voice Wish!")
    voice_folder = "voice_wishes"
    if not os.path.exists(voice_folder):
        os.makedirs(voice_folder)
    voice_file = st.file_uploader("Upload a voice wish (mp3 or wav)", type=["mp3", "wav"], key="voice")
    if voice_file is not None:
        v_path = os.path.join(voice_folder, voice_file.name)
        with open(v_path, "wb") as f:
            f.write(voice_file.getbuffer())
        st.success(f"Uploaded {voice_file.name}!")
    voice_files = [f for f in os.listdir(voice_folder) if f.lower().endswith((".mp3", ".wav"))]
    if voice_files:
        v_selected = st.selectbox("Play a voice wish:", voice_files)
        v_bytes = open(os.path.join(voice_folder, v_selected), 'rb').read()
        st.audio(v_bytes)

    # Gallery Section
    st.subheader("Photo Gallery 📸")
    gallery_folder = "gallery"
    if not os.path.exists(gallery_folder):
        os.makedirs(gallery_folder)
    images = [f for f in os.listdir(gallery_folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if images:
        img_idx = st.slider("Slide through the gallery", 0, len(images)-1, 0)
        img_path = os.path.join(gallery_folder, images[img_idx])
        st.image(Image.open(img_path), use_column_width=True, caption=images[img_idx], output_format="auto")
    else:
        st.info("No pictures in the gallery yet. Add images to the 'gallery' folder.")

    # Message Section
    wishes_file = "wishes.json"
    st.subheader("🎈 Leave a Birthday Wish!")
    # Load wishes from file
    if os.path.exists(wishes_file):
        with open(wishes_file, "r") as f:
            wishes = json.load(f)
    else:
        wishes = []
    # Add new wish
    with st.form("wish_form"):
        wish = st.text_area("Write your birthday wish for her:", max_chars=200)
        wish_submit = st.form_submit_button("Send Wish")
        if wish_submit and wish.strip():
            wishes.append(wish.strip())
            with open(wishes_file, "w") as f:
                json.dump(wishes, f)
            st.success("Your wish has been added!")
    if wishes:
        st.markdown("<h4>Birthday Wishes from Friends:</h4>", unsafe_allow_html=True)
        for idx, msg in enumerate(reversed(wishes), 1):
            st.markdown(f"<div style='background:#fff3cd;padding:1em;border-radius:10px;margin-bottom:0.5em;color:#333;'><b>Wish {idx}:</b> {msg}</div>", unsafe_allow_html=True)
else:
    st.info("Please enter your name and age to continue.")

# --- Shareable Link ---
st.subheader("🔗 Share this Birthday Page!")
st.info("Share this app's URL with friends so they can join and leave wishes!")

# --- Admin Panel ---
st.subheader("🔒 Admin Panel (Birthday Girl Only)")
admin_pw = st.text_input("Enter admin password to manage wishes:", type="password")
if admin_pw == "happybirthday":
    st.success("Admin access granted!")
    if wishes:
        del_idx = st.selectbox("Select a wish to delete:", [f"Wish {i+1}: {w}" for i, w in enumerate(wishes)])
        if st.button("Delete Selected Wish"):
            idx = [f"Wish {i+1}: {w}" for i, w in enumerate(wishes)].index(del_idx)
            wishes.pop(idx)
            with open(wishes_file, "w") as f:
                json.dump(wishes, f)
            st.success("Wish deleted!")
elif admin_pw:
    st.error("Incorrect password.")
