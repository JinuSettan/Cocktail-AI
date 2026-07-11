import streamlit as st
from langchain_openai import ChatOpenAI

# Title
st.set_page_config(page_title="Cocktail x Z Ai Builder")
st.title("Cocktail x Z Ai - Software Factory")
st.markdown("Powered by Cocktail x Z Ai")

# Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# User Input
user_input = st.text_input("എന്താണ് പണിയേണ്ടത്? (Website / App):")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # AI Logic (ഇവിടെ നിന്റെ അടിമ പ്രവർത്തിക്കും)
    response = f"നീ ആവശ്യപ്പെട്ടത് '{user_input}' ആണ്. ഞാൻ അത് കോഡ് ചെയ്യാൻ റെഡിയാണ്! "
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.write(response)

# Sidebar for controls
st.sidebar.title("Controls")
if st.sidebar.button("Build APK"):
    st.sidebar.write("APK ബിൽഡിംഗ് പ്രക്രിയ തുടങ്ങുന്നു... ഇത് നിന്റെ ഗിറ്റ്ഹബിൽ അപ്‌ഡേറ്റ് ചെയ്യും.")

