import streamlit as st
import time
from app import rag_chain 

st.set_page_config(page_title="Chatbot Médical IA", page_icon="🩺")
st.title("Chatbot Médical IA")
st.write("Posez vos questions sur les maladies et le chatbot vous répondra.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage historique
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Entrée utilisateur
if user_input := st.chat_input("Écrivez votre question ici..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("...")
        time.sleep(1)

        # Appel RAG/LLM
        try:
            response = rag_chain.invoke({"input": user_input})
            chatbot_response = response["answer"]
        except Exception as e:
            chatbot_response = f"Erreur : {e}"

        placeholder.markdown(chatbot_response)
        st.session_state.messages.append({"role": "assistant", "content": chatbot_response})