import streamlit as st
from bot import get_claude_malayalam_reply
from ui import set_custom_ui, display_about_section, display_function_icon

st.set_page_config(page_title="ആൻഡ്രോയിഡ് കുഞ്ഞപ്പൻ 🤖", layout="centered")
set_custom_ui()

st.title("ആൻഡ്രോയിഡ് കുഞ്ഞപ്പൻ 🤖 ")
st.markdown("നമസ്കാരം! എന്ത് സഹായം വേണം എന്ന് എഴുതി ചോദിക്കൂ 👵👴")

display_about_section()
display_function_icon()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat placeholder if no messages
if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown("🤖 കാത്തിരിക്കുന്നു... എന്തെങ്കിലും ചോദിക്കൂ 👇")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input prompt
if prompt := st.chat_input("താങ്കളുടെ ചോദ്യം ഇവിടെ എഴുതൂ 👇"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Claude API response
    response = get_claude_malayalam_reply(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
