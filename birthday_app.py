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
