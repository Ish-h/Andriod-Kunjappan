import streamlit as st
import base64
import os

def set_custom_ui():
    import base64
    import streamlit as st

    with open("assets/bg.jpg", "rb") as f:
        bg_data = base64.b64encode(f.read()).decode()

    st.markdown(f"""
        <style>
        html, body, .stApp {{
            height: 100%;
            margin: 0;
            padding: 0;
            background-color: #f4e4cf; 
            background-image: url("data:image/png;base64,{bg_data}");
            background-size: 100% 100%;
            background-attachment: fixed;
            background-repeat: no-repeat;
            background-position: center center;
            min-height: 100vh;
            box-sizing: border-box;
            overflow-x: hidden;
        }}

        #root, .main, .block-container {{
            min-height: 100vh !important;
            height: 100vh !important;
            margin: 0 !important;
            padding-bottom: 0 !important;
            box-sizing: border-box;
        }}

        /* Remove white space at the bottom (footer-like area) */
        [data-testid="stBottom"],
        [data-testid="stBottomBlockContainer"],
        [data-testid="stChatInput"] {{
            background: transparent !important;
            box-shadow: none !important;
            margin: 0 !important;
            padding: 0 !important;
            min-height: 0 !important;
            height: auto !important;
        }}

        [data-testid="stVerticalBlock"] {{
            margin-bottom: 0 !important;
            padding-bottom: 0 !important;
            background: transparent !important;
        }}

        .block-container > div:last-child {{
            margin-bottom: 0 !important;
            padding-bottom: 0 !important;
            background: transparent !important;
        }}

        .stChatMessage, .st-emotion-cache-1c7y2kd, .st-emotion-cache-16txtl3 {{
            background: #fff !important;
            border-radius: 14px !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.07) !important;
            padding: 14px 18px !important;
            margin-bottom: 0.7rem !important;
            font-size: 18px !important;
            line-height: 1.6 !important;
            border: 1px solid #ececec !important;
        }}

        /* Highlight all chat messages (user and bot) in a white box */
        [data-testid="stChatMessage"] > div {{
            background: #fff !important;
            border-radius: 14px !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.07) !important;
            padding: 14px 18px !important;
            margin-bottom: 0.7rem !important;
            font-size: 18px !important;
            line-height: 1.6 !important;
            border: 1px solid #ececec !important;
       }}

        /* Only highlight the message text, not the avatar/icon */
        [data-testid="stChatMessageContent"] {{
            background: #fff !important;
            border-radius: 14px !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.07) !important;
            padding: 14px 18px !important;
            margin-bottom: 0.7rem !important;
            font-size: 18px !important;
            line-height: 1.6 !important;
            border: 1px solid #ececec !important;
        }}

        footer {{
            background-color: transparent !important;
            height: 0 !important;
            min-height: 0 !important;
            margin: 0 !important;
            padding: 0 !important;
        }}
        header {{
            background-color: transparent !important;
            height: 0 !important;
            min-height: 0 !important;
            margin: 0 !important;
            padding: 0 !important;
        }}

        .stMarkdown p, .stTextInput, .stTextArea textarea, .stExpander, .stButton button, label, .st-bb, .st-bc {{
            font-weight: 600 !important;
            background-color: transparent !important;
        }}
        
        /* Remove all extra space and background from bottom containers */
        [data-testid="stBottom"] *,
        [data-testid="stBottomBlockContainer"] *,
        [data-testid="stChatInput"] *,
        [data-testid="stVerticalBlock"] *,
        .stChatInput, .stVerticalBlock, .stElementContainer, .element-container {{
            background: transparent !important;
            box-shadow: none !important;
            margin: 0 !important;
            padding: 0 !important;
            min-height: 0 !important;
            height: auto !important;
            border: none !important;
        }}

        /* Remove min-height from the chat input's parent containers */
        [data-testid="stBottom"],
        [data-testid="stBottomBlockContainer"],
        [data-testid="stChatInput"],
        [data-testid="stVerticalBlock"] {{
            min-height: 0 !important;
            height: auto !important;
            background: transparent !important;
        }}

        /* Remove any flex/grid spacing at the bottom */
        [data-testid="stBottom"] > div,
        [data-testid="stBottomBlockContainer"] > div,
        [data-testid="stVerticalBlock"] > div {{
            margin: 0 !important;
            padding: 0 !important;
            min-height: 0 !important;
            height: auto !important;
            background: transparent !important;
        }}

        /* Highlight the chat input area for better visibility */
        [data-testid="stChatInput"] textarea {{
            background: rgba(255,255,255,0.85) !important;
            border: 2px solid #bfa16c !important;
            border-radius: 12px !important;
            color: #222 !important;
            box-shadow: 0 2px 8px rgba(191,161,108,0.15) !important;
            font-size: 18px !important;
            padding: 10px !important;
        }}

        /* Optional: Add a subtle background to the chat input container */
        [data-testid="stChatInput"] {{
            background: rgba(250, 235, 215, 0.7) !important;
            border-radius: 16px !important;
            padding: 8px !important;
            box-shadow: 0 2px 12px rgba(191,161,108,0.08) !important;
        }}
        </style>
    """, unsafe_allow_html=True)


def display_about_section():
    with st.expander(" കുഞ്ഞപ്പനെ കുറിച്ച്?", expanded=False):
        st.write("കുഞ്ഞപ്പൻ മുതിർന്നവർക്കായി നിർമ്മിച്ചതാണ്. മലയാളത്തിൽ എളുപ്പത്തിൽ സ്മാർട്ട്ഫോൺ ഉപയോഗിക്കാൻ സഹായിക്കും.")

def display_function_icon():
    show_icons = st.toggle("📱 പ്രധാന ഫോൺ ഉപയോഗങ്ങൾ കാണിക്കൂ", value=False)

    if show_icons:
        icons = {
            "കോൾ": "assets/call.jpg",
            "മെസ്സേജ്": "assets/message.png",
            "ഗാലറി": "assets/gallery.jpg",
            "ക്യാമറ": "assets/camera.jpg",
            "വാട്സാപ്പ്": "assets/whatsapp.jpg",
            "സജ്ജീകരണം": "assets/settings.png"
        }

        st.markdown("### 📱 മുഖ്യ ഫോൺ സഹായങ്ങൾ")

        with st.container():
            rows = [list(icons.items())[i:i+3] for i in range(0, len(icons), 3)]
            for row in rows:
                cols = st.columns(len(row))
                for col, (label, path) in zip(cols, row):
                    with col:
                        if os.path.exists(path):
                            st.image(path, width=50)
                        else:
                            st.write("No image")
                        st.markdown(f"<div style='text-align:center'><b>{label}</b></div>", unsafe_allow_html=True)
