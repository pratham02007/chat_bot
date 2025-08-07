import streamlit as st
import google.generativeai as genai

# Configure the page
st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# TODO: Replace with your actual API key
API_KEY = "AIzaSyD1zCTZTZiGmhnW8_KVckza8Rx6S6UQJAQ"

# Configure Gemini AI
genai.configure(api_key=API_KEY)

# App title
st.title("🤖 My First AI Chatbot")
st.write("Welcome! Ask me anything and I'll help you.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
    else:
        with st.chat_message("assistant"):
            st.write(message["content"])

# Function to get AI response
def get_ai_response(user_question):
    try:
        # Create AI model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Get response from AI
        response = model.generate_content(user_question)
        return response.text
    
    except Exception as e:
        return "Sorry, I'm having trouble right now. Please try again!"

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Show user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            ai_response = get_ai_response(user_input)
            st.write(ai_response)
    
    # Add AI response to chat
    st.session_state.messages.append({"role": "assistant", "content": ai_response})

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Instructions for students
st.markdown("---")
st.markdown("""
### 💡 Try asking:
- Tell me a joke
- Explain what AI is
- Help me with math problems
- Write a short story
- What's the weather like? (Note: I can't access real-time data)
""")
