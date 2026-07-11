import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Secrets-ൽ നിന്ന് കീ എടുക്കുന്നു (അതുകൊണ്ട് ആപ്പിൽ എവിടെയും കീ കാണിക്കില്ല)
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

# Title
st.set_page_config(page_title="Cocktail x Z Ai Builder", layout="wide")
st.title("Cocktail x Z Ai - Software Factory 🚀")
st.markdown("Powered by Gemini 1.5 Flash - നിന്റെ സ്വന്തം AI അടിമ")

# AI Model Initialization
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# User Input
user_input = st.text_input("എന്താണ് പണിയേണ്ടത്? (Website / App):")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # AI Logic
    with st.spinner('നിന്റെ പ്രോജക്റ്റ് പണിയുന്നു...'):
        response = llm.invoke(f"Create a high-quality code structure for: {user_input}").content
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.write("### AI-യുടെ മറുപടി:")
    st.write(response)

# Sidebar for controls (Features)
st.sidebar.title("Controls")
if st.sidebar.button("Build APK"):
    st.sidebar.success("APK ബിൽഡിംഗ് പ്രക്രിയ തുടങ്ങുന്നു... ⚙️")
    st.sidebar.write("നിന്റെ ഗിറ്റ്ഹബിൽ ഫയലുകൾ അപ്‌ഡേറ്റ് ചെയ്യുന്നു...")

# എക്സ്ട്രാ ഫീച്ചറുകൾ
st.sidebar.markdown("---")
st.sidebar.subheader("Extra Features")
if st.sidebar.button("Generate ReadMe"):
    st.sidebar.info("പ്രോജക്റ്റിനായി ReadMe ഫയൽ ഉണ്ടാക്കുന്നു...")

if st.sidebar.button("Debug Code"):
    st.sidebar.warning("കോഡിലെ പിശകുകൾ പരിശോധിക്കുന്നു...")
