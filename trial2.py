import streamlit as st
from bardapi import Bard
import json
import os

from streamlit_chat import message

st.title("Aditya's tutoring chat bot")

with open('credentials.json', 'r') as f:

    file = json.load(f)
    os.environ['_BARD_API_KEY'] = file['token']

def generate_response(prompt):
    bard = Bard(token=os.environ['_BARD_API_KEY'])
    bard = Bard()
    response = bard.get_answer(prompt)['content']
    return response


def get_text():
    input_text = st.text_input("my bot", "hey wassup!!!", key="input")
    return input_text


# url='https://images.unsplash.com/photo-1613023711166-c6ff5d71af6f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=464&q=8'
# data-testid='stAppViewContainer'
changes = '''
<style>
[data-testid = "stAppViewContainer"]
    {

    background-image:url('https://images.unsplash.com/photo-1613023711166-c6ff5d71af6f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzN8fG9jZWFuJTIwYmFja2dyb3VuZHxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60');
    background-size:cover;

    }
    </style>
    '''
st.markdown(changes, unsafe_allow_html=True)
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

user_input = get_text()
if user_input:
    print(user_input)
    output = generate_response(user_input)
    print(output)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)
if st.session_state['generated']:
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], key="user_" + str(i), is_user=True)





