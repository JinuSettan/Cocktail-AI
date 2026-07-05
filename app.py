import streamlit as st
import streamlit.components.v1 as components

# പേജ് സെറ്റിംഗ്സ്
st.set_page_config(page_title="Cocktail AI", page_icon="🍸", layout="wide")

# ടൈറ്റിൽ
st.title("🍸 Cocktail AI")
st.subheader("Maya V.3.0 - Ultimate Roast Mode")

# ഇവിടെയാണ് നിന്റെ Hugging Face Space വരുന്നത്
components.iframe("https://cocateail-z-ai-x-maya.hf.space", height=600)
