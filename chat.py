
import google.generativeai as genai
import streamlit as st
st.set_page_config(page_title="GenAI",page_icon=":robot_face:",layout="wide")
st.title("Google gemini chatbot")

api_key ="AIzaSyARWkQgtX-fLng1xBLeAsXzSiGc6ui_t3Y"
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')
  # Initialize conversation history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
prompt=st.chat_input("Enter a prompt:")
if prompt is not None:
    response=model.generate_content(contents=prompt)
    #st.write(response.text)
       # Store the question and response in the chat history
    st.session_state.chat_history.append({"question": prompt, "answer": response.text})
     # Display the conversation history
if st.session_state.chat_history:
    st.subheader("Conversation History:")
    for chat in st.session_state.chat_history:
        st.markdown(f"**You:** {chat['question']}")
        st.markdown(f"**Bot:** {chat['answer']}")

