import streamlit as st

st.set_page_config(page_title="Cocktail AI", page_icon="🍸")
st.title("🍸 Cocktail AI")
st.subheader("Maya V.3.0 - Ultimate Roast Mode")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("മായയോട് എന്തെങ്കിലും ചോദിക്കൂ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = "ഇതൊരു ടെസ്റ്റ് മെസ്സേജ് ആണ്, ഉടനെ API കണക്ട് ചെയ്യാം!"
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
