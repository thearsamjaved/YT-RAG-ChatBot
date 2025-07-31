import streamlit as st
import re

st.set_page_config(layout="centered")

if "youtube_url_value" not in st.session_state:
    st.session_state.youtube_url_value = ""

if "video_id" not in st.session_state:
    st.session_state.video_id = None
if "error_message" not in st.session_state:
    st.session_state.error_message = None
if "should_switch_page" not in st.session_state:
    st.session_state.should_switch_page = False


def extract_id_from_url(url: str) -> str | None:
    if not url:
        return None
    pattern = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.search(string=url, pattern=pattern)
    return match.group(1)


def on_search_button_click():
    st.session_state.video_id = None
    st.session_state.error_message = None

    youtube_url_from_state = st.session_state.youtube_url_input
    video_id = extract_id_from_url(youtube_url_from_state)

    if video_id:
        st.session_state.video_id = video_id
        st.success(body=f"Got Video ID {st.session_state.video_id}", icon="✅")
        st.session_state.youtube_url_value = youtube_url
        st.session_state.video_id = video_id
        st.session_state.should_switch_page = True
    else:
        st.session_state.error_message = "Invalid YouTube URL. Please try another one."


st.title("YouTube ChatBot")

if st.session_state.error_message:
    st.error(body="Please Enter A Valid YouTube URL")


col1, col2 = st.columns(
    [5, 1],
    vertical_alignment="bottom",
)

with col1:
    youtube_url = st.text_input(
        label="YouTube Video URL",
        placeholder="Paste YouTube URL Here",
        key="youtube_url_input",
    )
with col2:
    st.button(label="Search", icon="🔍", on_click=on_search_button_click)
if st.session_state.should_switch_page:
    st.switch_page(
        "pages/chatbot_screen.py",
    )
