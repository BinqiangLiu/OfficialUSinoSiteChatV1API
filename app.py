import requests
import streamlit as st

st.set_page_config(page_title="USinoIP Website AI Chat Assistant - Open Source Version", layout="wide")
st.subheader("Welcome to USinoIP Website AI Chat Assistant - Open Source Version.")
st.write("Important notice: This USinoIP Website AI Chat Assistant is offered ONLY for the purpose of assisting users to better interact with USinoIP webiste contents and by no means for any other use. Any user should never interact with the AI Assistant in any way that is against any related promulgated regulations. The user is the only entity responsible for interactions taken between the user and the AI Chat Assistant.")

css_file = "main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

def call_chatbot_api(query):
    #url = 'https://binqiangliu-fastapi-in-docker.hf.space/api/chat'
    url = 'https://binqiangliu-officialusinositechatv1api.hf.space/api/chat'
    json_data_for_api = {'user_question': query}
    response = requests.post(url, json=json_data_for_api) 
    result = response.json()
    return result['response']
    
user_query = st.text_input("Enter your query here:")
with st.spinner("AI Thinking...Please wait a while to Cheers!"):    
    if user_query !="" and not user_query.strip().isspace() and not user_query == "" and not user_query.strip() == "" and not user_query.isspace():
        response = call_chatbot_api(user_query)
        st.write("USino AI Response:")
        st.write(response)
        print(response)  # 打印Chatbot的响应
